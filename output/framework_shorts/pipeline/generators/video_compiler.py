"""
Video Compiler
Combines visuals, audio, and text overlays into final video
"""

from pathlib import Path
from typing import Dict, Any, List
import subprocess
import json


class VideoCompiler:
    """Compiles visual scenes and audio into final video"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.width = config['video']['resolution']['width']
        self.height = config['video']['resolution']['height']
        self.fps = config['video']['fps']
        self.output_format = config['video']['format']

    def create_scene_sequence(self, scenes: List[Path], timing: Dict[str, float],
                              output_path: Path) -> Path:
        """Create video sequence from scene images based on timing"""

        # Calculate frames per scene based on timing
        # For simplicity, divide time equally among scenes
        total_duration = sum(timing.values())
        frames_per_scene = []

        section_names = list(timing.keys())
        scenes_per_section = len(scenes) // len(section_names) or 1

        for i, section in enumerate(section_names):
            section_duration = timing[section]
            section_frames = int(section_duration * self.fps)

            # Distribute frames across scenes in this section
            for j in range(scenes_per_section):
                scene_idx = i * scenes_per_section + j
                if scene_idx < len(scenes):
                    frames_per_scene.append(section_frames // scenes_per_section)

        # Adjust to use all scenes
        while len(frames_per_scene) < len(scenes):
            frames_per_scene.append(30)  # Default 1 second

        # Create video from images using FFmpeg
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Create concat file for FFmpeg
        concat_file = output_path.parent / "concat_list.txt"

        with open(concat_file, 'w') as f:
            for scene, duration in zip(scenes, frames_per_scene):
                scene_duration = duration / self.fps
                f.write(f"file '{scene.absolute()}'\n")
                f.write(f"duration {scene_duration}\n")

            # Add last image again (FFmpeg concat requirement)
            if scenes:
                f.write(f"file '{scenes[-1].absolute()}'\n")

        # Run FFmpeg to create video from images
        cmd = [
            'ffmpeg',
            '-y',  # Overwrite output
            '-f', 'concat',
            '-safe', '0',
            '-i', str(concat_file),
            '-vf', f'scale={self.width}:{self.height}',
            '-r', str(self.fps),
            '-pix_fmt', 'yuv420p',
            str(output_path)
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            concat_file.unlink()  # Clean up
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg error: {e.stderr}")
            raise

    def add_audio(self, video_path: Path, audio_path: Path, output_path: Path) -> Path:
        """Add audio track to video"""

        output_path = Path(output_path)

        cmd = [
            'ffmpeg',
            '-y',
            '-i', str(video_path),
            '-i', str(audio_path),
            '-c:v', 'copy',  # Copy video without re-encoding
            '-c:a', self.config['video']['audio_codec'],
            '-b:a', self.config['video']['audio_bitrate'],
            '-shortest',  # Match shorter stream
            str(output_path)
        ]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg error: {e.stderr}")
            raise

    def add_text_overlay(self, video_path: Path, text: str, output_path: Path,
                         position: str = "bottom", start_time: float = 0,
                         duration: float = 5) -> Path:
        """Add text overlay to video"""

        output_path = Path(output_path)

        # Position mapping
        positions = {
            "top": "x=(w-text_w)/2:y=50",
            "middle": "x=(w-text_w)/2:y=(h-text_h)/2",
            "bottom": "x=(w-text_w)/2:y=h-text_h-100"
        }

        pos = positions.get(position, positions["bottom"])

        # Escape special characters in text
        text_escaped = text.replace("'", "\\'").replace(":", "\\:")

        # Create text overlay filter
        filter_str = (
            f"drawtext=text='{text_escaped}':"
            f"fontcolor=white:"
            f"fontsize=36:"
            f"box=1:boxcolor=black@0.7:boxborderw=10:"
            f"{pos}:"
            f"enable='between(t,{start_time},{start_time+duration})'"
        )

        cmd = [
            'ffmpeg',
            '-y',
            '-i', str(video_path),
            '-vf', filter_str,
            '-c:a', 'copy',  # Copy audio
            '-c:v', self.config['video']['codec'],
            str(output_path)
        ]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg error: {e.stderr}")
            raise

    def compile_video(self, scenes: List[Path], audio_path: Path, script: Dict[str, Any],
                      output_path: Path) -> Path:
        """
        Compile complete video from all components

        Args:
            scenes: List of image paths for visual scenes
            audio_path: Path to narration audio
            script: Script dictionary with timing and text
            output_path: Where to save final video

        Returns:
            Path to compiled video
        """

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        temp_dir = output_path.parent / "temp"
        temp_dir.mkdir(exist_ok=True)

        print("Step 1/3: Creating video sequence from scenes...")
        # Create video from scene images
        video_no_audio = temp_dir / "video_no_audio.mp4"
        self.create_scene_sequence(scenes, script['timing'], video_no_audio)

        print("Step 2/3: Adding audio narration...")
        # Add audio
        video_with_audio = temp_dir / "video_with_audio.mp4"
        self.add_audio(video_no_audio, audio_path, video_with_audio)

        print("Step 3/3: Adding text overlays...")
        # Add definition text overlay at the end
        if self.config['overlays'].get('show_definition', True):
            final_video = output_path
            total_duration = sum(script['timing'].values())
            overlay_start = total_duration - 3  # Show in last 3 seconds

            self.add_text_overlay(
                video_with_audio,
                script.get('on_screen_text', ''),
                final_video,
                position=self.config['overlays'].get('definition_position', 'bottom'),
                start_time=max(0, overlay_start),
                duration=3
            )
        else:
            # No overlay, just rename
            import shutil
            shutil.move(video_with_audio, output_path)

        # Clean up temp files
        if self.config['performance'].get('cleanup_temp', True):
            import shutil
            shutil.rmtree(temp_dir)

        print(f"✓ Video compiled: {output_path}")
        return output_path

    def get_video_info(self, video_path: Path) -> Dict[str, Any]:
        """Get video metadata using ffprobe"""

        cmd = [
            'ffprobe',
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            '-show_streams',
            str(video_path)
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"ffprobe error: {e.stderr}")
            return {}


if __name__ == "__main__":
    # Test video compilation
    import yaml

    # Load settings
    settings_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    with open(settings_path) as f:
        config = yaml.safe_load(f)

    # Test with dummy files (would need actual files to work)
    print("Video Compiler Test")
    print("Note: This requires actual scene images and audio files to run")
    print("\nConfiguration loaded:")
    print(f"  Resolution: {config['video']['resolution']['width']}x{config['video']['resolution']['height']}")
    print(f"  FPS: {config['video']['fps']}")
    print(f"  Format: {config['video']['format']}")

"""
Audio Generator
Generates voiceover narration using Text-to-Speech
"""

from pathlib import Path
from typing import Dict, Any, Optional
import hashlib
import os


class AudioGenerator:
    """Generates audio narration for video scripts"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.tts_provider = config['audio']['tts_provider']
        self.voice = config['audio']['voice']
        self.cache_enabled = config['performance'].get('cache_tts', True)
        self.cache_dir = Path(config['paths']['output']) / "audio" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Initialize TTS client
        if self.tts_provider == "openai":
            try:
                from openai import OpenAI
                api_key = os.getenv(config['api']['openai_key_env'])
                if not api_key:
                    raise ValueError(f"OpenAI API key not found in environment variable: {config['api']['openai_key_env']}")
                self.client = OpenAI(api_key=api_key)
            except ImportError:
                raise ImportError("OpenAI package not installed. Run: pip install openai")
        elif self.tts_provider == "gtts":
            try:
                from gtts import gTTS
                self.gtts = gTTS
            except ImportError:
                raise ImportError("gTTS package not installed. Run: pip install gtts")
        else:
            raise ValueError(f"Unsupported TTS provider: {self.tts_provider}")

    def _get_cache_key(self, text: str) -> str:
        """Generate cache key from text and settings"""
        cache_string = f"{text}|{self.tts_provider}|{self.voice}"
        return hashlib.md5(cache_string.encode()).hexdigest()

    def _get_cached_audio(self, text: str) -> Optional[Path]:
        """Check if audio for this text is already cached"""
        if not self.cache_enabled:
            return None

        cache_key = self._get_cache_key(text)
        cache_file = self.cache_dir / f"{cache_key}.mp3"

        if cache_file.exists():
            return cache_file

        return None

    def _save_to_cache(self, text: str, audio_path: Path) -> None:
        """Save generated audio to cache"""
        if not self.cache_enabled:
            return

        cache_key = self._get_cache_key(text)
        cache_file = self.cache_dir / f"{cache_key}.mp3"

        # Copy audio to cache
        import shutil
        shutil.copy(audio_path, cache_file)

    def generate_openai_tts(self, text: str, output_path: Path) -> Path:
        """Generate audio using OpenAI TTS"""
        from openai import OpenAI

        response = self.client.audio.speech.create(
            model="tts-1",  # or "tts-1-hd" for higher quality
            voice=self.voice,
            input=text,
            speed=self.config['audio'].get('speech_rate', 1.0)
        )

        # Save audio file
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'wb') as f:
            for chunk in response.iter_bytes():
                f.write(chunk)

        return output_path

    def generate_gtts(self, text: str, output_path: Path) -> Path:
        """Generate audio using Google TTS (free, lower quality)"""
        tts = self.gtts(text=text, lang='en', slow=False)
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        tts.save(str(output_path))
        return output_path

    def generate_narration(self, script: Dict[str, Any], output_dir: Path) -> Dict[str, Path]:
        """
        Generate narration audio for each script section

        Args:
            script: Script dictionary with sections
            output_dir: Directory to save audio files

        Returns:
            Dictionary mapping section names to audio file paths
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        audio_files = {}
        term_id = script['term'].lower().replace(' ', '_')

        # Combine all sections into one narration
        full_text = " ".join([
            script['sections']['hook'],
            script['sections']['definition'],
            script['sections']['example'],
            script['sections']['application'],
            script['sections'].get('cta', '')
        ])

        # Check cache first
        cached_path = self._get_cached_audio(full_text)
        if cached_path:
            # Copy from cache to output
            import shutil
            output_path = output_dir / f"{term_id}_narration.mp3"
            shutil.copy(cached_path, output_path)
            audio_files['full'] = output_path
            return audio_files

        # Generate new audio
        output_path = output_dir / f"{term_id}_narration.mp3"

        if self.tts_provider == "openai":
            self.generate_openai_tts(full_text, output_path)
        elif self.tts_provider == "gtts":
            self.generate_gtts(full_text, output_path)

        # Save to cache
        self._save_to_cache(full_text, output_path)

        audio_files['full'] = output_path

        # Optionally generate section-by-section audio
        if script.get('generate_sections', False):
            for section_name, text in script['sections'].items():
                if not text:
                    continue

                section_output = output_dir / f"{term_id}_{section_name}.mp3"

                if self.tts_provider == "openai":
                    self.generate_openai_tts(text, section_output)
                elif self.tts_provider == "gtts":
                    self.generate_gtts(text, section_output)

                audio_files[section_name] = section_output

        return audio_files

    def get_audio_duration(self, audio_path: Path) -> float:
        """Get duration of audio file in seconds"""
        try:
            from pydub import AudioSegment
            audio = AudioSegment.from_file(audio_path)
            return len(audio) / 1000.0  # Convert ms to seconds
        except ImportError:
            # Fallback: estimate based on text length if pydub not available
            # Rough estimate: ~150 words per minute
            return 0.0

    def add_background_music(self, narration_path: Path, output_path: Path,
                            music_volume: float = 0.15) -> Path:
        """Add background music to narration (optional)"""
        if not self.config['audio'].get('background_music', False):
            return narration_path

        try:
            from pydub import AudioSegment

            # Load narration
            narration = AudioSegment.from_file(narration_path)

            # Load background music
            music_dir = Path(self.config['paths']['music'])
            music_files = list(music_dir.glob('*.mp3'))

            if not music_files:
                print("Warning: No background music files found")
                return narration_path

            music = AudioSegment.from_file(music_files[0])

            # Loop music to match narration length if needed
            if len(music) < len(narration):
                music = music * (len(narration) // len(music) + 1)

            # Trim music to narration length
            music = music[:len(narration)]

            # Reduce music volume
            music = music - (20 + int((1 - music_volume) * 30))  # Ducking

            # Mix narration with music
            mixed = narration.overlay(music)

            # Export
            output_path = Path(output_path)
            mixed.export(output_path, format="mp3")

            return output_path

        except ImportError:
            print("Warning: pydub not available, skipping background music")
            return narration_path


if __name__ == "__main__":
    # Test audio generation
    import yaml
    import json
    from script_generator import ScriptGenerator, load_term_config

    # Load settings
    settings_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    with open(settings_path) as f:
        config = yaml.safe_load(f)

    # Load a test term
    config_dir = Path(__file__).parent.parent / "config"
    term_data = load_term_config("computing_fundamentals", "idempotency", config_dir)

    # Generate script
    script_gen = ScriptGenerator(config)
    script = script_gen.generate(term_data)

    # Generate audio
    print("Generating audio narration...")
    audio_gen = AudioGenerator(config)

    output_dir = Path(__file__).parent.parent.parent / "output" / "audio"

    try:
        audio_files = audio_gen.generate_narration(script, output_dir)
        print(f"\n✓ Generated audio:")
        for section, path in audio_files.items():
            duration = audio_gen.get_audio_duration(path)
            print(f"  - {section}: {path} ({duration:.1f}s)")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nNote: Make sure to set OPENAI_API_KEY environment variable if using OpenAI TTS")
        print("Or change tts_provider to 'gtts' in settings.yaml for free alternative")

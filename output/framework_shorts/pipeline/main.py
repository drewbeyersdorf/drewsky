#!/usr/bin/env python3
"""
Knowledge Shorts Production Pipeline
Main orchestrator for automated educational video generation
"""

import click
import yaml
from pathlib import Path
from typing import List, Optional
import sys
from tqdm import tqdm
import concurrent.futures

# Add generators to path
sys.path.insert(0, str(Path(__file__).parent / "generators"))

from script_generator import ScriptGenerator, load_term_config
from visual_generator import VisualGenerator
from audio_generator import AudioGenerator
from video_compiler import VideoCompiler


class ProductionPipeline:
    """Main production pipeline orchestrator"""

    def __init__(self, config_path: Optional[Path] = None):
        """Initialize pipeline with configuration"""

        if config_path is None:
            config_path = Path(__file__).parent / "config" / "settings.yaml"

        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        self.config_dir = Path(__file__).parent / "config"
        self.output_base = Path(__file__).parent.parent / "output"

        # Initialize generators
        self.script_gen = ScriptGenerator(self.config)
        self.visual_gen = VisualGenerator(self.config)
        self.audio_gen = AudioGenerator(self.config)
        self.video_compiler = VideoCompiler(self.config)

    def generate_single_video(self, category: str, term_id: str,
                             output_dir: Optional[Path] = None) -> Path:
        """
        Generate a complete video for a single term

        Args:
            category: Term category (e.g., 'computing_fundamentals')
            term_id: Term identifier (e.g., 'idempotency')
            output_dir: Optional custom output directory

        Returns:
            Path to generated video file
        """

        print(f"\n{'='*60}")
        print(f"Generating: {term_id}")
        print(f"{'='*60}\n")

        # Load term configuration
        print("→ Loading term configuration...")
        term_data = load_term_config(category, term_id, self.config_dir)

        # Generate script
        print("→ Generating script...")
        script = self.script_gen.generate(term_data)

        if self.config['output'].get('save_script', True):
            script_dir = self.output_base / "scripts"
            self.script_gen.save_script(script, script_dir)
            print(f"  ✓ Script saved to {script_dir}")

        # Generate visuals
        print("→ Generating visual scenes...")
        scenes = self.visual_gen.generate_scenes(term_data, script)
        print(f"  ✓ Generated {len(scenes)} scenes")

        if self.config['output'].get('create_preview', True):
            preview_path = scenes[0].parent / "preview.html"
            self.visual_gen.create_preview_html(scenes, preview_path)
            print(f"  ✓ Preview: {preview_path}")

        # Generate audio
        print("→ Generating audio narration...")
        audio_dir = self.output_base / "audio"
        audio_files = self.audio_gen.generate_narration(script, audio_dir)
        audio_path = audio_files['full']
        print(f"  ✓ Audio: {audio_path}")

        # Compile video
        print("→ Compiling final video...")
        if output_dir is None:
            output_dir = self.output_base / "videos"

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        filename_template = self.config['output']['filename_format']
        filename = filename_template.format(
            category=category,
            term=term_id,
            date=__import__('datetime').datetime.now().strftime('%Y%m%d'),
            id=term_id
        )
        video_path = output_dir / filename

        final_video = self.video_compiler.compile_video(
            scenes,
            audio_path,
            script,
            video_path
        )

        print(f"\n✓ Video complete: {final_video}")
        print(f"\nVideo info:")
        info = self.video_compiler.get_video_info(final_video)
        if info.get('format'):
            duration = float(info['format'].get('duration', 0))
            size_mb = int(info['format'].get('size', 0)) / (1024 * 1024)
            print(f"  Duration: {duration:.1f}s")
            print(f"  Size: {size_mb:.1f} MB")

        return final_video

    def generate_batch(self, category: str, term_ids: Optional[List[str]] = None,
                      parallel: int = 1) -> List[Path]:
        """
        Generate videos for multiple terms

        Args:
            category: Term category
            term_ids: List of specific term IDs, or None for all in category
            parallel: Number of parallel jobs

        Returns:
            List of paths to generated videos
        """

        # Load all terms in category if not specified
        if term_ids is None:
            config_file = self.config_dir / "terms" / f"{category}.json"
            with open(config_file) as f:
                import json
                data = json.load(f)
                term_ids = [term['id'] for term in data['terms']]

        print(f"\nGenerating {len(term_ids)} videos from {category}")
        print(f"Parallel jobs: {parallel}\n")

        videos = []

        if parallel == 1:
            # Sequential processing
            for term_id in tqdm(term_ids, desc="Processing terms"):
                try:
                    video = self.generate_single_video(category, term_id)
                    videos.append(video)
                except Exception as e:
                    print(f"\n✗ Error generating {term_id}: {e}")

        else:
            # Parallel processing
            with concurrent.futures.ThreadPoolExecutor(max_workers=parallel) as executor:
                futures = {
                    executor.submit(self.generate_single_video, category, term_id): term_id
                    for term_id in term_ids
                }

                for future in tqdm(concurrent.futures.as_completed(futures),
                                 total=len(futures), desc="Processing terms"):
                    term_id = futures[future]
                    try:
                        video = future.result()
                        videos.append(video)
                    except Exception as e:
                        print(f"\n✗ Error generating {term_id}: {e}")

        print(f"\n✓ Batch complete: {len(videos)}/{len(term_ids)} videos generated")
        return videos


@click.group()
def cli():
    """Knowledge Shorts Production Pipeline - Automated educational video generation"""
    pass


@cli.command()
@click.option('--term', required=True, help='Term ID to generate')
@click.option('--category', default='computing_fundamentals', help='Term category')
@click.option('--output', type=click.Path(), help='Output directory')
@click.option('--config', type=click.Path(), help='Custom config file')
def generate(term: str, category: str, output: Optional[str], config: Optional[str]):
    """Generate a single video for a term"""

    config_path = Path(config) if config else None
    pipeline = ProductionPipeline(config_path)

    output_dir = Path(output) if output else None
    video_path = pipeline.generate_single_video(category, term, output_dir)

    click.echo(f"\n✓ Success! Video: {video_path}")


@cli.command()
@click.option('--category', required=True, help='Term category')
@click.option('--terms', help='Comma-separated term IDs (or all if omitted)')
@click.option('--output', type=click.Path(), help='Output directory')
@click.option('--parallel', default=1, type=int, help='Number of parallel jobs')
@click.option('--config', type=click.Path(), help='Custom config file')
def batch(category: str, terms: Optional[str], output: Optional[str],
          parallel: int, config: Optional[str]):
    """Generate videos for multiple terms"""

    config_path = Path(config) if config else None
    pipeline = ProductionPipeline(config_path)

    if output:
        pipeline.output_base = Path(output)

    term_ids = terms.split(',') if terms else None
    videos = pipeline.generate_batch(category, term_ids, parallel)

    click.echo(f"\n✓ Generated {len(videos)} videos")
    for video in videos:
        click.echo(f"  - {video}")


@cli.command()
@click.option('--term', required=True, help='Term ID to preview')
@click.option('--category', default='computing_fundamentals', help='Term category')
def preview(term: str, category: str):
    """Generate preview (script and visuals only, no video compilation)"""

    pipeline = ProductionPipeline()

    print(f"Generating preview for: {term}")

    # Load and generate script
    term_data = load_term_config(category, term, pipeline.config_dir)
    script = pipeline.script_gen.generate(term_data)

    # Save script
    script_dir = pipeline.output_base / "scripts"
    script_path = pipeline.script_gen.save_script(script, script_dir)

    # Generate visuals
    scenes = pipeline.visual_gen.generate_scenes(term_data, script)

    # Create preview HTML
    preview_path = scenes[0].parent / "preview.html"
    pipeline.visual_gen.create_preview_html(scenes, preview_path)

    click.echo(f"\n✓ Preview generated:")
    click.echo(f"  Script: {script_path}")
    click.echo(f"  Visuals: {preview_path}")
    click.echo(f"\nOpen {preview_path} in your browser to review")


@cli.command()
def list_terms():
    """List all available terms"""

    pipeline = ProductionPipeline()
    terms_dir = pipeline.config_dir / "terms"

    for category_file in sorted(terms_dir.glob("*.json")):
        import json
        with open(category_file) as f:
            data = json.load(f)

        category = data.get('category', category_file.stem)
        category_display = data.get('category_display', category)

        click.echo(f"\n{category_display} ({category}):")
        for term in data['terms']:
            complexity = term.get('complexity', 'unknown')
            duration = term.get('duration', 0)
            click.echo(f"  - {term['id']:20s} ({complexity:8s}, {duration}s) - {term['name']}")


@cli.command()
def check_dependencies():
    """Check if all required dependencies are installed"""

    click.echo("Checking dependencies...\n")

    deps = {
        'PIL': 'Pillow',
        'yaml': 'PyYAML',
        'jinja2': 'Jinja2',
        'click': 'Click',
        'tqdm': 'tqdm',
    }

    optional_deps = {
        'openai': 'OpenAI (for TTS)',
        'pydub': 'pydub (for audio processing)',
        'moviepy': 'moviepy (for advanced video editing)',
    }

    all_ok = True

    # Check required
    for module, name in deps.items():
        try:
            __import__(module)
            click.echo(f"✓ {name}")
        except ImportError:
            click.echo(f"✗ {name} - REQUIRED")
            all_ok = False

    # Check optional
    click.echo("\nOptional dependencies:")
    for module, name in optional_deps.items():
        try:
            __import__(module)
            click.echo(f"✓ {name}")
        except ImportError:
            click.echo(f"- {name} - optional")

    # Check system dependencies
    click.echo("\nSystem dependencies:")
    import shutil
    for cmd in ['ffmpeg', 'ffprobe']:
        if shutil.which(cmd):
            click.echo(f"✓ {cmd}")
        else:
            click.echo(f"✗ {cmd} - REQUIRED")
            all_ok = False

    if all_ok:
        click.echo("\n✓ All required dependencies installed!")
    else:
        click.echo("\n✗ Some required dependencies missing")
        click.echo("\nInstall with:")
        click.echo("  pip install -r requirements.txt")
        click.echo("  brew install ffmpeg  # macOS")
        click.echo("  sudo apt install ffmpeg  # Linux")


if __name__ == "__main__":
    cli()

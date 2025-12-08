"""
Visual Generator
Creates ASCII art scenes and animations for videos
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from typing import List, Tuple, Dict, Any
import textwrap


class VisualGenerator:
    """Generates ASCII art visuals for educational videos"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.width = config['video']['resolution']['width']
        self.height = config['video']['resolution']['height']
        self.bg_color = config['visual']['colors']['background']
        self.text_color = config['visual']['colors']['text_primary']
        self.accent_color = config['visual']['colors']['accent']

        # Load font
        font_path = Path(config['paths']['fonts']) / config['visual']['font_family']
        self.font_size = config['visual']['font_size']['body']
        try:
            self.font = ImageFont.truetype(str(font_path), self.font_size)
            self.title_font = ImageFont.truetype(str(font_path), config['visual']['font_size']['title'])
            self.caption_font = ImageFont.truetype(str(font_path), config['visual']['font_size']['caption'])
        except:
            # Fallback to default font
            self.font = ImageFont.load_default()
            self.title_font = ImageFont.load_default()
            self.caption_font = ImageFont.load_default()

    def create_frame(self, content: str, title: str = None, accent_text: str = None) -> Image.Image:
        """Create a single frame with ASCII content"""
        img = Image.new('RGB', (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(img)

        y_offset = 100

        # Draw title if provided
        if title:
            title_bbox = draw.textbbox((0, 0), title, font=self.title_font)
            title_width = title_bbox[2] - title_bbox[0]
            title_x = (self.width - title_width) // 2
            draw.text((title_x, y_offset), title, fill=self.accent_color, font=self.title_font)
            y_offset += 150

        # Draw main ASCII content
        lines = content.split('\n')
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=self.font)
            line_width = bbox[2] - bbox[0]
            x = (self.width - line_width) // 2
            draw.text((x, y_offset), line, fill=self.text_color, font=self.font)
            y_offset += self.font_size + 10

        # Draw accent text at bottom if provided
        if accent_text:
            wrapped = textwrap.wrap(accent_text, width=40)
            accent_y = self.height - 200
            for line in wrapped:
                bbox = draw.textbbox((0, 0), line, font=self.caption_font)
                line_width = bbox[2] - bbox[0]
                x = (self.width - line_width) // 2
                draw.text((x, accent_y), line, fill=self.text_color, font=self.caption_font)
                accent_y += 50

        return img

    def create_cow_scene(self, scene_type: str = "neutral", caption: str = None) -> Image.Image:
        """Create a scene with ASCII cow"""

        cows = {
            "neutral": r"""
       (o_o)
       ( | )
       /   \
      """,
            "thinking": r"""
       (?_?)
      ( hmm )
       ( | )
       /   \
      """,
            "teaching": r"""
       (^_^)
       ( | )  -->  [CONCEPT]
       /   \
      """,
            "confused": r"""
       (@_@)
       ( | )  ???
       /   \
      """
        }

        cow = cows.get(scene_type, cows["neutral"])
        return self.create_frame(cow, accent_text=caption)

    def create_comparison_scene(self, left_text: str, right_text: str,
                                 left_label: str = "Before",
                                 right_label: str = "After") -> Image.Image:
        """Create a before/after comparison scene"""

        comparison = f"""
{left_label:^30}   |   {right_label:^30}
{'─' * 30}   |   {'─' * 30}

{left_text:^30}   →   {right_text:^30}
        """

        return self.create_frame(comparison)

    def create_process_scene(self, steps: List[str]) -> Image.Image:
        """Create a step-by-step process visualization"""

        process = "\n\n".join([f"  Step {i+1}: {step}" for i, step in enumerate(steps)])
        arrows = "\n     ↓\n".join([""] * (len(steps) - 1))

        content = ""
        for i, step in enumerate(steps):
            content += f"  {step}\n"
            if i < len(steps) - 1:
                content += "     ↓\n"

        return self.create_frame(content)

    def create_definition_scene(self, term: str, definition: str) -> Image.Image:
        """Create a scene showing term and definition"""

        wrapped_def = textwrap.wrap(definition, width=35)
        definition_text = "\n".join(wrapped_def)

        return self.create_frame(definition_text, title=term, accent_text=f"{term} = {definition}")

    def generate_scenes(self, term_data: Dict[str, Any], script: Dict[str, Any]) -> List[Path]:
        """Generate all visual scenes for a term"""

        output_dir = Path(self.config['paths']['output']) / "visuals" / term_data['id']
        output_dir.mkdir(parents=True, exist_ok=True)

        scenes = []

        # Scene 1: Title card with cow
        title_scene = self.create_cow_scene("teaching", term_data['name'])
        title_path = output_dir / "scene_01_title.png"
        title_scene.save(title_path)
        scenes.append(title_path)

        # Scene 2: Hook/Introduction
        hook_scene = self.create_frame(script['sections']['hook'])
        hook_path = output_dir / "scene_02_hook.png"
        hook_scene.save(hook_path)
        scenes.append(hook_path)

        # Scene 3: Main visual (style depends on term)
        visual_style = term_data.get('visual_style', 'demonstration')

        if visual_style == "before_after":
            main_scene = self.create_comparison_scene(
                "[BEFORE]", "[AFTER]",
                "Before", "After"
            )
        elif visual_style == "comparison":
            main_scene = self.create_comparison_scene(
                "[OPTION A]", "[OPTION B]",
                "Option A", "Option B"
            )
        elif visual_style == "process":
            main_scene = self.create_process_scene([
                "Input", "Process", "Output"
            ])
        else:  # demonstration
            main_scene = self.create_cow_scene("neutral", script['sections']['example'])

        main_path = output_dir / "scene_03_main.png"
        main_scene.save(main_path)
        scenes.append(main_path)

        # Scene 4: Definition card
        def_scene = self.create_definition_scene(
            term_data['name'],
            term_data['definition']
        )
        def_path = output_dir / "scene_04_definition.png"
        def_scene.save(def_path)
        scenes.append(def_path)

        return scenes

    def create_preview_html(self, scenes: List[Path], output_path: Path):
        """Create HTML preview of all scenes"""

        html = """
<!DOCTYPE html>
<html>
<head>
    <title>Scene Preview</title>
    <style>
        body { background: #111; color: #0f0; font-family: monospace; padding: 20px; }
        .scene { margin: 20px 0; text-align: center; }
        img { max-width: 400px; border: 2px solid #0f0; }
        h2 { color: #ff6b35; }
    </style>
</head>
<body>
    <h1>Visual Scene Preview</h1>
"""

        for i, scene in enumerate(scenes):
            html += f"""
    <div class="scene">
        <h2>Scene {i+1}</h2>
        <img src="{scene.name}" alt="Scene {i+1}">
    </div>
"""

        html += """
</body>
</html>
"""

        with open(output_path, 'w') as f:
            f.write(html)


if __name__ == "__main__":
    # Test visual generation
    import yaml
    import json

    # Load settings
    settings_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    with open(settings_path) as f:
        config = yaml.safe_load(f)

    # Load a test term
    config_file = Path(__file__).parent.parent / "config" / "terms" / "computing_fundamentals.json"
    with open(config_file) as f:
        data = json.load(f)
        term_data = data['terms'][1]  # Idempotency

    # Create mock script
    script = {
        'sections': {
            'hook': 'Press a button once, twice, 100 times...',
            'example': 'Like a light switch - always the same result'
        }
    }

    # Generate visuals
    generator = VisualGenerator(config)
    scenes = generator.generate_scenes(term_data, script)

    print(f"✓ Generated {len(scenes)} scenes")
    for scene in scenes:
        print(f"  - {scene}")

    # Create preview
    preview_path = scenes[0].parent / "preview.html"
    generator.create_preview_html(scenes, preview_path)
    print(f"\n✓ Preview: {preview_path}")

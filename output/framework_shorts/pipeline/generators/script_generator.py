"""
Script Generator
Generates structured video scripts from term configurations
"""

import json
from pathlib import Path
from typing import Dict, Any
from jinja2 import Template


class ScriptGenerator:
    """Generates video scripts from term definitions"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def generate(self, term_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a complete script from term data

        Args:
            term_data: Dictionary containing term information

        Returns:
            Dictionary with script sections and timing
        """
        duration = term_data.get('duration', 25)

        # Build script sections
        script = {
            'term': term_data['name'],
            'category': term_data.get('category', 'unknown'),
            'duration': duration,
            'sections': {
                'hook': term_data.get('hook', ''),
                'definition': term_data.get('explanation', ''),
                'example': term_data.get('example', ''),
                'application': term_data.get('why_matters', ''),
                'cta': self.config['branding'].get('end_cta_text', 'Follow for more')
            },
            'on_screen_text': term_data.get('on_screen_text', ''),
            'visuals': term_data.get('ascii_scenes', []),
            'timing': self._calculate_timing(term_data, duration)
        }

        # Validate script
        self._validate_script(script)

        return script

    def _calculate_timing(self, term_data: Dict[str, Any], duration: int) -> Dict[str, float]:
        """Calculate timing for each script section"""

        # Rough proportions for each section
        if duration <= 20:  # Short video
            timing = {
                'hook': 4,
                'definition': 6,
                'example': 6,
                'application': 3,
                'cta': 1
            }
        elif duration <= 25:  # Medium video
            timing = {
                'hook': 5,
                'definition': 7,
                'example': 8,
                'application': 4,
                'cta': 1
            }
        else:  # Long video (30s)
            timing = {
                'hook': 6,
                'definition': 8,
                'example': 10,
                'application': 5,
                'cta': 1
            }

        # Adjust to exactly match target duration
        total = sum(timing.values())
        scale = duration / total
        timing = {k: v * scale for k, v in timing.items()}

        return timing

    def _validate_script(self, script: Dict[str, Any]) -> None:
        """Validate that script has all required elements"""
        required = ['hook', 'definition', 'example', 'application']

        for section in required:
            if not script['sections'].get(section):
                raise ValueError(f"Missing required section: {section}")

        if script['duration'] < 15 or script['duration'] > 30:
            raise ValueError(f"Duration {script['duration']}s outside valid range (15-30s)")

    def generate_markdown(self, script: Dict[str, Any]) -> str:
        """Generate markdown version of script for review"""

        template = """# {{ term }} Script

**Category:** {{ category }}
**Duration:** {{ duration }}s

## Script Sections

### Hook ({{ timing.hook|round(1) }}s)
{{ sections.hook }}

### Definition ({{ timing.definition|round(1) }}s)
{{ sections.definition }}

### Example ({{ timing.example|round(1) }}s)
{{ sections.example }}

### Application ({{ timing.application|round(1) }}s)
{{ sections.application }}

### CTA ({{ timing.cta|round(1) }}s)
{{ sections.cta }}

---

**On-Screen Text:** {{ on_screen_text }}

**Visual Scenes:**
{% for scene in visuals %}
- {{ scene }}
{% endfor %}

**Total Duration:** {{ duration }}s
"""

        t = Template(template)
        return t.render(**script)

    def save_script(self, script: Dict[str, Any], output_dir: Path) -> Path:
        """Save script as both JSON and Markdown"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        term_id = script['term'].lower().replace(' ', '_')

        # Save JSON
        json_path = output_dir / f"{term_id}_script.json"
        with open(json_path, 'w') as f:
            json.dump(script, f, indent=2)

        # Save Markdown
        md_path = output_dir / f"{term_id}_script.md"
        with open(md_path, 'w') as f:
            f.write(self.generate_markdown(script))

        return json_path


def load_term_config(category: str, term_id: str, config_dir: Path) -> Dict[str, Any]:
    """Load a specific term from category config"""
    config_file = config_dir / "terms" / f"{category}.json"

    with open(config_file, 'r') as f:
        data = json.load(f)

    for term in data['terms']:
        if term['id'] == term_id:
            term['category'] = category
            return term

    raise ValueError(f"Term '{term_id}' not found in category '{category}'")


if __name__ == "__main__":
    # Test script generation
    from pathlib import Path
    import yaml

    # Load settings
    settings_path = Path(__file__).parent.parent / "config" / "settings.yaml"
    with open(settings_path) as f:
        config = yaml.safe_load(f)

    # Load a test term
    config_dir = Path(__file__).parent.parent / "config"
    term_data = load_term_config("computing_fundamentals", "idempotency", config_dir)

    # Generate script
    generator = ScriptGenerator(config)
    script = generator.generate(term_data)

    # Save script
    output_dir = Path(__file__).parent.parent.parent / "output" / "scripts"
    script_path = generator.save_script(script, output_dir)

    print(f"✓ Generated script: {script_path}")
    print("\nScript Preview:")
    print(generator.generate_markdown(script))

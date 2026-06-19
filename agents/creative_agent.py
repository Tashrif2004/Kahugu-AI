"""Creative Agent - Image and music generation"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class CreativeAgent:
    """Generates images, music, and creative content."""

    def __init__(self):
        self.name = "Creative Agent"
        self.generated_content = []
        logger.info(f"Initializing {self.name}")

    def process(self, command: str) -> Dict[str, Any]:
        """Process creative command."""
        return {
            'agent': self.name,
            'command': command,
            'status': 'processed',
            'timestamp': datetime.now().isoformat()
        }

    def generate_image(self, prompt: str, style: Optional[str] = None) -> Dict[str, Any]:
        """Generate an image from text prompt."""
        content = {
            'id': len(self.generated_content),
            'type': 'image',
            'prompt': prompt,
            'style': style,
            'status': 'generating',
            'created_at': datetime.now().isoformat()
        }
        self.generated_content.append(content)
        logger.info(f"Image generation started: {prompt}")
        print(f"🎨 Generating image: '{prompt}'...")
        return content

    def generate_music(self, genre: str, mood: Optional[str] = None, duration: int = 60) -> Dict[str, Any]:
        """Generate music."""
        content = {
            'id': len(self.generated_content),
            'type': 'music',
            'genre': genre,
            'mood': mood,
            'duration': duration,
            'status': 'generating',
            'created_at': datetime.now().isoformat()
        }
        self.generated_content.append(content)
        logger.info(f"Music generation started: {genre} - {mood}")
        print(f"🎵 Generating {genre} music ({mood} mood, {duration}s)...")
        return content

    def generate_text(self, prompt: str, style: Optional[str] = None) -> Dict[str, Any]:
        """Generate creative text."""
        content = {
            'id': len(self.generated_content),
            'type': 'text',
            'prompt': prompt,
            'style': style,
            'created_at': datetime.now().isoformat()
        }
        self.generated_content.append(content)
        logger.info(f"Text generation started: {prompt}")
        return content

    def get_generated_content(self, content_type: Optional[str] = None, limit: int = 10) -> list:
        """Get generated content history."""
        if content_type:
            return [c for c in self.generated_content if c['type'] == content_type][-limit:]
        return self.generated_content[-limit:]

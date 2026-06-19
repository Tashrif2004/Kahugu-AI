"""Updated Creative Agent with Image Generation Integration"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
from models.image_gen import ImageGenerator

logger = logging.getLogger(__name__)


class CreativeAgent:
    """Generates images, music, and creative content."""

    def __init__(self):
        self.name = "Creative Agent"
        self.generated_content = []
        self.image_gen = ImageGenerator()
        logger.info(f"Initializing {self.name}")

    def process(self, command: str) -> Dict[str, Any]:
        """Process creative command."""
        return {
            'agent': self.name,
            'command': command,
            'status': 'processed',
            'timestamp': datetime.now().isoformat()
        }

    def generate_image(self, prompt: str, style: Optional[str] = None, 
                      num_steps: int = 50, guidance: float = 7.5) -> Dict[str, Any]:
        """Generate an image from text prompt using Stable Diffusion."""
        try:
            logger.info(f"Image generation requested: {prompt}")
            result = self.image_gen.generate(
                prompt=prompt,
                style=style,
                num_inference_steps=num_steps,
                guidance_scale=guidance
            )
            
            # Add to content history
            self.generated_content.append(result)
            return result
        except Exception as e:
            logger.error(f"Error generating image: {e}")
            return {'status': 'error', 'error': str(e)}

    def batch_generate_images(self, prompts: list, style: Optional[str] = None) -> list:
        """Generate multiple images."""
        logger.info(f"Batch image generation: {len(prompts)} images")
        results = []
        for prompt in prompts:
            result = self.generate_image(prompt, style=style)
            results.append(result)
        return results

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
            return [c for c in self.generated_content if c.get('type') == content_type][-limit:]
        return self.generated_content[-limit:]

    def get_image_history(self, limit: int = 10) -> list:
        """Get image generation history."""
        return self.image_gen.get_history(limit)
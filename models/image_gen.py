"""Image Generation Module - Stable Diffusion Integration"""

import logging
import os
from typing import Optional, Dict, Any
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class ImageGenerator:
    """Generate images using Stable Diffusion or alternative methods."""

    def __init__(self):
        self.name = "ImageGenerator"
        self.generated_images = []
        self.model_loaded = False
        self.output_dir = Path("./generated_content/images")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initializing {self.name}")
        self._initialize_model()

    def _initialize_model(self):
        """Initialize Stable Diffusion model."""
        try:
            # Try to import diffusers for Stable Diffusion
            from diffusers import StableDiffusionPipeline
            import torch

            logger.info("Loading Stable Diffusion model...")
            print("🎨 Loading Stable Diffusion model (this may take a while on first run)...")

            # Use CPU or GPU based on availability
            device = "cuda" if torch.cuda.is_available() else "cpu"
            logger.info(f"Using device: {device}")

            # Load model (runwayml/stable-diffusion-v1-5 is free and open)
            self.pipe = StableDiffusionPipeline.from_pretrained(
                "runwayml/stable-diffusion-v1-5",
                torch_dtype=torch.float32 if device == "cpu" else torch.float16
            ).to(device)

            self.model_loaded = True
            logger.info("✅ Stable Diffusion model loaded successfully")
            print("✅ Stable Diffusion ready!")

        except ImportError:
            logger.warning("diffusers not installed. Using placeholder mode.")
            print("⚠️ Install diffusers for image generation: pip install diffusers")
            self.model_loaded = False
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            print(f"⚠️ Error loading Stable Diffusion: {e}")
            self.model_loaded = False

    def generate(self, prompt: str, num_inference_steps: int = 50, 
                 guidance_scale: float = 7.5, style: Optional[str] = None) -> Dict[str, Any]:
        """Generate an image from a text prompt."""
        try:
            # Enhance prompt with style
            full_prompt = prompt
            if style:
                full_prompt = f"{prompt}, {style} style, high quality, detailed"
            else:
                full_prompt = f"{prompt}, high quality, detailed"

            logger.info(f"Generating image: {prompt}")
            print(f"🎨 Generating: '{prompt}'...")

            if not self.model_loaded:
                logger.warning("Model not loaded, using placeholder")
                return self._placeholder_image(prompt, style)

            # Generate image
            image = self.pipe(
                full_prompt,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale
            ).images[0]

            # Save image
            filename = f"caugu_{len(self.generated_images)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            filepath = self.output_dir / filename
            image.save(str(filepath))

            result = {
                'id': len(self.generated_images),
                'type': 'image',
                'prompt': prompt,
                'style': style,
                'filepath': str(filepath),
                'filename': filename,
                'status': 'completed',
                'created_at': datetime.now().isoformat()
            }

            self.generated_images.append(result)
            logger.info(f"✅ Image saved: {filepath}")
            print(f"✅ Image saved to: {filepath}")

            return result

        except Exception as e:
            logger.error(f"Error generating image: {e}")
            print(f"❌ Error: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'created_at': datetime.now().isoformat()
            }

    def _placeholder_image(self, prompt: str, style: Optional[str] = None) -> Dict[str, Any]:
        """Return placeholder when model not available."""
        filename = f"caugu_placeholder_{len(self.generated_images)}.png"
        filepath = self.output_dir / filename

        # Create placeholder
        try:
            from PIL import Image, ImageDraw
            img = Image.new('RGB', (512, 512), color='blue')
            draw = ImageDraw.Draw(img)
            draw.text((50, 250), f"Generated: {prompt}", fill='white')
            img.save(str(filepath))
        except:
            pass

        return {
            'id': len(self.generated_images),
            'type': 'image',
            'prompt': prompt,
            'style': style,
            'filepath': str(filepath),
            'filename': filename,
            'status': 'placeholder',
            'created_at': datetime.now().isoformat()
        }

    def batch_generate(self, prompts: list, style: Optional[str] = None) -> list:
        """Generate multiple images."""
        results = []
        for prompt in prompts:
            result = self.generate(prompt, style=style)
            results.append(result)
        return results

    def get_history(self, limit: int = 10) -> list:
        """Get image generation history."""
        return self.generated_images[-limit:]

    def get_image_by_id(self, image_id: int) -> Optional[Dict[str, Any]]:
        """Get image by ID."""
        for img in self.generated_images:
            if img.get('id') == image_id:
                return img
        return None
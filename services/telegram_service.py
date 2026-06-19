"""Telegram Service - Notifications and Bot Integration"""

import logging
import asyncio
from typing import Optional, Dict, Any, Callable
from datetime import datetime

logger = logging.getLogger(__name__)


class TelegramService:
    """Handle Telegram notifications and bot interactions."""

    def __init__(self, token: Optional[str] = None, chat_id: Optional[str] = None):
        self.token = token
        self.chat_id = chat_id
        self.bot = None
        self.is_connected = False
        self.message_history = []
        self.handlers = {}
        logger.info("Initializing Telegram Service")
        self._initialize_bot()

    def _initialize_bot(self):
        """Initialize Telegram bot."""
        try:
            if not self.token:
                logger.warning("Telegram token not set in .env")
                print("⚠️ TELEGRAM_TOKEN not configured in .env")
                print("📚 Get a token from @BotFather: https://t.me/BotFather")
                return False

            try:
                from telegram.ext import Application
                self.Application = Application
                self.is_connected = True
                logger.info("✅ Telegram bot initialized")
                print("✅ Telegram bot ready!")
                return True
            except ImportError:
                logger.warning("python-telegram-bot not installed")
                print("⚠️ Install telegram bot: pip install python-telegram-bot")
                return False

        except Exception as e:
            logger.error(f"Error initializing Telegram: {e}")
            return False

    async def send_message(self, message: str, parse_mode: str = "HTML") -> bool:
        """Send a message via Telegram."""
        try:
            if not self.token or not self.chat_id:
                logger.warning("Telegram not configured, printing message instead")
                print(f"📱 [Telegram] {message}")
                return False

            import requests
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': parse_mode
            }

            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                logger.info(f"Message sent via Telegram")
                # Store in history
                self.message_history.append({
                    'type': 'sent',
                    'message': message,
                    'timestamp': datetime.now().isoformat()
                })
                return True
            else:
                logger.error(f"Telegram API error: {response.text}")
                return False

        except Exception as e:
            logger.error(f"Error sending Telegram message: {e}")
            return False

    async def send_photo(self, photo_path: str, caption: Optional[str] = None) -> bool:
        """Send a photo via Telegram."""
        try:
            if not self.token or not self.chat_id:
                logger.warning("Telegram not configured")
                return False

            import requests
            url = f"https://api.telegram.org/bot{self.token}/sendPhoto"

            with open(photo_path, 'rb') as photo_file:
                payload = {'chat_id': self.chat_id}
                if caption:
                    payload['caption'] = caption

                files = {'photo': photo_file}
                response = requests.post(url, data=payload, files=files)

            if response.status_code == 200:
                logger.info(f"Photo sent via Telegram")
                return True
            else:
                logger.error(f"Telegram API error: {response.text}")
                return False

        except Exception as e:
            logger.error(f"Error sending photo: {e}")
            return False

    async def send_notification(self, title: str, message: str, priority: str = "normal") -> bool:
        """Send a formatted notification."""
        priority_emoji = {
            'high': '🔴',
            'medium': '🟡',
            'normal': '🟢',
            'info': 'ℹ️'
        }

        emoji = priority_emoji.get(priority, '🟢')
        formatted_message = f"{emoji} <b>{title}</b>\n{message}"
        return await self.send_message(formatted_message)

    async def send_workout_notification(self, workout_data: Dict[str, Any]) -> bool:
        """Send a workout completion notification."""
        message = f"""
🏃 <b>Workout Complete!</b>

💪 Type: <b>{workout_data.get('type', 'N/A')}</b>
⏱️ Duration: <b>{workout_data.get('duration')} min</b>
🔥 Calories: <b>{workout_data.get('calories')} kcal</b>
📍 Location: <b>{workout_data.get('location', 'Unknown')}</b>

🎯 Great job staying active!
        """
        return await self.send_notification("Workout Logged", message, priority="high")

    async def send_achievement_notification(self, achievement: str, stats: Dict[str, Any]) -> bool:
        """Send an achievement notification."""
        message = f"""
🏆 <b>Achievement Unlocked!</b>

✨ {achievement}

Stats:
• Total Workouts: <b>{stats.get('total_workouts', 0)}</b>
• Total Calories: <b>{stats.get('total_calories', 0)} kcal</b>
• Streak Days: <b>{stats.get('streak_days', 0)}</b>
        """
        return await self.send_notification("Achievement", message, priority="high")

    async def send_image(self, image_path: str, prompt: str) -> bool:
        """Send generated image with description."""
        caption = f"🎨 Generated Image\n\nPrompt: {prompt}"
        return await self.send_photo(image_path, caption)

    def send_message_sync(self, message: str) -> bool:
        """Send message synchronously (blocking)."""
        try:
            import requests
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, json=payload)
            return response.status_code == 200
        except:
            return False

    def get_message_history(self, limit: int = 10) -> list:
        """Get message history."""
        return self.message_history[-limit:]

    def register_handler(self, command: str, handler: Callable):
        """Register a command handler."""
        self.handlers[command] = handler
        logger.info(f"Handler registered for: {command}")

    def is_configured(self) -> bool:
        """Check if Telegram is properly configured."""
        return bool(self.token and self.chat_id)
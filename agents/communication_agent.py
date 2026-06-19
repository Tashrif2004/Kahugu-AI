"""Updated Communication Agent with Telegram Integration"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
import asyncio
from services.telegram_service import TelegramService
from utils.config import Config

logger = logging.getLogger(__name__)


class CommunicationAgent:
    """Handles all communication: notifications, alerts, messages."""

    def __init__(self):
        self.name = "Communication Agent"
        self.notification_history = []
        self.telegram = TelegramService(
            token=Config.TELEGRAM_TOKEN,
            chat_id=Config.TELEGRAM_CHAT_ID
        )
        logger.info(f"Initializing {self.name}")

    def process(self, command: str) -> Dict[str, Any]:
        """Process communication command."""
        return {
            'agent': self.name,
            'command': command,
            'status': 'processed',
            'timestamp': datetime.now().isoformat()
        }

    def notify(self, message: str, priority: str = 'normal', recipient: Optional[str] = None) -> bool:
        """Send a notification."""
        notification = {
            'message': message,
            'priority': priority,
            'recipient': recipient,
            'timestamp': datetime.now().isoformat()
        }
        self.notification_history.append(notification)
        logger.info(f"Notification: {message}")
        print(f"📢 [{priority.upper()}] {message}")
        
        # Send via Telegram if configured
        if self.telegram.is_configured():
            self.telegram.send_message_sync(f"🔔 {message}")
        
        return True

    def alert(self, alert_type: str, data: Dict[str, Any]) -> bool:
        """Send an alert."""
        logger.info(f"Alert: {alert_type} - {data}")
        print(f"🚨 ALERT [{alert_type}]: {data}")
        
        # Send via Telegram if configured
        if self.telegram.is_configured():
            message = f"🚨 <b>ALERT: {alert_type}</b>\n{str(data)}"
            self.telegram.send_message_sync(message)
        
        return True

    def send_approval_request(self, request_type: str, data: Dict[str, Any]) -> bool:
        """Send approval request notification."""
        message = f"""🔔 <b>APPROVAL REQUEST</b>

Type: <b>{request_type}</b>
Details: {str(data)[:200]}

Please approve or reject."""
        
        if self.telegram.is_configured():
            self.telegram.send_message_sync(message)
        return True

    def send_workout_notification(self, workout_data: Dict[str, Any]) -> bool:
        """Send a workout completion notification."""
        message = f"""🏃 <b>Workout Complete!</b>

💪 Type: <b>{workout_data.get('type', 'N/A')}</b>
⏱️ Duration: <b>{workout_data.get('duration')} min</b>
🔥 Calories: <b>{workout_data.get('calories')} kcal</b>
📍 Location: <b>{workout_data.get('location', 'Unknown')}</b>

🎯 Great job staying active!"""
        
        if self.telegram.is_configured():
            self.telegram.send_message_sync(message)
        return True

    def send_achievement_notification(self, achievement: str, stats: Dict[str, Any]) -> bool:
        """Send an achievement notification."""
        message = f"""🏆 <b>Achievement Unlocked!</b>

✨ {achievement}

Stats:
• Total Workouts: <b>{stats.get('total_workouts', 0)}</b>
• Total Calories: <b>{stats.get('total_calories', 0)} kcal</b>
• Streak Days: <b>{stats.get('streak_days', 0)}</b>"""
        
        if self.telegram.is_configured():
            self.telegram.send_message_sync(message)
        return True

    def send_product_notification(self, product_data: Dict[str, Any]) -> bool:
        """Send product/affiliate notification."""
        message = f"""💰 <b>New Product Found!</b>

📦 Product: <b>{product_data.get('name')}</b>
💵 Price: <b>${product_data.get('price')}</b>
⭐ Rating: <b>{product_data.get('rating')}</b>
📊 Reviews: <b>{product_data.get('reviews_count')}</b>

🔗 Link: {product_data.get('affiliate_link', 'N/A')}"""
        
        if self.telegram.is_configured():
            self.telegram.send_message_sync(message)
        return True

    def send_image_notification(self, image_path: str, caption: str) -> bool:
        """Send image notification via Telegram."""
        if self.telegram.is_configured():
            try:
                self.telegram.send_message_sync(f"🎨 {caption}\n📸 Image: {image_path}")
            except:
                pass
        return True

    def get_notifications(self, limit: int = 10) -> list:
        """Get recent notifications."""
        return self.notification_history[-limit:]

    def get_telegram_status(self) -> Dict[str, Any]:
        """Get Telegram configuration status."""
        return {
            'configured': self.telegram.is_configured(),
            'connected': self.telegram.is_connected,
            'token_set': bool(Config.TELEGRAM_TOKEN),
            'chat_id_set': bool(Config.TELEGRAM_CHAT_ID),
            'message_count': len(self.telegram.message_history)
        }
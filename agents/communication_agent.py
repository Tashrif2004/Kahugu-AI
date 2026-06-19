"""Communication Agent - Handles notifications and alerts"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class CommunicationAgent:
    """Handles all communication: notifications, alerts, messages."""

    def __init__(self):
        self.name = "Communication Agent"
        self.notification_history = []
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
        logger.info(f"Notification sent: {message}")
        print(f"📢 [{priority.upper()}] {message}")
        return True

    def alert(self, alert_type: str, data: Dict[str, Any]) -> bool:
        """Send an alert."""
        logger.info(f"Alert: {alert_type} - {data}")
        print(f"🚨 ALERT [{alert_type}]: {data}")
        return True

    def get_notifications(self, limit: int = 10) -> list:
        """Get recent notifications."""
        return self.notification_history[-limit:]

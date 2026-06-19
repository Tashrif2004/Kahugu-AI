"""Social Media Agent - Handles social media posting with approval"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class SocialMediaAgent:
    """Handles social media posting with approval workflow."""

    def __init__(self):
        self.name = "Social Media Agent"
        self.post_history = []
        self.platforms = ['twitter', 'instagram', 'facebook', 'tiktok']
        logger.info(f"Initializing {self.name}")

    def process(self, command: str) -> Dict[str, Any]:
        """Process social media command."""
        return {
            'agent': self.name,
            'command': command,
            'status': 'processed',
            'timestamp': datetime.now().isoformat()
        }

    def create_post(self, content: str, platform: str, image: Optional[str] = None) -> Dict[str, Any]:
        """Create a social media post (with approval)."""
        post = {
            'id': len(self.post_history),
            'content': content,
            'platform': platform,
            'image': image,
            'status': 'pending_approval',
            'created_at': datetime.now().isoformat()
        }
        self.post_history.append(post)
        logger.info(f"Post created: {post['id']} on {platform}")
        return post

    def approve_post(self, post_id: int) -> bool:
        """Approve a pending post."""
        if post_id < len(self.post_history):
            post = self.post_history[post_id]
            post['status'] = 'approved'
            post['approved_at'] = datetime.now().isoformat()
            logger.info(f"Post approved: {post_id}")
            print(f"✅ Post #{post_id} approved on {post['platform']}")
            return True
        return False

    def reject_post(self, post_id: int) -> bool:
        """Reject a pending post."""
        if post_id < len(self.post_history):
            post = self.post_history[post_id]
            post['status'] = 'rejected'
            post['rejected_at'] = datetime.now().isoformat()
            logger.info(f"Post rejected: {post_id}")
            print(f"❌ Post #{post_id} rejected")
            return True
        return False

    def get_pending_posts(self) -> list:
        """Get all pending approval posts."""
        return [p for p in self.post_history if p['status'] == 'pending_approval']

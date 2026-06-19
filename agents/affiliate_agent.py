"""Affiliate Marketing Agent - Product curation and Pinterest automation"""

import logging
from typing import Dict, Any, Optional, List
from datetime import datetime
from services.product_affiliate_service import ProductAffiliateManager

logger = logging.getLogger(__name__)


class AffiliateAgent:
    """Manages affiliate products, content creation, and Pinterest automation."""

    def __init__(self):
        self.name = "Affiliate Agent"
        self.manager = ProductAffiliateManager()
        logger.info(f"Initializing {self.name}")

    def process(self, command: str) -> Dict[str, Any]:
        """Process affiliate command."""
        return {
            'agent': self.name,
            'command': command,
            'status': 'processed',
            'timestamp': datetime.now().isoformat()
        }

    def add_product(self, product_name: str, category: str, price: float,
                   source: str, affiliate_link: str, description: str = "",
                   rating: float = 0.0, reviews_count: int = 0) -> Dict[str, Any]:
        """Add a fitness/health product."""
        return self.manager.add_product(
            product_name, category, price, source, affiliate_link,
            description, rating, reviews_count
        )

    def curate_best_products(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Curate best fitness products."""
        return self.manager.curate_best_products(category)

    def request_pin_approval(self, product: Dict[str, Any],
                            image_url: str) -> Dict[str, Any]:
        """Request approval for Pinterest pin."""
        pin_description = self.manager.generate_pin_description(product)
        return self.manager.request_pin_creation_approval(product, pin_description, image_url)

    def approve_pin(self, approval_id: int) -> bool:
        """Approve a Pinterest pin."""
        return self.manager.approve_pin(approval_id)

    def reject_pin(self, approval_id: int, reason: str = "") -> bool:
        """Reject a Pinterest pin."""
        return self.manager.reject_pin(approval_id, reason)

    def create_pin(self, product: Dict[str, Any], image_path: str) -> Dict[str, Any]:
        """Create a Pinterest pin."""
        pin_title = f"{product['name']} - Best {product['category']}"
        pin_description = self.manager.generate_pin_description(product)
        return self.manager.create_pinterest_pin(product, image_path, pin_title, pin_description)

    def monitor_digstore24(self, keywords: List[str]) -> Dict[str, Any]:
        """Monitor Digstore24 for new products."""
        return self.manager.monitor_platform('digstore24', keywords)

    def monitor_amazon(self, keywords: List[str]) -> Dict[str, Any]:
        """Monitor Amazon for fitness products."""
        return self.manager.monitor_platform('amazon', keywords)

    def monitor_youtube(self, keywords: List[str]) -> Dict[str, Any]:
        """Monitor YouTube for fitness content."""
        return self.manager.monitor_platform('youtube', keywords)

    def check_status(self) -> Dict[str, Any]:
        """Check platform monitoring status."""
        return self.manager.check_platform_status()

    def create_content_calendar(self, days: int = 7) -> List[Dict[str, Any]]:
        """Create content calendar."""
        return self.manager.create_content_calendar(days)

    def get_analytics(self) -> Dict[str, Any]:
        """Get affiliate performance analytics."""
        return self.manager.get_performance_analytics()

    def get_pending_approvals(self) -> List[Dict[str, Any]]:
        """Get pending pin approvals."""
        return [a for a in self.manager.approval_queue if a['status'] == 'pending_approval']
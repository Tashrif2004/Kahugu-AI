"""Product Affiliate Service - Manage fitness products and affiliate links"""

import logging
import json
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class ProductAffiliateManager:
    """Manage fitness/health products and create affiliate content."""

    def __init__(self):
        self.name = "ProductAffiliateManager"
        self.products = []
        self.curated_products = []
        self.pinterest_pins = []
        self.approval_queue = []
        self.monitored_platforms = {
            'digstore24': [],
            'amazon': [],
            'youtube': []
        }
        self.data_file = Path("./data/affiliate_products.json")
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initializing {self.name}")
        self._load_data()

    def add_product(self, product_name: str, category: str, price: float,
                   source: str, affiliate_link: str, description: str = "",
                   rating: float = 0.0, reviews_count: int = 0) -> Dict[str, Any]:
        """Add a fitness/health product."""
        product = {
            'id': len(self.products),
            'name': product_name,
            'category': category,  # fitness equipment, supplements, etc.
            'price': price,
            'source': source,  # digstore24, amazon, youtube affiliate
            'affiliate_link': affiliate_link,
            'description': description,
            'rating': rating,
            'reviews_count': reviews_count,
            'added_at': datetime.now().isoformat(),
            'performance': {
                'clicks': 0,
                'conversions': 0,
                'revenue': 0.0
            }
        }
        self.products.append(product)
        self._save_data()
        logger.info(f"Product added: {product_name}")
        return product

    def curate_best_products(self, category: Optional[str] = None, 
                            min_rating: float = 4.0) -> List[Dict[str, Any]]:
        """Curate best products based on rating and performance."""
        # Filter by category if specified
        filtered = self.products if not category else [
            p for p in self.products if p['category'].lower() == category.lower()
        ]

        # Sort by rating and reviews
        curated = sorted(
            [p for p in filtered if p['rating'] >= min_rating],
            key=lambda x: (x['rating'], x['reviews_count']),
            reverse=True
        )[:10]  # Top 10

        self.curated_products = curated
        logger.info(f"Curated {len(curated)} products")
        return curated

    def request_pin_creation_approval(self, product: Dict[str, Any],
                                     pin_description: str,
                                     image_url: str) -> Dict[str, Any]:
        """Request approval for Pinterest pin creation."""
        approval_request = {
            'id': len(self.approval_queue),
            'product': product,
            'pin_description': pin_description,
            'image_url': image_url,
            'status': 'pending_approval',
            'requested_at': datetime.now().isoformat()
        }
        self.approval_queue.append(approval_request)
        logger.info(f"Pin approval requested for: {product['name']}")
        print(f"\n📌 PINTEREST PIN APPROVAL REQUEST #{approval_request['id']}")
        print(f"Product: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"Description: {pin_description[:100]}...")
        print(f"Link: {product['affiliate_link']}")
        return approval_request

    def approve_pin(self, approval_id: int) -> bool:
        """Approve a Pinterest pin for creation."""
        if approval_id < len(self.approval_queue):
            approval = self.approval_queue[approval_id]
            approval['status'] = 'approved'
            approval['approved_at'] = datetime.now().isoformat()
            logger.info(f"Pin approved: {approval['product']['name']}")
            return True
        return False

    def reject_pin(self, approval_id: int, reason: str = "") -> bool:
        """Reject a Pinterest pin request."""
        if approval_id < len(self.approval_queue):
            approval = self.approval_queue[approval_id]
            approval['status'] = 'rejected'
            approval['rejection_reason'] = reason
            approval['rejected_at'] = datetime.now().isoformat()
            logger.info(f"Pin rejected: {approval['product']['name']}")
            return True
        return False

    def create_pinterest_pin(self, product: Dict[str, Any],
                            image_path: str, pin_title: str,
                            pin_description: str) -> Dict[str, Any]:
        """Create a Pinterest pin for a product (after approval)."""
        pin = {
            'id': len(self.pinterest_pins),
            'product_id': product['id'],
            'product_name': product['name'],
            'title': pin_title,
            'description': pin_description,
            'image_path': image_path,
            'affiliate_link': product['affiliate_link'],
            'source': product['source'],
            'created_at': datetime.now().isoformat(),
            'status': 'published',
            'engagement': {
                'saves': 0,
                'clicks': 0,
                'impressions': 0
            }
        }
        self.pinterest_pins.append(pin)
        self._save_data()
        logger.info(f"✅ Pinterest pin created: {pin_title}")
        print(f"✅ Pinterest pin created: {pin_title}")
        return pin

    def generate_pin_description(self, product: Dict[str, Any]) -> str:
        """Generate optimized Pinterest pin description."""
        description = f"""
🏋️ {product['name']} ⭐{product['rating']}

💪 Perfect for fitness & health
✨ {product['description'][:100]}...

💰 Price: ${product['price']}
📊 {product['reviews_count']} verified reviews

🔗 Get started today!
#fitness #health #workout #fitnessgear #{product['category'].replace(' ', '')}
        """
        return description.strip()

    def monitor_platform(self, platform: str, search_keywords: List[str]) -> Dict[str, Any]:
        """Monitor a platform (Digstore24, Amazon, YouTube) for products."""
        logger.info(f"Monitoring {platform} for: {search_keywords}")
        print(f"\n🔍 Monitoring {platform} for: {', '.join(search_keywords)}")

        results = {
            'platform': platform,
            'keywords': search_keywords,
            'products_found': [],
            'monitored_at': datetime.now().isoformat()
        }

        # Placeholder for actual API calls
        if platform == 'digstore24':
            results = self._monitor_digstore24(search_keywords, results)
        elif platform == 'amazon':
            results = self._monitor_amazon(search_keywords, results)
        elif platform == 'youtube':
            results = self._monitor_youtube(search_keywords, results)

        self.monitored_platforms[platform].append(results)
        return results

    def _monitor_digstore24(self, keywords: List[str], results: Dict) -> Dict:
        """Monitor Digstore24 for products."""
        # This would integrate with Digstore24 API
        # Placeholder implementation
        print(f"📊 Digstore24: Found products for {len(keywords)} keywords")
        return results

    def _monitor_amazon(self, keywords: List[str], results: Dict) -> Dict:
        """Monitor Amazon for products."""
        # This would use Amazon Product Advertising API
        print(f"📊 Amazon: Scanning {len(keywords)} categories")
        return results

    def _monitor_youtube(self, keywords: List[str], results: Dict) -> Dict:
        """Monitor YouTube for fitness content."""
        # This would use YouTube API
        print(f"📊 YouTube: Monitoring {len(keywords)} channels")
        return results

    def check_platform_status(self) -> Dict[str, Any]:
        """Check status of all monitored platforms."""
        status = {
            'timestamp': datetime.now().isoformat(),
            'platforms': {}
        }

        for platform in self.monitored_platforms:
            platform_data = self.monitored_platforms[platform]
            status['platforms'][platform] = {
                'monitored': len(platform_data) > 0,
                'last_check': platform_data[-1].get('monitored_at') if platform_data else None,
                'products_count': len([p for pdata in platform_data for p in pdata.get('products_found', [])])
            }

        logger.info(f"Platform status checked")
        return status

    def create_content_calendar(self, days_ahead: int = 7) -> List[Dict[str, Any]]:
        """Create content calendar for Pinterest pins."""
        calendar = []
        from datetime import timedelta
        
        products = self.curate_best_products()[:days_ahead]
        
        for i, product in enumerate(products):
            date = datetime.now() + timedelta(days=i)
            calendar_item = {
                'date': date.strftime('%Y-%m-%d'),
                'product_id': product['id'],
                'product_name': product['name'],
                'pin_title': f"{product['name']} - {product['category']}",
                'pin_description': self.generate_pin_description(product),
                'status': 'scheduled',
                'scheduled_at': datetime.now().isoformat()
            }
            calendar.append(calendar_item)

        logger.info(f"Content calendar created for {len(calendar)} days")
        return calendar

    def get_performance_analytics(self) -> Dict[str, Any]:
        """Get performance analytics for products and pins."""
        total_clicks = sum(p['performance']['clicks'] for p in self.products)
        total_conversions = sum(p['performance']['conversions'] for p in self.products)
        total_revenue = sum(p['performance']['revenue'] for p in self.products)
        total_saves = sum(pin['engagement']['saves'] for pin in self.pinterest_pins)
        total_impressions = sum(pin['engagement']['impressions'] for pin in self.pinterest_pins)

        return {
            'products': {
                'total_products': len(self.products),
                'total_clicks': total_clicks,
                'total_conversions': total_conversions,
                'total_revenue': total_revenue,
                'conversion_rate': (total_conversions / total_clicks * 100) if total_clicks > 0 else 0
            },
            'pinterest': {
                'total_pins': len(self.pinterest_pins),
                'total_saves': total_saves,
                'total_impressions': total_impressions,
                'engagement_rate': (total_saves / total_impressions * 100) if total_impressions > 0 else 0
            },
            'generated_at': datetime.now().isoformat()
        }

    def _save_data(self):
        """Save data to file."""
        try:
            data = {
                'products': self.products,
                'curated_products': self.curated_products,
                'pinterest_pins': self.pinterest_pins,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving data: {e}")

    def _load_data(self):
        """Load data from file."""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.products = data.get('products', [])
                self.curated_products = data.get('curated_products', [])
                self.pinterest_pins = data.get('pinterest_pins', [])
                logger.info("Affiliate data loaded")
        except Exception as e:
            logger.error(f"Error loading data: {e}")
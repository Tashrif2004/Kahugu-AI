import 'package:flutter/material.dart';

class AffiliateScreen extends StatefulWidget {
  const AffiliateScreen({Key? key}) : super(key: key);

  @override
  State<AffiliateScreen> createState() => _AffiliateScreenState();
}

class _AffiliateScreenState extends State<AffiliateScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('💰 Affiliate Products'),
        actions: [
          IconButton(
            icon: const Icon(Icons.analytics),
            onPressed: () {},
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Performance Stats
            Text(
              'Performance',
              style: Theme.of(context).textTheme.titleLarge,
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                Expanded(
                  child: _buildStatCard('$2,500', 'Total Revenue', Colors.green),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildStatCard('45', 'Total Clicks', Colors.blue),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildStatCard('12', 'Conversions', Colors.orange),
                ),
              ],
            ),
            const SizedBox(height: 20),

            // Pending Approvals
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'Pending Approvals',
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                Badge(
                  label: const Text('3'),
                  backgroundColor: Colors.red,
                ),
              ],
            ),
            const SizedBox(height: 12),
            _buildApprovalCard(
              productName: 'Ultimate Fitness Bundle',
              imageUrl: '🏋️',
              price: '\$47.99',
              rating: '4.8',
            ),
            const SizedBox(height: 8),
            _buildApprovalCard(
              productName: 'Yoga Mat Pro',
              imageUrl: '🧘',
              price: '\$29.99',
              rating: '4.5',
            ),
            const SizedBox(height: 20),

            // Top Products
            Text(
              'Top Products',
              style: Theme.of(context).textTheme.titleLarge,
            ),
            const SizedBox(height: 12),
            _buildProductCard(
              name: 'Pro Fitness Equipment',
              source: 'Digstore24',
              price: '\$99.99',
              rating: '4.9',
              clicks: '523',
            ),
            const SizedBox(height: 8),
            _buildProductCard(
              name: 'Health Supplements Kit',
              source: 'Amazon',
              price: '\$59.99',
              rating: '4.7',
              clicks: '412',
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildStatCard(String value, String label, Color color) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          children: [
            Text(
              value,
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: color,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              label,
              style: TextStyle(fontSize: 12, color: Colors.grey[400]),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildApprovalCard({
    required String productName,
    required String imageUrl,
    required String price,
    required String rating,
  }) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Text(imageUrl, style: const TextStyle(fontSize: 32)),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        productName,
                        style: const TextStyle(fontWeight: FontWeight.bold),
                      ),
                      Row(
                        children: [
                          Text('⭐ $rating  ', style: const TextStyle(fontSize: 12)),
                          Text(price, style: const TextStyle(fontSize: 12)),
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: () {},
                    child: const Text('Reject'),
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: ElevatedButton(
                    onPressed: () {},
                    child: const Text('Approve'),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildProductCard({
    required String name,
    required String source,
    required String price,
    required String rating,
    required String clicks,
  }) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              name,
              style: const TextStyle(fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                      decoration: BoxDecoration(
                        color: Colors.blue.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: Text(
                        source,
                        style: const TextStyle(fontSize: 11),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Text('⭐ $rating'),
                  ],
                ),
                Text(price, style: const TextStyle(fontWeight: FontWeight.bold)),
              ],
            ),
            const SizedBox(height: 8),
            Text(
              '$clicks clicks',
              style: TextStyle(fontSize: 12, color: Colors.grey[400]),
            ),
          ],
        ),
      ),
    );
  }
}

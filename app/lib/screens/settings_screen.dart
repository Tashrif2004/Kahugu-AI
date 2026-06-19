import 'package:flutter/material.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({Key? key}) : super(key: key);

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool _notificationsEnabled = true;
  bool _trackingEnabled = true;
  bool _darkMode = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('⚙️ Settings'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Profile Section
            Container(
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  const CircleAvatar(
                    radius: 40,
                    child: Icon(Icons.person, size: 40),
                  ),
                  const SizedBox(height: 12),
                  const Text(
                    'CAUGU User',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Text(
                    'AI Personal Assistant',
                    style: TextStyle(color: Colors.grey[400]),
                  ),
                ],
              ),
            ),
            const Divider(),

            // Notifications
            _buildSettingSection('Notifications'),
            _buildSettingTile(
              title: 'Push Notifications',
              subtitle: 'Receive updates and alerts',
              value: _notificationsEnabled,
              onChanged: (value) {
                setState(() => _notificationsEnabled = value);
              },
            ),
            _buildSettingTile(
              title: 'Telegram Notifications',
              subtitle: 'Send alerts via Telegram',
              onTap: () {},
            ),
            const Divider(),

            // Fitness
            _buildSettingSection('Fitness'),
            _buildSettingTile(
              title: 'Activity Tracking',
              subtitle: 'Track steps and movements',
              value: _trackingEnabled,
              onChanged: (value) {
                setState(() => _trackingEnabled = value);
              },
            ),
            _buildSettingTile(
              title: 'Connected Devices',
              subtitle: 'Apple Watch, Fitbit',
              onTap: () {},
            ),
            const Divider(),

            // Affiliate
            _buildSettingSection('Affiliate'),
            _buildSettingTile(
              title: 'Digstore24',
              subtitle: 'Connect your account',
              onTap: () {},
            ),
            _buildSettingTile(
              title: 'Amazon Associates',
              subtitle: 'Link affiliate account',
              onTap: () {},
            ),
            _buildSettingTile(
              title: 'Pinterest',
              subtitle: 'Authorize pin creation',
              onTap: () {},
            ),
            const Divider(),

            // Display
            _buildSettingSection('Display'),
            _buildSettingTile(
              title: 'Dark Mode',
              subtitle: 'Reduce eye strain',
              value: _darkMode,
              onChanged: (value) {
                setState(() => _darkMode = value);
              },
            ),
            _buildSettingTile(
              title: 'Language',
              subtitle: 'English',
              onTap: () {},
            ),
            const Divider(),

            // About
            _buildSettingSection('About'),
            _buildSettingTile(
              title: 'Version',
              subtitle: '1.0.0',
              onTap: () {},
            ),
            _buildSettingTile(
              title: 'Privacy Policy',
              subtitle: 'View our policies',
              onTap: () {},
            ),
            _buildSettingTile(
              title: 'Terms of Service',
              subtitle: 'Read our terms',
              onTap: () {},
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  Widget _buildSettingSection(String title) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 12, 16, 8),
      child: Align(
        alignment: Alignment.centerLeft,
        child: Text(
          title,
          style: Theme.of(context).textTheme.titleMedium?.copyWith(
                color: Colors.blue,
              ),
        ),
      ),
    );
  }

  Widget _buildSettingTile({
    required String title,
    required String subtitle,
    bool? value,
    VoidCallback? onTap,
    Function(bool)? onChanged,
  }) {
    return ListTile(
      title: Text(title),
      subtitle: Text(subtitle),
      trailing: value != null
          ? Switch(
              value: value,
              onChanged: onChanged,
            )
          : const Icon(Icons.arrow_forward_ios, size: 16),
      onTap: onTap,
    );
  }
}

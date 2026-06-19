"""CAUGU Mobile App - Flutter UI Structure"""

# Install Flutter: https://flutter.dev/docs/get-started/install
# Create project: flutter create caugu_app
# Run: flutter run

App structure will be in lib/ directory:

lib/
├── main.dart                 # App entry point
├── screens/
│   ├── home_screen.dart      # Dashboard
│   ├── fitness_screen.dart   # Fitness tracking
│   ├── affiliate_screen.dart # Affiliate products
│   ├── pinterest_screen.dart # Pinterest pins
│   └── profile_screen.dart   # User profile
├── widgets/
│   ├── workout_card.dart
│   ├── product_card.dart
│   └── pin_card.dart
├── services/
│   ├── api_service.dart
│   ├── storage_service.dart
│   └── notification_service.dart
└── models/
    ├── workout.dart
    ├── product.dart
    └── pin.dart

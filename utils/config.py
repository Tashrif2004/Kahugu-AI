"""Configuration management for CAUGU"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class for CAUGU system."""

    # Core
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///caugu.db')

    # Telegram
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    TELEGRAM_ENABLED = os.getenv('TELEGRAM_ENABLED', 'true').lower() == 'true'

    # AI Models
    LLM_MODEL = os.getenv('LLM_MODEL', 'mistral-7b-instruct')
    IMAGE_MODEL = os.getenv('IMAGE_MODEL', 'stable-diffusion-v1.5')
    VOICE_MODEL = os.getenv('VOICE_MODEL', 'base')

    # Features
    APPROVAL_REQUIRED = os.getenv('APPROVAL_REQUIRED', 'true').lower() == 'true'
    TRACKING_ENABLED = os.getenv('TRACKING_ENABLED', 'true').lower() == 'true'
    LOCATION_TRACKING = os.getenv('LOCATION_TRACKING', 'true').lower() == 'true'
    FITNESS_TRACKING = os.getenv('FITNESS_TRACKING', 'true').lower() == 'true'

    # API Keys (optional)
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
    INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', './logs/caugu.log')

    # Security
    SECURE_MODE = os.getenv('SECURE_MODE', 'true').lower() == 'true'
    ENCRYPT_SENSITIVE_DATA = os.getenv('ENCRYPT_SENSITIVE_DATA', 'true').lower() == 'true'

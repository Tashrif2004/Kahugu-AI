"""Logging configuration for CAUGU"""

import logging
import os
from utils.config import Config


def setup_logging():
    """Setup logging for CAUGU system."""
    os.makedirs('./logs', exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

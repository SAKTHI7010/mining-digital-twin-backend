import logging
import sys
from app.core.config import get_settings

def get_logger(name: str) -> logging.Logger:
    settings = get_settings()
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(settings.LOG_LEVEL)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

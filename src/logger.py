import logging
from logging.config import dictConfig

# Define logging configuration
LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
        },
        "detailed": {
            "format": "[%(asctime)s] %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "detailed",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
}

# Apply logging configuration
dictConfig(LOG_CONFIG)

# Get a logger instance
def get_logger(name: str):
    return logging.getLogger(name)

from loguru import logger
import sys

# Basic structured logging setup
logger.remove()
logger.add(sys.stdout, serialize=True, level="INFO")

__all__ = ["logger"]

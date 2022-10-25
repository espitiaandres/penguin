import logging
import traceback

logger = logging.getLogger("penguin")


def log_errors(e: Exception):
    """
    Logs the errors that arise when the function was called.
    """
    logger.error(traceback.format_exc())
    return

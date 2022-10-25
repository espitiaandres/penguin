import logging
from typing import Any

logger = logging.getLogger("penguin")


def log_return(value: Any):
    """
    Logs the return value of the function that was called.
    """
    logger.info(f"Returned value: {value!r}")
    return

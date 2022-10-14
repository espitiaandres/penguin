import logging
from typing import Any

logger = logging.getLogger("penguin")


def log_return(value: Any):
    logger.info(f"Returned value: {value!r}")
    return

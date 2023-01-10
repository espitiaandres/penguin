# -*- coding: utf-8 -*-

#
# penguin_py - A lightweight, customizable stopwatch  decorator
#
# Andres Espitia
# espitiaandres.com
# espitiaandres123@gmail.com
#
# License: MIT
#

import logging
from typing import Any

logger = logging.getLogger("penguin")


def log_return(value: Any):
    """
    Logs the return value of the function that was called.
    """
    logger.info(f"Returned value: {value!r}")
    return

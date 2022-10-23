import logging
from typing import Any, Tuple

from .colour_map import colour_map

logger = logging.getLogger("penguin")


def log_args(args: Tuple[Any, ...], kwargs: dict, func_name: str, colour_msg: str):
    grey_colour = colour_map["grey"]
    args_list = [repr(arg) for arg in args]
    kwargs_list = [f"{k}={v!r}" for k, v, in kwargs.items()]
    params_list = ", ".join([*args_list, *kwargs_list])
    function_signature = f"{func_name}({params_list})"
    logger.info(f"Running {colour_msg}{function_signature}{grey_colour}")
    return

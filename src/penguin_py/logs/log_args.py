import logging
from typing import Any, Tuple

from ..colours.get_default_colours import get_default_colours

logger = logging.getLogger("penguin")


def log_args(
    args: Tuple[Any, ...],
    kwargs: dict,
    func_name: str,
    foreground_colour: str,
    background_colour: str,
):
    """
    Logs the args and kwargs that a function was called with.
    """
    args_list = [repr(arg) for arg in args]
    kwargs_list = [f"{k}={v!r}" for k, v, in kwargs.items()]
    params_list = ", ".join([*args_list, *kwargs_list])
    function_signature = f"{func_name}({params_list})"

    grey_foreground_colour, black_background_colour = get_default_colours()
    format_start = f"{foreground_colour}{background_colour}"
    format_end = f"{grey_foreground_colour}{black_background_colour}"
    logger.info(f"Running {format_start}{function_signature}{format_end}")
    return

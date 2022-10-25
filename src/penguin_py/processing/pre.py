from typing import Any, Literal, Optional

from ..colours.get_logger_colour import get_logger_colour
from ..logs.log_args import log_args


def penguin_wrapped_pre_timer(
    func: Any,
    args: Any,
    kwargs: Any,
    verbose: Optional[bool] = False,
    show_args: Optional[bool] = False,
    foreground: Optional[
        Literal["red" "yellow", "green", "blue", "magenta", "cyan", "grey"]
    ] = "grey",
    background: Optional[
        Literal[
            "red" "yellow", "green", "blue", "magenta", "cyan", "grey", "black", "white"
        ]
    ] = "black",
):
    """
    Performs pre-processing on the function:
    It runs common functions used, and gets the foreground colour, background colour, and the function name to run in the @penguin and @penguin_async decorators.
    """
    func_name = func.__name__
    foreground_colour = get_logger_colour(foreground, "foreground_colours")
    background_colour = get_logger_colour(background, "background_colours")

    if show_args or verbose:
        log_args(args, kwargs, func_name, foreground_colour, background_colour)

    return foreground_colour, background_colour, func_name

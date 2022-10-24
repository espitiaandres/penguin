import logging
from typing import Any, Optional

from ..colours.get_default_colours import get_default_colours

logger = logging.getLogger("penguin")


def penguin_wrapped_post_timer(
    foreground_colour: str,
    background_colour: str,
    func_name: str,
    time_msg: str,
    value: Any,
    verbose: Optional[bool] = False,
    show_return: Optional[bool] = False,
):
    """
    Runs common functions in the @penguin and @penguin_async decorators.
    """
    grey_foreground_colour, black_background_colour = get_default_colours()
    format_start = f"{foreground_colour}{background_colour}"
    format_end = f"{grey_foreground_colour}{black_background_colour}"
    logger.info(
        f"Finished {format_start}{func_name}{format_end} in {format_start}{time_msg}{format_end}"
    )

    if show_return or verbose:
        logger.info(f"Returned value: {format_start}{value!r}{format_end}")

    return

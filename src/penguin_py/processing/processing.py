import logging
from typing import Any, Literal, Optional

from ..colours.get_default_colours import get_default_colours
from ..colours.get_logger_colour import get_logger_colour
from ..logs.log_args import log_args

logger = logging.getLogger("penguin")


class DataProcessing:
    """
    A DataProcessing object handles the pre-processing and post-processing of the function.
    This entails the getting colours, logs, and formatting the logging output.
    """

    def __init__(
        self,
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
                "red" "yellow",
                "green",
                "blue",
                "magenta",
                "cyan",
                "grey",
                "black",
                "white",
            ]
        ] = "black",
    ):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.verbose = verbose if verbose is not None else False
        self.show_args = show_args if show_args is not None else False
        self.foreground = foreground if foreground is not None else "grey"
        self.background = background if background is not None else "black"
        return

    def pre(self):
        """
        Performs pre-processing on the function:
        It runs common functions used, and gets the foreground colour, background colour, and the function name to run in the @penguin and @penguin_async decorators.
        """
        self.func_name = self.func.__name__
        self.foreground_colour = get_logger_colour(
            self.foreground, "foreground_colours"
        )
        self.background_colour = get_logger_colour(
            self.background, "background_colours"
        )

        if self.show_args or self.verbose:
            log_args(
                self.args,
                self.kwargs,
                self.func_name,
                self.foreground_colour,
                self.background_colour,
            )

        return

    def post(
        self,
        time_msg: str,
        value: Optional[bool] = None,
        verbose: Optional[bool] = False,
        show_return: Optional[bool] = False,
    ):
        """
        Performs post-processing on the function:
        It runs common functions in the @penguin and @penguin_async decorators.
        """
        grey_foreground_colour, black_background_colour = get_default_colours()
        format_start = f"{self.foreground_colour}{self.background_colour}"
        format_end = f"{grey_foreground_colour}{black_background_colour}"
        logger.info(
            f"Finished {format_start}{self.func_name}{format_end} in {format_start}{time_msg}{format_end}"
        )

        if show_return or verbose:
            logger.info(f"Returned value: {format_start}{value!r}{format_end}")

        return

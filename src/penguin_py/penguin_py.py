"""An amazing sample package!"""

__version__ = "0.1"


import logging
import time
from functools import wraps
from typing import Callable, Literal, Optional

from .colours.get_default_colours import get_default_colours
from .colours.get_logger_colour import get_logger_colour
from .get_time_msg import get_time_msg
from .logs.log_args import log_args

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("penguin")


"""
TODO:
- Give user ability to log to a log file.
"""

"""
Instructions to update new version:

- Delete all files in the dist folder.

- Update the version number in the setup.py file.

- Re-create the wheels:
python3 setup.py sdist bdist_wheel

- Re-upload the new files:
twine upload dist/*
"""


def penguin(
    verbose: Optional[bool] = False,
    show_args: Optional[bool] = False,
    show_return: Optional[bool] = False,
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
    ## Penguin: a customizable stopwatch decorator

    Penguin is a lightweight, customizable decorator that helps you determine how long it takes for your functions to run.

    kwargs:
    `verbose`: When `True`, it shows all logs that are described by the other kwargs. When `False`,
    each kwarg would determine if that specific log is shown
        - default: `False`
    `show_args`: When `True`, it shows the function's signature, with the `*args` and `**kwargs` being passed in.
        - default: `False`
    `show_return`: When `True`, it shows the function's return value(s).
        - default: `False`
    `foreground`: When chosen from this list, `["red" "yellow", "green", "blue", "magenta", "cyan", "grey"]`, it colour the logger output **text** the chosen colour.
        - default: `"grey"`
    `background`: When chosen from this list, `["red" "yellow", "green", "blue", "magenta", "cyan", "grey", "black", "white"]`, it colour the logger output **background** the chosen colour.
        - default: `"black"`
    """

    def penguin_decorator(func: Callable):
        """Log the runtime of the decorated function"""

        @wraps(func)
        def penguin_wrapper(*args, **kwargs):
            func_name = func.__name__
            foreground_colour = get_logger_colour(foreground, "foreground_colours")
            background_colour = get_logger_colour(background, "background_colours")
            grey_foreground_colour, black_background_colour = get_default_colours()

            if show_args or verbose:
                log_args(args, kwargs, func_name, foreground_colour, background_colour)

            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            time_msg = get_time_msg(run_time)

            format_start = f"{foreground_colour}{background_colour}"
            format_end = f"{grey_foreground_colour}{black_background_colour}"
            logger.info(
                f"Finished {format_start}{func_name}{format_end} in {format_start}{time_msg}{format_end}"
            )

            if show_return or verbose:
                logger.info(f"Returned value: {format_start}{value!r}{format_end}")

            return value

        return penguin_wrapper

    return penguin_decorator

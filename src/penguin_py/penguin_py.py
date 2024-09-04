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
import time
import traceback
from functools import wraps
from typing import Callable, Literal, Optional

from colorama import just_fix_windows_console

from .processing.get_time_msg import get_time_msg
from .processing.processing import DataProcessing

logging.basicConfig(
    level=logging.NOTSET,
    format="%(asctime)s | %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("penguin")


"""
TODO:
- reddit post

"""

"""
Instructions to update new version:

- Delete all files in the dist folder.

- Update the version number in setup.py, README.md, and README_PYPI.md

- Re-create the wheels:
python3 setup.py sdist bdist_wheel

- Re-upload the new files:
twine upload dist/*

- Push to Github repo
"""

just_fix_windows_console()


def penguin(
    verbose: Optional[bool] = False,
    show_args: Optional[bool] = False,
    show_return: Optional[bool] = False,
    foreground: Optional[
        Literal["red", "yellow", "green", "blue", "magenta", "cyan", "grey"]
    ] = "grey",
    background: Optional[
        Literal[
            "red",
            "yellow",
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
    """
    ## A customizable stopwatch decorator for synchronous functions

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
        def penguin_wrapped(*args, **kwargs):
            data_processing = DataProcessing(
                func,
                args,
                kwargs,
                verbose=verbose,
                show_args=show_args,
                foreground=foreground,
                background=background,
            )
            data_processing.pre()

            try:
                start_time = time.perf_counter()
                value = func(*args, **kwargs)

                end_time = time.perf_counter()
                run_time = end_time - start_time
                time_msg = get_time_msg(run_time)

                data_processing.post(
                    time_msg,
                    value,
                    verbose=verbose,
                    show_return=show_return,
                )
                return value
            except Exception:
                logger.error(traceback.format_exc())

        return penguin_wrapped

    return penguin_decorator


def penguin_async(
    verbose: Optional[bool] = False,
    show_args: Optional[bool] = False,
    show_return: Optional[bool] = False,
    foreground: Optional[
        Literal["red", "yellow", "green", "blue", "magenta", "cyan", "grey"]
    ] = "grey",
    background: Optional[
        Literal[
            "red",
            "yellow",
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
    """
    ## A customizable stopwatch decorator for coroutines (asynchronous functions)

    Penguin is a lightweight, customizable decorator that helps you determine how long it takes for your functions to run.

    kwargs:
    `verbose`: When `True`, it shows all logs that are described by the other kwargs. When `False`,
    each kwarg would determine if that specific log is shown
        - default: `False`
    `show_args`: When `True`, it shows the function's signature, with the `*args` and `**kwargs` being passed in.
        - default: `False`
    `show_return`: When `True`, it shows the function's return value(s).
        - default: `False`
    `foreground`: When chosen from this list, `["red", "yellow", "green", "blue", "magenta", "cyan", "grey"]`, it colour the logger output **text** the chosen colour.
        - default: `"grey"`
    `background`: When chosen from this list, `["red", "yellow", "green", "blue", "magenta", "cyan", "grey", "black", "white"]`, it colour the logger output **background** the chosen colour.
        - default: `"black"`
    """

    def penguin_decorator(func: Callable):
        """Log the runtime of the decorated function"""

        @wraps(func)
        async def penguin_wrapped(*args, **kwargs):
            data_processing = DataProcessing(
                func,
                args,
                kwargs,
                verbose=verbose,
                show_args=show_args,
                foreground=foreground,
                background=background,
            )
            data_processing.pre()

            try:
                start_time = time.perf_counter()
                value = await func(*args, **kwargs)

                end_time = time.perf_counter()
                run_time = end_time - start_time
                time_msg = get_time_msg(run_time)

                data_processing.post(
                    time_msg,
                    value,
                    verbose=verbose,
                    show_return=show_return,
                )
                return value
            except Exception:
                logger.error(traceback.format_exc())

        return penguin_wrapped

    return penguin_decorator

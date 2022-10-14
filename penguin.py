import logging
from functools import wraps
import time
from typing import Callable, Any, Optional

from log_args import log_args

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

"""
TODO:
-
"""


def penguin(
    verbose: Optional[bool] = False,
    show_args: Optional[bool] = False,
    show_return: Optional[bool] = False,
) -> Callable:
    """
    ## Penguin: a customizable stopwatch decorator

    Penguin is lightweight, customizable decorator that helps you determine how long it takes for your functions to run.
    """

    def penguin_decorator(func: Callable):
        """Log the runtime of the decorated function"""

        @wraps(func)
        def penguin_wrapper(*args, **kwargs):
            func_name = func.__name__

            if show_args or verbose:
                log_args(args, kwargs, func_name)

            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time

            if run_time < 0.0001:
                time_msg = f"{(run_time * 1_000_000):.4f} \u03BCs (microseconds)"
            elif run_time < 1:
                time_msg = f"{(run_time * 1000):.4f} ms (miliseconds)"
            elif run_time < 60:
                time_msg = f"{run_time:.4f} s (seconds)"
            else:
                run_time_mins = run_time / 60
                time_msg = f"{run_time_mins:.4f} min (minutes)"

            logger.info(f"Finished {func_name} in {time_msg}.")

            if show_return or verbose:
                logger.info(f"Returned value: {value!r}")

            return value

        return penguin_wrapper

    return penguin_decorator

import logging
from functools import wraps
import time
from typing import Callable, Any

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

"""
TODO:
- docstrings
- rename functions better
- kwarg for when wanting show output
"""


def penguin(verbose: bool = False) -> Callable:
    """
    ## This is a docstring

    with markdon
    """
    def penguin_decorator(func: Callable) -> Any:
        """Log the runtime of the decorated function"""
        @wraps(func)
        def penguin_wrapper(*args, **kwargs):
            func_name = func.__name__

            if verbose:
              args_list = [repr(arg) for arg in args]
              kwargs_list = [f"{k}={v}" for k, v, in kwargs.items()]
              params_list = ", ".join([*args_list, *kwargs_list])
              logger.info(f"Running {func_name}({params_list})")

            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time

            if run_time < 0.0001:
                time_msg = f"{(run_time * 1000):.4f} \u03BCs (microseconds)"
            elif run_time < 1:
                time_msg = f"{(run_time * 1000):.4f} ms (miliseconds)"
            elif run_time < 60:
                time_msg = f"{run_time:.4f} s (seconds)"
            else:
                run_time_mins = run_time / 60
                time_msg = f"{run_time_mins:.4f} min (minutes)"

            logger.info(f"Finished {func_name} in {time_msg}.")

            if verbose:
              logger.info(f"Returned value: {value!r}")

            return value

        return penguin_wrapper

    return penguin_decorator

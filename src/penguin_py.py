"""An amazing sample package!"""

__version__ = "0.1"


import logging
import time
from functools import wraps
from typing import Callable, Optional

from . import get_time_msg, log_args

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("penguin")

"""
TODO:
- change imports -> from penguin_py import penguin
- Update README.md
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
):
    """
    ## Penguin: a customizable stopwatch decorator

    Penguin is lightweight, customizable decorator that helps you determine how long it takes for your functions to run.

    kwargs:
    `verbose`: When `True`, it shows all logs that are described by the other kwargs. When `False`,
    each kwarg would determine if that specific log is shown
    `show_args`: When `True`, it shows the function's signature, with the `*args` and `**kwargs` being passed in.
    `show_return`: When `True`, it shows the function's return value(s).
    """

    def penguin_decorator(func: Callable):
        """Log the runtime of the decorated function"""

        @wraps(func)
        def penguin_wrapper(*args, **kwargs):
            func_name = func.__name__

            if show_args or verbose:
                log_args.log_args(args, kwargs, func_name)

            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            time_msg = get_time_msg.get_time_msg(run_time)
            logger.info(f"Finished {func_name} in {time_msg}.")

            logger.info("adventure of a lifetime!")

            if show_return or verbose:
                logger.info(f"Returned value: {value!r}")

            return value

        return penguin_wrapper

    return penguin_decorator

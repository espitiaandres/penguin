import logging
from typing import Any, Tuple

logger = logging.getLogger("penguin")


def log_args(args: Tuple[Any, ...], kwargs: dict, func_name: str):
    args_list = [repr(arg) for arg in args]
    kwargs_list = [f"{k}={v!r}" for k, v, in kwargs.items()]
    params_list = ", ".join([*args_list, *kwargs_list])
    logger.info(f"Running {func_name}({params_list})")
    return

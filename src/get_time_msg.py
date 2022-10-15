import logging

logger = logging.getLogger("penguin")


def get_time_msg(run_time: float):
    if run_time < 0.0001:
        time_msg = f"{(run_time * 1_000_000):.4f} \u03BCs (microseconds)"
    elif run_time < 1:
        time_msg = f"{(run_time * 1000):.4f} ms (milliseconds)"
    elif run_time < 60:
        time_msg = f"{run_time:.4f} s (seconds)"
    else:
        run_time_mins = run_time / 60
        time_msg = f"{run_time_mins:.4f} min (minutes)"

    return time_msg

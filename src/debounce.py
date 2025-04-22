import time
from threading import Timer
from functools import wraps
from typing import Callable, Any

def debounce(delay: float):
    """
    Simple debounce decorator that delays function execution.

    Args:
        delay (float): Delay time in seconds before executing the function
                      after the last invocation.
    """
    def decorator(func: Callable) -> Callable:
        timer = None

        @wraps(func)
        def wrapped(*args, **kwargs) -> None:
            nonlocal timer
            if timer is not None:
                timer.cancel()

            def execute():
                func(*args, **kwargs)

            timer = Timer(delay, execute)
            timer.start()

        return wrapped

    return decorator
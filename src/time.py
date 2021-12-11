from time import sleep, time
from typing import Any, Callable, Generator

repeat_count = 1
unit_factor = 1000
unit = "ms"


class Timer:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.duration = None

    def __enter__(self) -> None:
        """Start timer."""
        self.start = time()

    def __exit__(self, exc_type, exc_value, traceback) -> None:  # noqa: ANN001
        """End timer and output duration."""
        self.end = time()
        self.duration = self.end - self.start
        print(f"code took {self.duration * unit_factor} {unit}")


def time_func(count: int = repeat_count) -> Callable:
    """Decorator to measure execution time of a function."""
    count = abs(count) or 1

    def decorator(function: Callable) -> Callable:
        """Decorator to measure execution time of a function."""

        def wrapper(*args: Any, **kw: Any) -> Any:
            start = time()
            result = None
            for _ in range(count):
                result = function(*args, **kw)
            end = time()
            duration = (end - start) / count
            print(
                f"{function.__name__} took {duration * unit_factor} {unit} "
                f"(average of {count} runs)"
            )
            return result

        return wrapper

    return decorator


def time_loop(count: int = repeat_count) -> Generator:
    """Generator to measure execution time of a code block in a for loop."""
    count = abs(count) or 1

    start = time()
    for _ in range(count):
        yield None
    end = time()
    duration = (end - start) / count
    print(f"loop took {duration * unit_factor} {unit} (average of {count} runs)")
    return duration


if __name__ == "__main__":

    @time_func(10000)
    def sleep_test() -> None:
        """Dummy test function."""
        sleep(0.01)

    sleep_test()

    for _ in time_loop(10000):
        sleep(0.01)

    with Timer():
        sleep(0.01)

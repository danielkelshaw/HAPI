import functools
from typing import Any, Callable, List


def to_list(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:

    """Force inputs to function to be iterables.

    Parameters
    ----------
    fn : Callable[[Any], Any]
        Function to decorate.

    Returns
    -------
    Callable[[Any], Any]
        Decorated function.
    """

    @functools.wraps(fn)
    def _decorated(*args: Any) -> Any:
        return fn(*[convert_list(x) for x in args])

    return _decorated


def convert_list(x: Any) -> List:

    """Convert int / float to list.

    Parameters
    ----------
    x : Any
        Input to convert.

    Returns
    -------
    x : Iterable
        Converted value.
    """

    if isinstance(x, (int, float)):
        return [x]
    else:
        return x

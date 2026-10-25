"""Friendly checks for the chapter notebooks.

Each check prints one of four results:
  Correct      your answer matches
  Not yet      it runs, but the answer is off (with a hint where there is one)
  Not started  the function still raises NotImplementedError or the value is still None
  Error        your code raised an error (the message says which)
"""
from __future__ import annotations

import numbers

import numpy as np


def _fmt(x):
    if type(x).__name__ == "DataFrame":
        return f"<table with {len(x)} rows>"
    if callable(x) and hasattr(x, "__name__"):
        return x.__name__
    if isinstance(x, bool):
        return str(x)
    if isinstance(x, numbers.Real) and not isinstance(x, numbers.Integral):
        return f"{float(x):.4g}"
    if isinstance(x, (tuple, list)):
        inner = ", ".join(_fmt(v) for v in x)
        return f"({inner})" if isinstance(x, tuple) else f"[{inner}]"
    return repr(x)


def _close(got, expected, tol):
    if isinstance(expected, bool):
        is_boolish = isinstance(got, (bool, np.bool_))
        return is_boolish and bool(got) == expected
    if isinstance(expected, numbers.Real) and not isinstance(expected, numbers.Integral):
        try:
            return abs(float(got) - float(expected)) <= tol
        except (TypeError, ValueError):
            return False
    if isinstance(expected, (tuple, list)) and isinstance(got, (tuple, list)):
        return len(got) == len(expected) and all(_close(g, e, tol) for g, e in zip(got, expected))
    try:
        return bool(got == expected)
    except Exception:
        return False


def check(name, func, cases, tol=1e-6, hint=None):
    """Call func on each (args, expected) pair and report whether the results match.

    args can be a single value or a tuple of arguments. Use () for a function with no arguments.
    """
    for args, expected in cases:
        if not isinstance(args, tuple):
            args = (args,)
        shown = f"{name}({', '.join(_fmt(a) for a in args)})"
        try:
            got = func(*args)
        except NotImplementedError:
            print(f"Not started: {name}. Write it in the cell above, run that cell, then run this one again.")
            return False
        except Exception as exc:  # report the error instead of a long traceback
            print(f"Error: {shown} raised {type(exc).__name__}: {exc}")
            if hint:
                print(f"Hint: {hint}")
            return False
        if got is None and expected is not None:
            print(f"Not started: {shown} returned None. Did you forget the return statement?")
            return False
        if not _close(got, expected, tol):
            print(f"Not yet: {shown} returned {_fmt(got)}, but the expected answer is about {_fmt(expected)}.")
            if hint:
                print(f"Hint: {hint}")
            return False
    print(f"Correct: {name} passed {len(cases)} check{'s' if len(cases) != 1 else ''}.")
    return True


def check_value(name, value, expected, tol=1e-6, hint=None):
    """Compare a value you computed with the expected answer."""
    if value is None:
        print(f"Not started: {name}. Replace None with your answer and run the cell again.")
        return False
    if not _close(value, expected, tol):
        print(f"Not yet: {name} is {_fmt(value)}, but the expected answer is about {_fmt(expected)}.")
        if hint:
            print(f"Hint: {hint}")
        return False
    print(f"Correct: {name}.")
    return True

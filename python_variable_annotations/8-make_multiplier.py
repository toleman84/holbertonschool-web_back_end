#!/usr/bin/env python3
"""
    doc
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        This function takes a float multiplier as argument
        and returns a function that multiplies a float by multiplier.

        Args:
            multiplier: A float.

        Returns:
            A function that multiplies a float by multiplier.
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function

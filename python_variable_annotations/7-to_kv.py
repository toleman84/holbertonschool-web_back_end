#!/usr/bin/env python3
"""
    doc
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        This function takes a string k and an int OR float v as arguments
        and returns a tuple.

        Args:
          k: A string.
          v: An int or float.

        Returns:
          A tuple of (k, v^2).
    """

    return (k, v**2)

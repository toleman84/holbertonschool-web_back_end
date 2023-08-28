#!/usr/bin/env python3
"""doc"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list mxd_lst of integers and floats
    and returns their sum as a float.

    Args:
      mxd_lst: A list of integers and floats.

    Returns:
      The sum of the numbers in mxd_lst.
    """

    sum: float = 0.0
    for number in mxd_lst:
        sum += number

    return sum

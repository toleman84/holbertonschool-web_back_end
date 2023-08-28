#!/usr/bin/env python3
"""doc"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list input_list of floats as argument
    and returns their sum as a float.

    Args:
        input_list: A list of floats.

    Returns:
        The sum of the numbers in input_list.
    """

    sum = 0.0
    for number in input_list:
        sum += number

    return sum

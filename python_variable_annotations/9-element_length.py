#!/usr/bin/env python3
"""
    doc
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        This function takes an iterable of sequences as argument and returns
        a list of tuples, where each tuple contains a sequence and its length.

        Args:
            lst: An iterable of sequences.

        Returns:
            A list of tuples of (sequence, length).
    """

    return [(i, len(i)) for i in lst]

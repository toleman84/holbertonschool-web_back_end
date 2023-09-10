#!/usr/bin/env python3
"""doc"""

from typing import Tuple


def index_range(page: int, page_size: int):
    """ Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.

        Args:
            page (_type_): _description_
            page_size (_type_): _description_
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size

    return (start_index, end_index)

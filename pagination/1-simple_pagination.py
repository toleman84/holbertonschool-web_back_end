#!/usr/bin/env python3
"""doc"""

def index_range(page, page_size):
    """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.

        Args:
            page (_type_): _description_
            page_size (_type_): _description_
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size

    return (start_index, end_index)

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_

            Args:
                page (int, optional): _description_. Defaults to 1.
                page_size (int, optional): _description_. Defaults to 10.

            Returns:
                List[list]: _description_
        """
        assert page > 0
        assert page_size > 0

        dataset = self.dataset()
        num_rows = len(dataset)
        start_index, end_index = index_range(page, page_size)
        
        if start_index >= num_rows:
            return []
        
        return dataset[start_index:end_index]

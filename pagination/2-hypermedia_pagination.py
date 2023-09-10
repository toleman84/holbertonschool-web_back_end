#!/usr/bin/env python3
"""
    doc
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.

        Args:
            page (_type_): _description_
            page_size (_type_): _description_
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        num_rows = len(dataset)
        start_index, end_index = index_range(page, page_size)

        if start_index >= num_rows:
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            Get pagination hyper data.

            Args:
                page (int, optional): Page number. Defaults to 1.
                page_size (int, optional): Page size. Defaults to 10.

            Returns:
                Dict: Pagination hyper data.
    """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_data = self.get_page(page, page_size)
        num_rows = len(self.dataset())
        total_pages = math.ceil(num_rows / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

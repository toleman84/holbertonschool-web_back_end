#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
            Get pagination hyper data with deletion resilience.

            Args:
                index (int): Start index of the current page. Defaults None
                page_size (int, optional): The page size. Defaults to 10.

            Returns:
                Dict: Pagination hyper data.
        """
        assert isinstance(page_size, int) and page_size > 0
        if index is None:
            index = 0

        dataset = self.indexed_dataset()
        num_row = len(dataset)

        start_index = index
        end_index = start_index + page_size

        if start_index >= num_row:
            return {"data": []}

        # Check if any rows were deleted between the start and end index
        while end_index < num_row and dataset[end_index] is None:
            end_index -= -1

        next_index = end_index

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": end_index,
        }

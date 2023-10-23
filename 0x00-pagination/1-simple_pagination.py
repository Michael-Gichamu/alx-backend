#!/usr/bin/env python3
"""
Contains function index_range and class Server
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    """
    Creates a Tuple containing start and end index, based on page
    and page_size.

    Args:
        page (int): Page numbers indexed from 1.
        page_size (int): Items in page.

    Returns:
        Tuple: size of page containing start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


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
        """Creates a list of paginated data.

        Args:
            page (int, optional): Number of pages. Defaults to 1.
            page_size (int, optional): Number of items per page.
                                       Defaults to 10.

        Returns:
            List[List]: List of items of the appropriate page of the dataset.
        """
        assert page > 0 or page_size > 0
        assert isinstance(page, int) and isinstance(page_size, int)
        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()
        if start_idx > len(dataset) or end_idx > len(dataset):
            return []
        return dataset[start_idx: end_idx]
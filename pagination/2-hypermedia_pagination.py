#!/usr/bin/env python3
"""
This module contains a Server class for hypermedia pagination
of a dataset of popular baby names
"""
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

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Calculates the start and end indexes for pagination

        Args:
            page (int): the page number (starts at 1)
            page_size (int): number of items per page

        Returns:
            tuple: (start_index, end_index)
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the requested page of the dataset

        Args:
            page (int): the page number (must be > 0)
            page_size (int): number of items per page (must be > 0)

        Returns:
            List[List]: the corresponding page of rows,
            or an empty list if out of range
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing pagination metadata
        along with the requested page of the dataset

        Args:
            page (int): the page number (must be > 0)
            page_size (int): number of items per page (must be > 0)

        Returns:
            dict: pagination metadata and dataset page
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

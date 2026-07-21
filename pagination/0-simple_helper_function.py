#!/usr/bin/env python3
"""
This module contains a helper function for pagination
"""


def index_range(page, page_size):
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

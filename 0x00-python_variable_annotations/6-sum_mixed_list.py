#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union
Mixed = List[Union[float, int]]


def sum_mixed_list(mxd_list: Mixed) -> float:
    """Returns a float from summing a mixed list"""
    return sum(mxd_list)

#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import List, Union, Tuple
Mixed = Union[int, float]


def to_kv(k: str, v: Mixed) -> Tuple[str, float]:
    """Returns a tuple of string and float"""
    return (k, v * v)

#!/bin/bash/env python3
"""Test Utils Module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class to Test Nested Map function"""

    @parameterized.expand([
        ("single", {"a": 1}, ["a"], 1),
        ("single_dict", {"a": {"b": 2}}, ["a"], {"b": 2}),
        ("final", {"a": {"b": 2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """test case for nested map access"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

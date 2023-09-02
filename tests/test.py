import unittest

from main import base_sort


class TestBaseSort(unittest.TestCase):
    def test_empty_array(self):
        array = []
        expected_result = []
        self.assertEqual(base_sort(array), expected_result)

    def test_sorted_array(self):
        array = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(base_sort(array), expected_result)

    def test_reverse_sorted_array(self):
        array = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(base_sort(array), expected_result)

    def test_unsorted_array(self):
        array = [3, 1, 4, 2, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(base_sort(array), expected_result)

    def test_array_with_duplicates(self):
        array = [3, 1, 4, 2, 5, 3, 4]
        expected_result = [1, 2, 3, 3, 4, 4, 5]
        self.assertEqual(base_sort(array), expected_result)

# tests/test_sort.py
# Sorting Tests: Selection Sort, Bubble Sort

import unittest
import sys
import os
import random

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from selection_sort import selection_sort
from bubble_sort import bubble_sort

class TestSort(unittest.TestCase):

    def setUp(self):
        self.test_function = selection_sort

    def test_error(self):
        with self.assertRaises(ValueError) as context:
            self.test_function(1)
        self.assertEqual(str(context.exception), "Input type must be a list.")

    def test_sorted_array(self):
        self.assertEqual(self.test_function([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
    
    def test_reverse_sorted_array(self):
        self.assertEqual(self.test_function([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
    
    def test_unsorted_array(self):
        self.assertEqual(self.test_function([3, 1, 4, 6, 7, 2, 5]), [1, 2, 3, 4, 5, 6, 7])
    
    def test_duplicates_array(self):
        self.assertEqual(self.test_function([4, 7, 2, 3, 7, 4]), [2, 3, 4, 4, 7, 7])

    def test_negative_array(self):
        self.assertEqual(self.test_function([3, -1, 7, -2, 0]), [-2, -1, 0, 3, 7])
    
    def test_empty_array(self):
        self.assertEqual(self.test_function([]), [])
    
    def test_single_element_array(self):
        self.assertEqual(self.test_function([9]), [9])
    
    def test_large_random_array(self):
        large_random_array = random.sample(range(1, 1001), 100)
        sorted_lra = sorted(large_random_array)
        self.assertEqual(self.test_function(large_random_array), sorted_lra)

    
class TestSelectionSort(TestSort):
    def setUp(self):
        super().setUp()
        self.test_function = selection_sort

class TestBubbleSort(TestSort):
    def setUp(self):
        super().setUp()
        self.test_function = bubble_sort


if __name__ == "__main__":
    unittest.main()
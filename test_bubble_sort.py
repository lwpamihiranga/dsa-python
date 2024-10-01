import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    
    def test_empty_list(self):
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [], "Failed on empty list")
        
    def test_single_element(self):
        arr = [1]
        bubble_sort(arr)
        self.assertEqual(arr, [1], "Failed on single element list")
        
    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5], "Failed on already sorted list")
    
    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5], "Failed on reverse sorted list")
    
    def test_unsorted_list(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90], "Failed on unsorted list")
        
    def test_list_with_duplicates(self):
        arr = [3, 1, 2, 2, 3, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 2, 3, 3], "Failed on list with duplicates")

    def test_large_numbers(self):
        arr = [1000, 500, 100000, 50000, 0]
        bubble_sort(arr)
        self.assertEqual(arr, [0, 500, 1000, 50000, 100000], "Failed on list with large numbers")

if __name__ == '__main__':
    unittest.main()

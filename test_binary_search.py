import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_cases(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 1))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5))
        self.assertFalse(binary_search([1, 2, 3, 4, 5], 6))
        self.assertFalse(binary_search([], 1))
        self.assertTrue(binary_search([1], 1))
        self.assertFalse(binary_search([1], 2))
        self.assertTrue(binary_search([1, 2], 1))
        self.assertTrue(binary_search([1, 2], 2))
        self.assertFalse(binary_search([1, 2], 3))
        self.assertTrue(binary_search([1, 1, 1, 1, 1], 1))
        self.assertFalse(binary_search([1, 1, 1, 1, 1], 2))
        large_list = list(range(1000))
        self.assertTrue(binary_search(large_list, 500))
        self.assertTrue(binary_search(large_list, 0))
        self.assertTrue(binary_search(large_list, 999))
        self.assertFalse(binary_search(large_list, 1000))

if __name__ == "__main__":
    unittest.main()

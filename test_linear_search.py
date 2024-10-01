import unittest
from linear_search import linear_search

# Test cases for linear_search
class TestLinearSearch(unittest.TestCase):

    def test_needle_in_haystack(self):
        self.assertTrue(linear_search([1, 2, 3, 4, 5], 3))

    def test_needle_not_in_haystack(self):
        self.assertFalse(linear_search([1, 2, 3, 4, 5], 6))

    def test_empty_haystack(self):
        self.assertFalse(linear_search([], 3))

    def test_single_element_haystack_found(self):
        self.assertTrue(linear_search([1], 1))

    def test_single_element_haystack_not_found(self):
        self.assertFalse(linear_search([1], 2))

    def test_multiple_occurrences_of_needle(self):
        self.assertTrue(linear_search([1, 2, 3, 3, 4], 3))

if __name__ == '__main__':
    unittest.main()

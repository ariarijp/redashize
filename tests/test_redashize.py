import unittest

from redashize import redashize, unredashize


class RedashizeTest(unittest.TestCase):
    result = {
        'columns': [
            {'name': 'a', 'friendly_name': 'a'},
            {'name': 'b', 'friendly_name': 'b'},
            {'name': 'c', 'friendly_name': 'c'},
        ],
        'rows': [
            {'a': 1, 'b': 0.2, 'c': 'foo'},
            {'a': 2, 'b': 0.4, 'c': 'bar'},
            {'a': 3, 'b': 0.6, 'c': 'baz'},
        ],
    }

    def test_redashize(self):
        self.assertEqual(redashize(self.result['rows']), self.result)

    def test_unredashize(self):
        self.assertEqual(unredashize(self.result), self.result['rows'])


if __name__ == '__main__':
    unittest.main()

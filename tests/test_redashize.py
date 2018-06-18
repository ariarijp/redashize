import unittest

from redashize import redashize


class RedashizeTest(unittest.TestCase):
    def test(self):
        result = redashize([
            {'a': 1, 'b': 0.2, 'c': 'foo'},
            {'a': 2, 'b': 0.4, 'c': 'bar'},
            {'a': 3, 'b': 0.6, 'c': 'baz'},
        ])
        expected = {
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
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

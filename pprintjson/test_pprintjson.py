"""pprintjson test module"""

import unittest
import os
from unittest.mock import patch
from pprintjson import pprintjson as ppjson


class test_pprintjson(unittest.TestCase):
    """pprintjson function tests."""

    def test_example1(self):
        obj = {"a": 1}

        with open('test1.json', 'a+') as f:
            ppjson(obj, file=f)
            f.seek(0)
            result = f.read()
            self.assertTrue(obj, result)

    @patch('pprintjson.pprintjson')
    def test_example2(self, mock_ppjson):
        obj = {"a": 1}
        mock_ppjson(obj)

        mock_ppjson.assert_called_once()
        mock_ppjson.assert_called_with(obj)
        self.assertEqual(mock_ppjson.call_count, 1)

    def tearDown(self):
        os.remove('test1.json')


if __name__ == '__main__':
    unittest.main()

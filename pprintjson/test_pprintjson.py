"""pprintjson test module"""
import os
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from json import dumps
from unittest.mock import patch

from pprintjson import pprintjson as ppjson


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class test_pprintjson(unittest.TestCase):
    """pprintjson function tests."""

    def test_example1(self):
        obj = {"a": 1}

        with open("test1.json", "a+") as f:
            ppjson(obj, file=f)
            f.seek(0)
            result = f.read()
            self.assertTrue(obj, result)

    def test_example2(self):
        obj = {"a": 1}
        with captured_output() as (out, err):
            ppjson(obj, file=sys.stdout)
            self.assertEqual(out.getvalue(), dumps(obj, indent=4) + "\n")

    @patch("pprintjson.pprintjson")
    def test_example3(self, mock_ppjson):
        obj = {"a": 1}
        mock_ppjson(obj)

        mock_ppjson.assert_called_once()
        mock_ppjson.assert_called_with(obj)
        self.assertEqual(mock_ppjson.call_count, 1)

    def tearDown(self):
        try:
            os.remove("test1.json")
        except OSError:
            pass


if __name__ == "__main__":
    unittest.main()

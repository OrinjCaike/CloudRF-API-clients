"""Unit Tests for demos"""
import unittest

from pathlib import Path

import points


class TestPoints(unittest.TestCase, points.App):
    """A unittest class to call tests independently from the main application

    Call with python -m unittest test_area for running all tests
    Call with python -m unittest test_demo.TestArea.test_best_server for running only best_server test
    see unittest documentation for more details.
    """

    def __init__(self, *pargs, **kwargs):
        unittest.TestCase.__init__(self, *pargs, **kwargs)
        points.App.__init__(self, '-i points_A.csv -t points_tmpl_A.json -s kmz -r')

    def test_responses(self):
        """ Test the correct number of responses are received"""

        self.responses = self.run_area()

        self.assertEqual(len(self.responses), self.row_count, "Should have as many responses as rows in CSV")

        for f in self.api.downloaded_files:
            self.assertTrue(Path(f).is_file(), f'File {f} should exist')

        # delete files produced
        for f in self.api.downloaded_files:
            Path(f).unlink()

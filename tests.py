import unittest
from unittest.mock import patch
import iss_io
from io import StringIO
import re


class TestISSFunctions(unittest.TestCase):
    def test_print_current_location(self):
        with patch('sys.stdout', new=StringIO()) as stdout_capture:
            iss_io.print_current_location()
            self.assertTrue(re.match(
                '\nThe current location of the ISS at \d+:\d+:\d+ is \([-+]?\d*\.*\d+, [-+]?\d*\.*\d+\)\n\n', stdout_capture.getvalue())
            )

    def test_print_next_pass(self):
        with patch('sys.stdout', new=StringIO()) as stdout_capture:
            iss_io.print_next_pass(48.858504, 2.294513)
            self.assertTrue(re.match(
                '\nThe ISS will be overhead \([-+]?\d*\.*\d+, [-+]?\d*\.*\d+\) at \d+:\d+:\d+ for \d+:\d+:\d+\n\n', stdout_capture.getvalue())
            )

    def test_print_people(self):
        with patch('sys.stdout', new=StringIO()) as stdout_capture:
            iss_io.print_people()
            self.assertTrue(re.match(
                '\nAstronauts aboard the ISS: .*\n\n', stdout_capture.getvalue())
            )


if __name__ == '__main__':
    unittest.main()

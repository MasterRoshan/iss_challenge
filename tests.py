import unittest
import iss_io
from io import StringIO
import re


class TestISSFunctions(unittest.TestCase):
    def test_print_current_location(self):
        current_location = iss_io.current_location()
        self.assertTrue(re.match(
            'The current location of the ISS at \d+:\d+:\d+ is \([-+]?\d*\.*\d+, [-+]?\d*\.*\d+\)', current_location)
        )

    def test_print_next_pass(self):
        next_pass = iss_io.next_pass(48.858504, 2.294513)
        self.assertTrue(re.match(
            'The ISS will be overhead \([-+]?\d*\.*\d+, [-+]?\d*\.*\d+\) at \d+:\d+:\d+ for \d+:\d+:\d+', next_pass)
        )

    def test_print_people(self):
        people = iss_io.people()
        self.assertTrue(re.match(
            'Astronauts aboard the ISS: .*', people)
        )


if __name__ == '__main__':
    unittest.main()

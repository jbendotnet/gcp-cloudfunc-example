import unittest
from pytest import raises
from dataclasses import dataclass
from util import format_greeting

class TestUtil(unittest.TestCase):
    def test_format_greeting(self):
        @dataclass
        class TestCase:
            input: str
            want: str

        testcases = {
            "Should state name": TestCase(
                input="Joe Bloggs",
                want="Hello Joe Bloggs",
            ),
        }
        for name, case in testcases.items():
            with self.subTest(name, case=case):
                got = format_greeting(name=case.input)
                self.assertEqual(case.want, got, name)

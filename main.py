import unittest
from ultis.ultis import *
from test_case import TestCase
import sys
import test_variable
from test_variable import FOLDER

ultis = Ultis()
test_case = TestCase()
test_arg = sys.argv[1]
test_variable = getattr(test_variable, test_arg)

files = ultis.get_files(FOLDER)

class TestAppium(unittest.TestCase):
    def test_voice(self):
        for file in files:
            with self.subTest(file=file):
                test_case.test_voice(file=file, test_variable=test_variable)

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
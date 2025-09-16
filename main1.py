import unittest
from ultis.ultis import *
from test_variables import FOLDER
from test_case1 import TestCase
import sys
import test_variable1

ultis = Ultis()
test_case = TestCase()
test_arg = sys.argv[1]
test_variable = getattr(test_variable1, test_arg)
print(test_variable)


files = ultis.get_files(FOLDER)

class TestAppium(unittest.TestCase):
    def test_voice(self):
        for file in files:
            with self.subTest(file=file):
                test_case.test_voice(file=file, test_variable=test_variable)


if __name__ == "__main__":
    # tránh unittest đọc sys.argv (ngoài tên file)
    unittest.main(argv=[sys.argv[0]])
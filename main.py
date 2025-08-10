import unittest
from ultis.ultis import *
from test_variables import FOLDER
from test_case import TestCase

ultis = Ultis()
test_case = TestCase()

files = ultis.get_files(FOLDER)

class TestAppium(unittest.TestCase):
    def test_voice_to_text(self):
        for file in files:
            with self.subTest(file=file):
                test_case.test_voice(file=file)

unittest.main()

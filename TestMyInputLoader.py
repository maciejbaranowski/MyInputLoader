import unittest
from unittest.mock import MagicMock
from MyInputLoader import MyInputLoader

class TestMyInputLoader(unittest.TestCase):
    def testReadsSingleIntegerLine(self):
        #loader = self.setUp()
        self.sut.fileHandle.readline = MagicMock(return_value="3")
        self.assertEqual(self.sut.loadSingleIntegerLine(), 3)

    def testReadsMultipleIntegerOneLine(self):
        #loader = self.setUp()
        self.sut.fileHandle.readline = MagicMock(return_value="3 4 5")
        self.assertEqual(self.sut.loadMultipleIntegerLine(), [3,4,5])

    def setUp(self):
        self.sut = MyInputLoader()

if __name__ == '__main__':
    unittest.main()
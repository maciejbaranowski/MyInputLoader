import unittest
from unittest.mock import MagicMock

from utils import InputHandler

class TestInputHandler(unittest.TestCase):
    def testReadsSingleIntegerLine(self):
        self.setReadLineMock(["3"])
        self.assertEqual(self.sut.loadSingleElementLine(), 3)

    def testReadsSingleIntegerLineHugeNumber(self):
        self.setReadLineMock(["123456789012345678901234567890123456789012345678901234567890"])
        self.assertEqual(self.sut.loadSingleElementLine(),
                         123456789012345678901234567890123456789012345678901234567890)

    def testReadsMultipleIntegerOneLine(self):
        self.setReadLineMock(["3 4 11"])
        self.assertEqual(self.sut.loadMultipleElementLine(), [3, 4, 11])

    def testReadsMultipleIntegerOneLineCustomSeparator(self):
        self.setReadLineMock(["-23|5|111"])
        self.assertEqual(self.sut.loadMultipleElementLine("|"), [-23, 5, 111])

    def testReadsMultipleIntegerMultipleLines(self):
        self.setReadLineMock(["1 2 3 4","111 23 -4 1","0 0 9 9"])
        self.assertEqual(self.sut.loadMultipleElementMultipleLines(3),
                         [[1, 2, 3, 4],[111, 23, -4, 1],[0, 0, 9, 9]])

    def testReadsSingleFloat(self):
        self.setReadLineMock(["-12.335"])
        self.assertEqual(self.sut.loadSingleElementLine(format = float),-12.335)

    def testReadsSingleWord(self):
        self.setReadLineMock(["ABC"])
        self.assertEqual(self.sut.loadSingleElementLine(format = str),'ABC')

    def setUp(self):
        self.sut = InputHandler()

    def setReadLineMock(self, returnValue):
        self.sut.readline = MagicMock()
        self.sut.readline.side_effect = returnValue


if __name__ == '__main__':
    unittest.main()
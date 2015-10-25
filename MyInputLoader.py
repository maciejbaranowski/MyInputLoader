import fileinput

class MyInputLoader:
    def __init__(self):
        self.fileHandle = fileinput.input()
    def openFile(self, fileName):
        self.fileHandle = open(fileName, 'r')
    def closeFile(self):
        self.fileHandle.close()
    def loadSingleIntegerLine(self):
        return int(self.fileHandle.readline())
    def loadMultipleIntegerLine(self, separator=" "):
        line = self.fileHandle.readline()
        line = line.split(separator)
        return [int(i) for i in line]
    def loadMultipleIntegerMultipleLines(self, lines, separator=" "):
        outputMatrix = []
        for noOfLine in range(lines):
            outputMatrix.append(self.loadMultipleIntegerLine())
        return outputMatrix

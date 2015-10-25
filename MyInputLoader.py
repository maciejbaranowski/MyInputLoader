import fileinput

class MyInputLoader:
    def __init__(self):
        self.fileHandle = fileinput.input()
    def openFile(self, fileName):
        self.fileHandle = open(fileName, 'r')
    def closeFile(self):
        self.fileHandle.close()
    def loadSingleElementLine(self, format = int):
        return format(self.fileHandle.readline())
    def loadMultipleElementLine(self, separator=" ", format = int):
        line = self.fileHandle.readline()
        line = line.split(separator)
        return [format(i) for i in line]
    def loadMultipleElementMultipleLines(self, lines, separator=" ", format = int):
        outputMatrix = []
        for noOfLine in range(lines):
            outputMatrix.append(self.loadMultipleElementLine(format = format))
        return outputMatrix

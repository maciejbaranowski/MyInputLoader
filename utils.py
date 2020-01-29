import fileinput
import os
import time
import io

class InputHandler(fileinput.FileInput):
    def loadSingleElementLine(self, format = int):
        return format(self.readline())
    def loadMultipleElementLine(self, separator=" ", format = int):
        line = self.readline()
        line = line.split(separator)
        return [format(i) for i in line]
    def loadMultipleElementMultipleLines(self, lines, separator=" ", format = int):
        outputMatrix = []
        for _ in range(lines):
            outputMatrix.append(self.loadMultipleElementLine(format = format))
        return outputMatrix

#TODO: Add tests to OutputHandler
class OutputHandler(io.TextIOWrapper):
    def write(self, value):
        arraySeparator = " "
        if isinstance(value, list):
            output = arraySeparator.join(map(str, value))
            super().write(output)
        else:
            super().write(str(value))
    def writeline(self, value):
        self.write(value)
        self.write("\n")

def processAll(solution):
    for inputFileName in os.listdir("in"):
        outputFileName = f'{inputFileName.split(".in")[0]}.out'
        with InputHandler("in/"+inputFileName) as inputFile:
            with OutputHandler(open("out/"+outputFileName, 'wb')) as outputFile:
                startTime = time.process_time()
                solution(inputFile, outputFile)   
                solutiontime = startTime - time.process_time()
        print(f'Processed {inputFileName}, it took {solutiontime} seconds')



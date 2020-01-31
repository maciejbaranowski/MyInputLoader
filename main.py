import utils

def solution(input : utils.InputHandler, output : utils.OutputHandler):
    [maxNumOfSlices, numOfPizzas] = input.loadMultipleElementLine()
    numOfSlicesInPizza = input.loadMultipleElementLine()
    selectedPizzas = []

    #Algorithm: just naively take pizzas from smallest one until max is reached
    slicesCounter = 0
    pizzaCounter = 0
    while pizzaCounter < numOfPizzas:
        if slicesCounter + numOfSlicesInPizza[pizzaCounter] <= maxNumOfSlices:
            slicesCounter += numOfSlicesInPizza[pizzaCounter]
            pizzaCounter += 1
        else:
            break

    selectedPizzas = list(range(0,pizzaCounter))

    output.writeline(len(selectedPizzas))
    output.writeline(selectedPizzas)

utils.processAll(solution)
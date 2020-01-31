import utils
from memoization import cached

def solution(input : utils.InputHandler, output : utils.OutputHandler):
    [maxNumOfSlices, numOfPizzas] = input.loadMultipleElementLine()
    numOfSlicesInPizza = input.loadMultipleElementLine()
    selectedPizzas = []

    #Algotithm: recursively check problem for n - 1 pizzas. Optimal but slow
    @cached(max_size=100000)
    def subProblem(numOfSlicesInPizzaSubset, maxNumOfSlicesSubset):
        if len(numOfSlicesInPizzaSubset) == 0:
            return [0 , []]
        pizzaTaken = subProblem(numOfSlicesInPizzaSubset[:-1], maxNumOfSlicesSubset - numOfSlicesInPizzaSubset[-1]) 
        pizzaTaken[0] += numOfSlicesInPizzaSubset[-1]
        pizzaNotTaken = subProblem(numOfSlicesInPizzaSubset[:-1], maxNumOfSlicesSubset)
    
        if (pizzaTaken[0] > pizzaNotTaken[0] and pizzaTaken[0] < maxNumOfSlicesSubset):
            return [pizzaTaken[0], pizzaTaken[1] + [len(numOfSlicesInPizzaSubset) - 1]]
        else:
            return [pizzaNotTaken[0], pizzaNotTaken[1]]

    [score, selectedPizzas] = subProblem(numOfSlicesInPizza, maxNumOfSlices)
    print(f"Score: {score}")
    output.writeline(len(selectedPizzas))
    output.writeline(selectedPizzas)

utils.processAll(solution)
import numpy as np

import random


class Chain:
    def __init__(self, percentageMatrix, states):
        self.percentageMatrix = percentageMatrix
        self.states = states
        # sum all percentages and raise error if sum is not 1
        for percentages in self.percentageMatrix:
            if sum(percentages) != 1:
                raise Exception(
                    "Every list in percentage matrix needs to have a sum of 1. This list is not correct {}".format(
                        percentages
                    )
                )
        self.state = ""

    def setState(self, indexState):
        self.state = self.states[indexState]

    def guess(self, times):
        # guess values
        values = []
        for i in range(0, times):
            # why get only 1 random choice
            # Its guesses a state and then it sets the current state
            # so it loops through all states instead getting only the percentages of one state
            value = np.random.choice(
                self.states, 1, p=self.percentageMatrix[self.states.index(self.state)]
            )
            values.append(value[0])
            self.state = value[0]
        return values

    def count_geusses(self, guesses):
        # counting every guess
        count = {}
        for item in guesses:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        return count

    def print_percentages(self, guesses, x):
        # calculating percentage of all guesses
        data = self.count_geusses(guesses)
        for item in self.states:
            print("{} has a percentage of: {}%".format(item, data[item] / x * 100))


percentagematrix = [[0.8, 0.1, 0.1], [0.4, 0.5, 0.1], [0.6, 0.2, 0.2]]
states = ["Hongerig", "Tevreden", "Opgejaagd"]

chain = Chain(percentagematrix, states)
chain.state = np.random.choice(states, 1, p=[0.7, 0.1, 0.2])


guesses = chain.guess(1000)

chain.print_percentages(guesses, 1000)

# adding an extra state
print()
print("=======================")
print("Adding Verdrietig state")
print("=======================")
print()

percentagematrix = [
    [0.6, 0.1, 0.1, 0.2],
    [0.4, 0.3, 0.1, 0.2],
    [0.4, 0.2, 0.2, 0.2],
    [0.6, 0.1, 0.1, 0.2],
]
states = ["Hongerig", "Tevreden", "Opgejaagd", "Verdrietig"]

chain = Chain(percentagematrix, states)
chain.state = np.random.choice(states, 1, p=[0.6, 0.1, 0.2, 0.1])

guesses = chain.guess(1000)

chain.print_percentages(guesses, 1000)

# adding bayes
print()
print("=======================")
print("Adding Bayes Zwanger")
print("=======================")
print()


percentagematrix = [[0.8, 0.1, 0.1], [0.4, 0.5, 0.1], [0.6, 0.2, 0.2]]

states = ["Hongerig", "Tevreden", "Opgejaagd"]

chain = Chain(percentagematrix, states)

is_zwanger = np.random.choice([True, False], 1, p=[0.25, 0.75])[0]
if is_zwanger:
    chain.state = np.random.choice(states, 1, p=[0.7, 0.1, 0.2])
else:
    chain.state = np.random.choice(states, 1, p=[0.5, 0.35, 0.15])

guesses = chain.guess(1000)

chain.print_percentages(guesses, 1000)

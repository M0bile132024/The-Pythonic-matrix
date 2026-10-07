#Class version of Perceptron
import random
from functools import lru_cache 

class Perceptron:
    def __init__(self, no, learning_rate=0.00001):
        # Set Initial Values
        self.learnc = learning_rate
        self.bias = 1

        # Compute Random Weights
        self.weights = [random.uniform(-1, 1) for _ in range(no + 1)]

    # Activate Function
    
    def activate(self, inputs):
        sum_value = 0
        for i in range(len(inputs)):
            sum_value += inputs[i] * self.weights[i]
        return 1 if sum_value > 1.5 else 0

    # Train Function
    def train(self, inputs, desired):
        inputs.append(self.bias)
        guess = self.activate(inputs)
        error = desired - guess
        if error != 0:
            for i in range(len(inputs)):
                self.weights[i] += self.learnc * error * inputs[i]
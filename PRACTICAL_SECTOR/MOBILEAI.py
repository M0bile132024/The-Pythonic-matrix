#MOBILE.AI
#Ver 1.5
#Author:M0bile132022
#A test project using machine learning(kind of)
import matplotlib.pyplot as plt
import numpy as np
import random
import Perceptron_Lib as Perceptron_Lib
#Functions VVVVVVVV
def activate(activate_inputs,activate_weights,threshold=1.5):
    sum_value = 0
    for i in range(len(activate_inputs)):
        sum_value += activate_inputs[i] * activate_weights[i]
    return 1 if sum_value > threshold else 0
def perceptron(no,learning_rate=0.00001):
    learn_c = learning_rate
    bias = 1
    weight = []
    for i in range(no):
        weight.append(random.uniform(-1,1))
def train(weights,bias,learnc, inputs, desired,threshold=1.5):
    inputs.append(bias)
    guess = activate(inputs,threshold,weights)
    error = desired - guess
    if error != 0:
        for i in range(len(inputs)):
            weights[i] += learnc * error * inputs[i]
#Tests VVVVVVV
def concert_perceptron():
    #Test 1:Concert Perceptron
    '''Context:A Perceptron is an Artificial Neuron.

    It is the simplest possible Neural Network.

    Neural Networks are the building blocks of Machine Learning.'''
    #Source:https://www.w3schools.com/ai/ai_perceptrons.asp
    print("Welcome to the Mobile AI Test 1:Concert Perceptron")
    print("This is a test of the Perceptron/ Linear Binary Classifiers.")   
    artist = int(input("Please input whether the artist is good(0 if bad,1 if good):"))
    if artist > 0:
        artist = 1
    else:
        artist = 0
    #The artist is either good or bad, so we can use a binary value of 0 or 1
    weather = int(input("Please input whether the weather is good(0 if bad,1 if good):"))
    if weather > 0:
        weather = 1
    else:
        weather = 0
    time = int(input("Please input whether the time is good(0 if bad,1 if good):"))
    if time > 0:
        time = 1
    else:
        time = 0
    friend = int(input("Please input whether your friends are coming(0 if no,1 if yes):"))
    if friend > 0:
        friend = 1
    else:
        friend = 0
    food = int(input("Please input whether the food is good(0 if bad,1 if good):"))
    if food > 0:
        food = 1
    else:
        food = 0
    alchol = int(input("Please input whether the alchol will be served(0 if no,1 if yes):"))
    if alchol > 0:
        alchol = 1
    else:
        alchol = 0
    threshold = float(input("Please input how you feel about concerts on a range from 1 to 6(1 being I'll go to any,6 being very picky):"))
    input_list = [artist,weather,time,friend,food,alchol]
    weights = [0.7,0.6,0.5,0.5,0.3,0.4]
    if activate(input_list, threshold, weights) == 1:
        print("You should go to the concert.")
    else:
        print("You should not go to the concert.")
    print("Thank you for using the Mobile AI Test 1:Concert Perceptron")




def line_plotting_perceptron(nump,lr=0.01,gradient=2, intercept=3,bias=2,iterations=100001):
    # Test 2: Line Plotting Perceptron
    num_points = nump
    learning_rate = lr
    errors = 0
    # Generate 500 random x, y points
    np.random.seed(42)  # For reproducibility
    x_points = np.random.uniform(0, 10, num_points)
    y_points = np.random.uniform(0, 10, num_points)

    # Display x, y points
    plt.scatter(x_points, y_points, color='blue', label='Random Points')

    # Define the line function f(x) = mx + c
    def f(x, m=gradient, c=intercept):
        return m * x + c

    # Generate the line based on the function
    line_x = np.linspace(0, 10, 100)
    line_y = f(line_x)  # Example line with slope 2 and intercept 3

    # Display the line
    plt.plot(line_x, line_y, color='red', label=f"Line f(x) = {gradient}x + {intercept}")

    # Compute the desired answers (e.g., count of points above the line)
    desired = [1 if y > f(x) else 0 for x, y in zip(x_points, y_points)]

    ptron = Perceptron_Lib.Perceptron(bias, learning_rate)
    for j in range(iterations):
        for i in range(num_points):
            ptron.train([x_points[i], y_points[i]], desired[i])
    for i in range(num_points):
        x = x_points[i]
        y = y_points[i]
        guess = ptron.activate([x, y, ptron.bias])
        color = "red"
        if guess == 0:
            color = "blue"
        if ((y > f(x) and guess == 0) or (y < f(x) and guess == 1)):
            errors += 1  # Increment errors by 1 if the condition is met
        plt.scatter(x, y, color=color)
    plt.title("Line Plotting Perceptron")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()
    print("Thank you for using the Mobile AI Test 2:Line Plotting Perceptron")
    print("This test uses a Perceptron to plot a line and classify points.")
    print("The red points are above the line and the blue points are below the line.")
    print("The line is defined by the function f(x) = mx + c.")
    print(f"The slope of the line is {gradient} and the intercept is {intercept}.")
    print("The perceptron is trained to classify the points above and below the line.")
    print("The perceptron is trained using the backpropagation algorithm.")
    print("The perceptron is trained using a simple weight update rule.")
    print(f"The perceptron made {errors} errors out of {num_points} points.")
class Trainer:
    def __init__(self, xArray, yArray):
        self.xArr = xArray
        self.yArr = yArray
        self.points = len(self.xArr)
        self.learnc = 0.00001
        self.weight = 0
        self.bias = 1
        self.cost = None

    # Cost Function
    def costError(self):
        total = 0
        for i in range(self.points):
            total += (self.yArr[i] - (self.weight * self.xArr[i] + self.bias)) ** 2
        return total / self.points

    # Train Function
    def train(self, iter):
        for _ in range(iter):
            self.updateWeights()
        self.cost = self.costError()

    # Update Weights Function
    def updateWeights(self):
        w_deriv = 0
        b_deriv = 0
        for i in range(self.points):
            wx = self.yArr[i] - (self.weight * self.xArr[i] + self.bias)
            w_deriv += -2 * wx * self.xArr[i]
            b_deriv += -2 * wx
        self.weight -= (w_deriv / self.points) * self.learnc
        self.bias -= (b_deriv / self.points) * self.learnc


#Main VVVVVVVV
print("Welcome to the Mobile AI")
print("Please choose a test to perform:")
print("""1:Concert Perceptron
2:Line Plotting Preceptron
3:Exit""")
match input("Please input the number of the test you wish to perform:"):
    case "1":
        concert_perceptron()
    case "2":
        nump = int(input("Please input the number of points you wish to generate:"))
        lr = input("Please input the learning rate you wish to use(Leave blank for 0.01):")
        if lr == "":
            lr = 0.01
        else:
            lr = float(lr)
        gradient = input("Please input the gradient of the line you wish to plot(Leave blank for 2):")
        if gradient == "":
            gradient = 2
        else:
            gradient = float(gradient)
        intercept = input("Please input the intercept of the line you wish to plot(Leave blank for 3):")
        if intercept == "":
            intercept = 3
        else:
            intercept = float(intercept)
        bias = input("Please input the bias of the perceptron(Leave blank for 2):")
        if bias == "":
            bias = 2
        else:
            bias = int(bias)
        iterations = input("Please input the number of iterations you wish to use(Leave blank for 100001):")
        if iterations == "":
            iterations = 100001
        else:
            iterations = int(iterations)
        print("Generating points...")
        line_plotting_perceptron(nump,lr,gradient,intercept,bias,iterations)
    case "3":
        print("Exiting Mobile AI...")
    case _:
        print("Invalid input")
        exit()  



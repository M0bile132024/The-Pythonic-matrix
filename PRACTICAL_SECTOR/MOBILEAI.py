#MOBILE.AI
#Ver 1
#Author:M0bile132022
#A test project using machine learning(kind of)


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
for i in range(len(input_list)):
    input_list[i] = input_list[i] * weights[i]
weighted_sum = sum(input_list)
if weighted_sum >= threshold:
    print("You should go to the concert")
else:
    print("You should not go to the concert")
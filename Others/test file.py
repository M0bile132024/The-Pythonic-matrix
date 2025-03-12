#test file
'''
Create a Python program that manages student grades using subroutines. The program should include subroutines for adding 3 grades, 
calculating the average grade, finding the overall total, finding the highest grade, and finding the lowest grade. 
The program should have a menu system that takes the user to the correct subroutine and then completes that task


'''
name = input("What is your name? ")
def greet_user():
    global name
    print("Hello", name)
    age = input("How old are you? ")
    print("You are", age, "years old")
    colour = input("What is your favourite colour? ")
    print("Your favourite colour is", colour)
def add_grades():
    global grade1, grade2, grade3
    grade1 = int(input("Enter grade 1: "))
    grade2 = int(input("Enter grade 2: "))
    grade3 = int(input("Enter grade 3: "))
    print("Grades have been added")

def average_grade():
    global grade1, grade2, grade3
    average = (grade1 + grade2 + grade3) / 3
    print("The average grade is", average)

def overall_total():
    global grade1, grade2, grade3
    total = grade1 + grade2 + grade3
    print("The overall total is", total)

def highest_grade():
    global grade1, grade2, grade3
    highest = max(grade1, grade2, grade3)
    print("The highest grade is", highest)

def lowest_grade():
    global grade1, grade2, grade3
    lowest = min(grade1, grade2, grade3)
    print("The lowest grade is", lowest)


greet_user()
grade1 = 0
grade2 = 0
grade3 = 0

while True:
    print("""1. Add grades
    2. Calculate average grade
    3. Find overall total
    4. Find highest grade
    5. Find lowest grade""")
    option = int(input("Enter an option: "))
    if option == 1:
        add_grades()
    elif option == 2:
        average_grade()
    elif option == 3:
        overall_total()
    elif option == 4:
        highest_grade()
    elif option == 5:
        lowest_grade()
    else:
        print("Invalid option")

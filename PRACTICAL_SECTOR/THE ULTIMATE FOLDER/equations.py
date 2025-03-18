#python code to solve simultanous equation test
from sympy import symbols, Eq, solve, parse_expr
from THE_ULTIMATE_CALC import copy_to_keyboard,copy_to_keyboard_true
'''
This code is used to solve simultanous equations'''

# Define the variables
def simultanous_calc():
    x, y = symbols('x y')
    print("Note:Type unknown values as 'number*variable' for example 2*x")
# Take input from the user
    equation1 = input("Enter the frist expression: ")
    answer1 = input("Enter the answer of the first expression: ")
    equation2 = input("Enter the second expression: ")
    answer2 = input("Enter the answer of the second expression: ")
    eq1 = Eq(parse_expr(equation1), int(answer1))
    eq2 = Eq(parse_expr(equation2), int(answer2))
    solution = solve((eq1, eq2), (x, y))
    print(f"x = {solution[x]}, y = {solution[y]}")
    copy_to_keyboard(f"x = {solution[x]}, y = {solution[y]}",copy_to_keyboard_true)
    

#simultanous_calc()
def equation_calc():
    x, y = symbols('x y')
    print("Note:Type unknown values as 'number*variable' for example 2*x")
# Take input from the user
    equation = input("Enter the expression: ")
    answer = input("Enter the answer of the expression: ")
    eq = Eq(parse_expr(equation), int(answer))
    solution = solve(eq, (x, y))
    print(f"x = {solution[x]}, y = {solution[y]}")
    copy_to_keyboard(f"x = {solution[x]}, y = {solution[y]}",copy_to_keyboard_true)
#equation_calc()
    
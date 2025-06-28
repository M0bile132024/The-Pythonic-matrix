#equations.py
#By: M0bile132022
#Date: 28-06-2025
#Version: 1.2
# This libary is used to solve equations, simultanous equations, quadratic factoriser and changing the subject of an equation.
from sympy import symbols, Eq, solve, parse_expr
import pyperclip
def copy_to_keyboard(text,true_or_false):
    if true_or_false == True:    
        pyperclip.copy(text)
        print("Text copied sucessfully")
    else:
        return
copy_to_keyboard_true = False

def simultanous_calc():
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    print("Note:Type unknown values as 'number*variable' for example 2*x")
# Take input from the user
    equation_list = []
    answer_list = []
    number_of_equations = int(input("Enter the number of equations you want to simultanously solve: "))
    #check if invalid number of equations is entered
    if number_of_equations < 2:
        print("Invalid number of equations. Please enter a number greater than or equal to 2.")
        return

    for i in range(number_of_equations):
        equation1 = input("Enter the frist expression: ")
        answer1 = input("Enter the answer of the first expression: ")
        equation_list.append(equation1)
        answer_list.append(answer1)
    #create a list of equations
    eq_list = []
    for i in range(number_of_equations):
        eq1 = Eq(parse_expr(equation_list[i]), int(answer_list[i]))
        eq_list.append(eq1)
    solution = solve((eq_list), (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
    print(solution)
    copy_to_keyboard(solution,copy_to_keyboard_true)
  

#simultanous_calc()
def equation_calc():
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    print("Note:Type unknown values as 'number*variable' for example 2*x")
# Take input from the user
    equation_list = []
    answer_list = []
    number_of_equations = int(input("Enter the number of equations you want to solve: "))
    #check if invalid number of equations is entered
    

    for i in range(number_of_equations):
        equation1 = input("Enter the frist expression: ")
        answer1 = input("Enter the answer of the first expression: ")
        equation_list.append(equation1)
        answer_list.append(answer1)
    #create a list of equations
    eq_list = []
    for i in range(number_of_equations):
        eq1 = Eq(parse_expr(equation_list[i]), int(answer_list[i]))
        eq_list.append(eq1)
    solution_list = []
    for i in range(len(eq_list)):
        solution = solve((eq_list[i]), (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
        #Remove the , sign from the solution string
        solution = solution.replace(",", "")
        #Remove the variable names from the solution string
        solution = solution.replace("a", "").replace("b", "").replace("c", "").replace("d", "").replace("e", "").replace("f", "").replace("g", "").replace("h", "").replace("i", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "").replace("o", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("t", "").replace("u", "").replace("v", "").replace("w", "").replace("x", "").replace("y", "").replace("z", "")
        solution_list.append(solution)
    for i in range(len(solution_list)):
        solution = solution_list[i]
        print(f"Solution for equation {i+1}: {solution}")
    copy_to_keyboard(solution_list,copy_to_keyboard_true)
   
#equation_calc()
def quadratic_factoriser_calc():
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    print("Note:Type unknown values as 'number*variable' for example 2*x")
# Take input from the user
#quadratic_factoriser_calc()
def changing_the_subject():
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    print("Note:Type unknown values as 'number*variable' for example 2*x")
# Take input from the user
    equation_list = []
    answer_list = []
    subject_list = []
    number_of_equations = int(input("Enter the number of equations you want to change the subject of: "))
    #check if invalid number of equations is entered
    

    for incrementer in range(number_of_equations):
        equation1 = input("Enter the frist expression: ")
        answer1 = input("Enter the answer of the first expression: ")
        subject = input("Enter the new subject of the equation: ")
        equation_list.append(equation1)
        answer_list.append(answer1)
        subject_list.append(subject)
    eq_list = []
    for incrementer in range(number_of_equations):
        eq1 = Eq(parse_expr(equation_list[incrementer]), int(answer_list[incrementer]))
        eq_list.append(eq1)
    solution_list = []
    for incrementer in range(len(eq_list)):
        solution = solve((eq_list[incrementer]), parse_expr(subject_list[incrementer]))
        #Remove the , sign from the solution string
        solution = str(solution).replace(",", "")
        #Remove the variable names from the solution string
        solution = solution.replace("a", "").replace("b", "").replace("c", "").replace("d", "").replace("e", "").replace("f", "").replace("g", "").replace("h", "").replace("i", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "").replace("o", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("t", "").replace("u", "").replace("v", "").replace("w", "").replace("x", "").replace("y", "").replace("z", "")
        solution_list.append(solution)
    for incrementer in range(len(solution_list)):
        solution = solution_list[incrementer]
        print(f"Solution for equation {incrementer+1}: {solution}")
    copy_to_keyboard(solution_list,copy_to_keyboard_true)
# Uncomment the function you want to use

    
#changing_the_subject()
def expanding_brackets(equation):
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    # This function expands the brackets in the given equation
    expanded_equation = parse_expr(equation).expand()
    return str(expanded_equation) 
#expanding_brackets("2*(x+3) + 4*(y-5)")  # Example usage of expanding brackets function
def factorising(equation):
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    # This function factorises the given equation
    factorised_equation = parse_expr(equation).factor()
    return str(factorised_equation)
#factorising("x**2 + 5*x + 6")  # Example usage of factorising function  


#Class formatting
class EquationSolver:
    def __init__(self, copy_to_keyboard=False):
        self.copy_to_keyboard = copy_to_keyboard

    def copy_to_keyboard(self, text):
        if self.copy_to_keyboard:
            pyperclip.copy(text)
            print("Text copied successfully")
    
    def simultanous_calc(self):
        simultanous_calc()

    def equation_calc(self):
        equation_calc()

    def quadratic_factoriser_calc(self):
        quadratic_factoriser_calc()

    def changing_the_subject(self):
        changing_the_subject()
    def expanding_brackets(self, equation):
        return expanding_brackets(equation)
    def factorising(self, equation):
        return factorising(equation)
    def solve(self, equation_type):
        if equation_type == "simultanous":
            self.simultanous_calc()
        elif equation_type == "equation":
            self.equation_calc()
        elif equation_type == "quadratic_factoriser":
            self.quadratic_factoriser_calc()
        elif equation_type == "changing_the_subject":
            self.changing_the_subject()
        elif equation_type == "expanding_brackets":
            equation = input("Enter the equation to expand: ")
            result = self.expanding_brackets(equation)
            print(f"Expanded equation: {result}")
            self.copy_to_keyboard(result)
        elif equation_type == "factorising":
            equation = input("Enter the equation to factorise: ")
            result = self.factorising(equation)
            print(f"Factorised equation: {result}")
            self.copy_to_keyboard(result)
        else:
            print("Invalid equation type. Please choose from 'simultanous', 'equation', 'quadratic_factoriser', 'changing_the_subject', 'expanding_brackets', or 'factorising'.")
# Example usage:
# solver = EquationSolver(copy_to_keyboard=True)
# solver.solve("simultanous")
# solver.solve("equation")
# solver.solve("quadratic_factoriser")
# solver.solve("changing_the_subject")
# solver.solve("invalid_type")  # This will print an error message
# solver = EquationSolver(copy_to_keyboard=True)
# solver.simultanous_calc()
# solver.equation_calc()
# solver.quadratic_factoriser_calc()
# solver.changing_the_subject()


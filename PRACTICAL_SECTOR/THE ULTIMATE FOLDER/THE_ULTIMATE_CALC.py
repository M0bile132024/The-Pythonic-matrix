   
#THE ULTIMATE CALC 
#By: @M0bile132022
#Date: 19/10/25
#Version: 2.60
#Milestones:
#UPDATE 2.0:01/05/2025
'''Description: This is a ULTIMATE calculator that can perform ULTIMATE operations such as SA:VOL, 
PHYSIC EQUATIONS, 
pythagoras therom,
Perimiter/Area,
The basics,
Ordering,
Scale factors,
Decimal to fraction to percentage conversions,
Planetary time and arcs/sectors/chords(included in others(in a future update)),
intrest
trigomentry
Standard form and more!
'''
#Note: This is a calculator that can do a lot of things, so don't be surprised if you see a lot of code.
import math
import time
import os
import fractions
import pyperclip
import equations as eq
import sympy as sp

def operation_dialogue():
    print("Please select an operation:")
    print("1. Surface Area")
    print("2. Volume")
    print("3. Both(SA:VOL ratio)")
    operation = int(input("Enter the number of the operation you want to perform: "))
    return operation
def twod_operation_dialogue(shape):
    print(f"You have selected the {shape}!")
    print("Please select an operation:")
    print("1. Perimiter")
    print("2. Area")
    print("3. Both(P:A ratio)")
    operation = int(input("Enter the number of the operation you want to perform: "))
    return operation
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)
def copy_to_keyboard(text,true_or_false):
    if true_or_false == True:    
        pyperclip.copy(text)
        print("Text copied sucessfully")
    else:
        return
def reciprocal(number):
    if number == 0:
        return "N/A(Cannot find reciprocal of zero)"
    return 1 / number
def subtract_list(values):
    result = values[0]
    for value in values[1:]:
        result -= value
    return result
def multiply_list(values):
    result = 1
    for value in values[1:]:
        result *= value
    return result
def divide_list(values):
    result = values[0]
    for value in values[1:]:
        result /= value
    return result
def calc(name,options,operation_or_calc):
    print(f"You have selected {name}!" if operation_or_calc == 1 else f"Welcome to the {name} category!")
    print("Please select an operation:" if operation_or_calc == 1 else "Please select a calculation:" if operation_or_calc == 2 else "Please select a method:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    operation = int(input("Enter the number of the operation you want to perform: "))
    return operation
#3rd party subroutines
#yzfargo/yu https://github.com/yzfargo/yu
def calculate_displacement(initial_velocity, acceleration, time):
    """Calculates the displacement using the SVT equation."""
    displacement = initial_velocity * time + 0.5 * acceleration * time**2
    return displacement

def calculate_final_velocity(initial_velocity, acceleration, time):
    """Calculates the final velocity using the SVT equation."""
    final_velocity = initial_velocity + acceleration * time
    return final_velocity

def calculate_time(initial_velocity, final_velocity, acceleration):
    """Calculates the time using the SVT equation."""
    time = (final_velocity - initial_velocity) / acceleration
    return time
def simplify_surd(expression):
    """Simplifies a surd expression."""
    simplified = sp.simplify(sp.sqrt(sp.sympify(expression)))
    return simplified
       


# Example usage
#print(reciprocal(5))  # Output: 0.2

#Alt functions
def find_x_intercept(m, b):
    if m == 0:
        print("The slope (m) cannot be zero for a valid x-intercept.")
        return None
    x_intercept = -b / m
    return x_intercept

file_path = os.path.abspath(__file__)
file_size = os.path.getsize(file_path)
version = 2.60
line_count = count_lines(file_path)
lenght_units = "Line units"
angle_units = "Angle units"
volume_units = "Cubic units"
area_units = "Area units"
money_units = "Money units"
time_units = "Time units"
try:
    copy_to_keyboard_true = True
    copy_to_keyboard("Test",copy_to_keyboard_true)
except:
    print("Pyperclip not installed or not working,copy to clipboard function has been disabled.\n\n\n")
    copy_to_keyboard_true = False



if __name__ == "__main__": 
    while True:
        print(f"Welcome to the ULTIMATE calc Ver {version}!")
        print("""Please select a category:
        1. Surface Area and Volume(SA:VOL ratio)
        2. Pythagoras therom
        3. Perimiter and Area(P:A ratio)
        4. Standard form
        5. The Basics
        6. Ordering/Mass operations
        7. Scale factors
        8. Decimal to fraction to percentage conversions
        9. Intrest
        10. Trigomentry
        11. Lines
        12. Equations(beta)
        13. Circles/Spheres
        14. Others(coming soon)
        15. Legal/Other Info on ULTIMATE CALC™
        16. Settings
        More functions are coming soon!!!!!""")
        category = int(input("Enter the number of the category you want to use: "))
        

        if category == 1:
            print("Welcome to the Surface Area and Volume category!")
            print("""Please select a shape:
            1. Cube
            2. Rectangular Prism
            3. Cylinder
            4. Cone
            5. Sphere
            6. Hemisphere
            6. Other prisms(required to know cross section area)
            7. Other pyrimids(required to know base area)
            """)
            shape = int(input("Enter the number of the shape you want to use: "))
            if shape == 1:
                print("You have selected the Cube!")
                operation = operation_dialogue()
                if operation == 1:
                    print("You have selected Surface Area!")
                    side = float(input("Enter the side length of the cube: "))
                    sa = 6 * (side ** 2)
                    print(f"The surface area of the cube is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    side = float(input("Enter the side length of the cube: "))
                    vol = side ** 3
                    print(f"The volume of the cube is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    side = float(input("Enter the side length of the cube: "))
                    sa = 6 * (side ** 2)
                    vol = side ** 3
                    ratio = sa / vol
                    print(f"The surface area of the cube is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                    print(f"The volume of the cube is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                    print(f"The SA:VOL ratio of the cube is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 2:
                print("You have selected the Rectangular Prism!")
                operation = operation_dialogue()
                if operation == 1:
                    print("You have selected Surface Area!")
                    length = float(input("Enter the length of the rectangular prism: "))
                    width = float(input("Enter the width of the rectangular prism: "))
                    height = float(input("Enter the height of the rectangular prism: "))
                    sa = 2 * ((length * width) + (width * height) + (height * length))
                    print(f"The surface area of the rectangular prism is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    length = float(input("Enter the length of the rectangular prism: "))
                    width = float(input("Enter the width of the rectangular prism: "))
                    height = float(input("Enter the height of the rectangular prism: "))
                    vol = length * width * height
                    print(f"The volume of the rectangular prism is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    length = float(input("Enter the length of the rectangular prism: "))
                    width = float(input("Enter the width of the rectangular prism: "))
                    height = float(input("Enter the height of the rectangular prism: "))
                    sa = 2 * ((length * width) + (width * height) + (height * length))
                    vol = length * width * height
                    ratio = sa / vol
                    print(f"The surface area of the rectangular prism is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                    print(f"The volume of the rectangular prism is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                    print(f"The SA:VOL ratio of the rectangular prism is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 3:
                print("You have selected the Cylinder!")
                
                operation = operation_dialogue()
                pi = math.pi
                if operation == 1:
                    print("You have selected Surface Area!")
                    radius = float(input("Enter the radius of the cylinder: "))
                    height = float(input("Enter the height of the cylinder: "))
                    sa = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
                    terms_of_pi = sa/pi
                    print(f"The surface area of the cylinder is {sa} {area_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{sa},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    radius = float(input("Enter the radius of the cylinder: "))
                    height = float(input("Enter the height of the cylinder: "))
                    vol = pi * (radius ** 2) * height
                    terms_of_pi = vol/pi
                    print(f"The volume of the cylinder is {vol} {volume_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{vol},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the cylinder: "))
                    height = float(input("Enter the height of the cylinder: "))
                    sa = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
                    sa_terms_of_pi = sa/pi
                    vol = pi * (radius ** 2) * height
                    vol_terms_of_pi = vol/pi
                    ratio = sa / vol
                    print(f"The surface area of the cylinder is {sa} {area_units}(Terms of Pi={sa_terms_of_pi}pi).")
                    copy_to_keyboard(f"{sa},{sa_terms_of_pi}",copy_to_keyboard_true)
                    print(f"The volume of the cylinder is {vol} {volume_units}(Terms of Pi={vol_terms_of_pi}pi).")
                    copy_to_keyboard(f"{vol},{vol_terms_of_pi}",copy_to_keyboard_true)
                    print(f"The SA:VOL ratio of the cylinder is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 4:
                print("You have selected the Cone!")
                operation = operation_dialogue()   
                pi = math.pi
                if operation == 1:
                    print("You have selected Surface Area!")
                    radius = float(input("Enter the radius of the cone: "))
                    slant_height = float(input("Enter the slant height of the cone: "))
                    sa = pi * radius * (radius + slant_height)
                    terms_of_pi = sa/pi
                    print(f"The surface area of the cone is {sa} {area_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{sa},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    radius = float(input("Enter the radius of the cone: "))
                    height = float(input("Enter the height of the cone: "))
                    vol = (1/3) * pi * (radius ** 2) * height
                    terms_of_pi = vol/pi
                    print(f"The volume of the cone is {vol} {volume_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{vol},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the cone: "))
                    height = float(input("Enter the height of the cone: "))
                    slant_height = float(input("Enter the slant height:"))
                    sa = pi * radius * (radius + slant_height)
                    vol = (1/3) * pi * (radius ** 2) * height
                    ratio = sa / vol
                    sa_terms_of_pi = sa/pi
                    vol_terms_of_pi = vol/pi
                    print(f"The surface area of the cone is {sa} {area_units}(Terms of Pi={sa_terms_of_pi}pi).")
                    print(f"The volume of the cone is {vol} {volume_units}(Terms of Pi={vol_terms_of_pi}pi).")
                    print(f"The SA:VOL ratio of the cone is {ratio}.")
                    copy_to_keyboard(f"{sa},{vol},{ratio},{sa_terms_of_pi},{vol_terms_of_pi}",copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 5:
                print("You have selected the Sphere!")
                operation = operation_dialogue()
                pi = math.pi
                if operation == 1:
                    print("You have selected Surface Area!")
                    radius = float(input("Enter the radius of the sphere: "))
                    sa = 4 * pi * (radius ** 2)
                    terms_of_pi = sa/pi
                    print(f"The surface area of the sphere is {area_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{sa},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    radius = float(input("Enter the radius of the sphere: "))
                    vol = (4/3) * pi * (radius ** 3)
                    terms_of_pi = vol/pi
                    print(f"The volume of the sphere is {vol} {volume_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{vol},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the sphere: "))
                    sa = 4 * pi * (radius ** 2)
                    vol = (4/3) * pi * (radius ** 3)
                    ratio = sa / vol
                    sa_terms_of_pi = sa/pi
                    vol_terms_of_pi = vol/pi
                    print(f"The surface area of the sphere is {sa} {area_units}(Terms of Pi={sa_terms_of_pi}pi).")
                    print(f"The volume of the sphere is {vol} {volume_units}(Terms of Pi={vol_terms_of_pi}pi).")
                    print(f"The SA:VOL ratio of the sphere is {ratio}.")
                    copy_to_keyboard(f"{sa},{vol},{ratio},{sa_terms_of_pi},{vol_terms_of_pi}",copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 6:
                #Total Surface Area (TSA) = 2 × Base Area + Base Perimeter × Height.
                print("You have selected the Other prisms!")
                operation = operation_dialogue()
                if operation == 1:
                    print("You have selected Surface Area!")
                    base_area = float(input("Enter the cross section area of the prism: "))
                    base_perimeter = float(input("Enter the perimeter of the prism: "))
                    height = float(input("Enter the height of the prism: "))
                    sa = (2 * base_area) + (base_perimeter * height)
                    print(f"The surface area of the prism is {sa} {area_units}.")#
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")   
                    area = float(input("Enter the cross section area of the prism: "))
                    height = float(input("Enter the height of the prism: "))
                    vol = area * height
                    print(f"The volume of the prism is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
            elif shape == 7:
                print("You have selected the Other pyrimids!")
                operation = operation_dialogue()
                if operation == 1:
                    print("You have selected Surface Area!")
                    base_area = float(input("Enter the base area of the pyrimid: "))
                    base_perimeter = float(input("Enter the perimeter of the pyrimid: "))
                    slant_height= float(input("Enter the slant height of the pyrimid: "))
                    sa = base_area + ((1/2) * base_perimeter * slant_height)
                    print(f"The surface area of the pyrimid is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    area = float(input("Enter the base area of the pyrimid: "))
                    height = float(input("Enter the height of the pyrimid: "))
                    vol = (1/3) * area * height
                    print(f"The volume of the pyrimid is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                
            else:
                print("Invalid shape!Please try again.")
                continue 
        elif category == 2:
            print("Welcome to the Pythagoras therom category!")
            print("Please select an operation:")
            print("""1. Calculate the hypotenuse
            2. Calculate one of the other sides""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Calculate the hypotenuse!")
                side1 = float(input("Enter the length of the first side: "))
                side2 = float(input("Enter the length of the second side: "))
                hypotenuse = math.sqrt((side1 ** 2) + (side2 ** 2))
                print(f"The length of the hypotenuse is {hypotenuse} {lenght_units}.")
                copy_to_keyboard(hypotenuse,copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Calculate one of the other sides!")
                side1 = float(input("Enter the length of the hypotnuse: "))
                side2 = float(input("Enter the length of the side known: "))
                unknown_side = math.sqrt((side1 ** 2) - (side2 ** 2))
                print(f"The length of the unknown side is {unknown_side} {lenght_units}.")
                copy_to_keyboard(unknown_side,copy_to_keyboard_true)
            else:
                print("Invalid operation!Please try again.")
                continue 
        elif category == 3:
            print("Welcome to the Perimiter and Area category!")
            print("""Please select a shape:
            1. Square
            2. Rectangle/Pallelogram
            3. Triangle
            4. Circle
            5. Semicircle
            6. Trapezium
            7. Kite(coming 2.1)
            8. Rhombus(coming 2.1)
            9. Other polygons(coming 2.1)""")
            shape = int(input("Enter the number of the shape you want to use: "))
            if shape == 1:
                operation = twod_operation_dialogue("Square")
                if operation == 1:
                    print("You have selected Perimiter!")
                    side = float(input("Enter the length of a side of the square: "))
                    perimiter = 4 * side
                    print(f"The perimiter of the square is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    side = float(input("Enter the length of a side of the square: "))
                    area = side ** 2
                    print(f"The area of the square is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    side = float(input("Enter the length of a side of the square: "))
                    perimiter = 4 * side
                    area = side ** 2
                    ratio = perimiter / area
                    print(f"The perimiter of the square is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                    print(f"The area of the square is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                    print(f"The P:A ratio of the square is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 2:
                operation = twod_operation_dialogue("Rectangle")
                if operation == 1:
                    print("You have selected Perimiter!")
                    length = float(input("Enter the length of the rectangle: "))
                    width = float(input("Enter the width of the rectangle: "))
                    perimiter = 2 * (length + width)
                    print(f"The perimiter of the rectangle is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    length = float(input("Enter the length of the rectangle: "))
                    width = float(input("Enter the width of the rectangle: "))
                    area = length * width
                    print(f"The area of the rectangle is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    length = float(input("Enter the length of the rectangle: "))
                    width = float(input("Enter the width of the rectangle: "))
                    perimiter = 2 * (length + width)    
                    area = length * width
                    ratio = perimiter / area
                    print(f"The perimiter of the rectangle is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                    print(f"The area of the rectangle is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                    print(f"The P:A ratio of the rectangle is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 3:
                operation = twod_operation_dialogue("Triangle")
                if operation == 1:
                    print("You have selected Perimiter!")
                    side1 = float(input("Enter the length of the first side: "))
                    side2 = float(input("Enter the length of the second side: "))
                    side3 = float(input("Enter the length of the third side: "))
                    perimiter = side1 + side2 + side3
                    print(f"The perimiter of the triangle is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    base = float(input("Enter the length of the base of the triangle: "))
                    height = float(input("Enter the height of the triangle: "))
                    area = (1/2) * base * height
                    print(f"The area of the triangle is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    side1 = float(input("Enter the length of the first side: "))
                    side2 = float(input("Enter the length of the second side: "))
                    side3 = float(input("Enter the length of the third side: "))
                    perimiter = side1 + side2 + side3
                    base = float(input("Enter the length of the base of the triangle: "))
                    height = float(input("Enter the height of the triangle: "))
                    area = (1/2) * base * height
                    ratio = perimiter / area
                    print(f"The perimiter of the triangle is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                    print(f"The area of the triangle is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                    print(f"The P:A ratio of the triangle is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue 
            elif shape == 4:
                operation = twod_operation_dialogue("Circle")
                pi = math.pi
                if operation == 1:
                    print("You have selected Perimiter!")
                    radius = float(input("Enter the radius of the circle: "))
                    perimiter = 2 * pi * radius
                    terms_of_pi = perimiter/pi
                    print(f"The perimiter of the circle is {perimiter} {lenght_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{perimiter},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    radius = float(input("Enter the radius of the circle: "))
                    area = pi * (radius ** 2)
                    terms_of_pi = area/pi
                    print(f"The area of the circle is {area} {area_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{area},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the circle: "))
                    perimiter = 2 * pi * radius
                    area = pi * (radius ** 2)
                    ratio = perimiter / area
                    perimiter_terms_of_pi = perimiter/pi
                    area_terms_of_pi = area/pi
                    print(f"The perimiter of the circle is {perimiter} {lenght_units}(Terms of Pi={perimiter_terms_of_pi}pi).")
                    print(f"The area of the circle is {area} {area_units}(Terms of Pi={area_terms_of_pi}pi).")
                    print(f"The P:A ratio of the circle is {ratio}.")
                    copy_to_keyboard(f"{perimiter},{area},{ratio},{perimiter_terms_of_pi},{area_terms_of_pi}",copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif shape == 5:
                print("You have selected the Semicircle!")
                operation = twod_operation_dialogue("Semicircle")
                pi = math.pi
                if operation == 1:
                    print("You have selected Perimiter!")
                    radius = float(input("Enter the radius of the semicircle: "))
                    perimiter = (pi * radius) + (2 * radius)
                    terms_of_pi = perimiter/pi
                    print(f"The perimiter of the semicircle is {perimiter} {lenght_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{perimiter},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    radius = float(input("Enter the radius of the semicircle: "))
                    area = (1/2) * pi * (radius ** 2)
                    terms_of_pi = area/pi
                    print(f"The area of the semicircle is {area} {area_units}(Terms of Pi={terms_of_pi}pi).")
                    copy_to_keyboard(f"{area},{terms_of_pi}",copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the semicircle: "))
                    perimiter = (pi * radius) + (2 * radius)
                    area = (1/2) * pi * (radius ** 2)
                    ratio = perimiter / area
                    perimiter_terms_of_pi = perimiter/pi
                    area_terms_of_pi = area/pi
                    print(f"The perimiter of the semicircle is {perimiter} {lenght_units}(Terms of Pi={perimiter_terms_of_pi}pi).")
                    print(f"The area of the semicircle is {area} {area_units}(Terms of Pi={area_terms_of_pi}pi).")
                    print(f"The P:A ratio of the semicircle is {ratio}.")
                    copy_to_keyboard(f"{perimiter},{area},{ratio},{perimiter_terms_of_pi},{area_terms_of_pi}",copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif shape == 6:
                print("You have selected the Trapezium!")
                operation = twod_operation_dialogue("Trapezium")
                if operation == 1:
                    print("You have selected Perimiter!")
                    a = float(input("Enter the length of the top side(a): "))
                    b = float(input("Enter the length of the bottom side(b): "))
                    c = float(input("Enter the length of the left side(c): "))
                    d = float(input("Enter the length of the right side(d): "))
                    perimiter = a + b + c + d
                    print(f"The perimiter of the trapezium is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    a = float(input("Enter the length of the top side(a): "))
                    b = float(input("Enter the length of the bottom side(b): "))
                    height = float(input("Enter the height of the trapezium: "))
                    area = (1/2) * (a + b) * height
                    print(f"The area of the trapezium is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    a = float(input("Enter the length of the top side(a): "))
                    b = float(input("Enter the length of the bottom side(b): "))
                    c = float(input("Enter the length of the left side(c): "))
                    d = float(input("Enter the length of the right side(d): "))
                    perimiter = a + b + c + d
                    height = float(input("Enter the height of the trapezium: "))
                    area = (1/2) * (a + b) * height
                    print(f"The perimiter of the trapezium is {perimiter} {lenght_units}.")
                    print(f"The area of the trapezium is {area} {area_units}.")
                    ratio = perimiter / area
                    print(f"The P:A ratio of the trapezium is {ratio}.")
                    copy_to_keyboard(f"{perimiter},{area},{ratio}",copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
            else:
                print("Invalid shape!Please try again.")
                continue 
        elif category == 4:
            print("Welcome to the Standard form category!")
            print("Please select an operation:")
            print("""1. Convert to standard form
    2. Convert from standard form
    Please note this calc only supports ENG notation""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Convert to standard form!")
                number = float(input("Enter the number you want to convert to standard form: "))
                standard_form = f"{number:.2e}"
                print(f"The number in standard form is {standard_form}.")
                copy_to_keyboard(standard_form,copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Convert from standard form!")
                try:
                    number = input("Enter the number you want to convert from standard form(ENG notation): ")
                    number = float(number)
                    print(f"The number in standard form is {number}.")
                    copy_to_keyboard(number,copy_to_keyboard_true)
                except:
                    print("Invalid notation!Please try again,using ENG Noation.")
                    continue 
            else:
                print("Invalid operation!Please try again.")
                continue 
        elif category == 5:
            print("Welcome to the Basics category(of course....)!")
            print("Please select an operation:")
            print("""1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponents
6. Square/cube/any root
7. Bring up "The Lists"....
8. Sin()
9. Cos()
10. Tan()
11. Terms of Pi()
12. Recipicoral()""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Addition!")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 + num2
                print(f"The sum of the two numbers is {result}.")
                copy_to_keyboard(result, copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Subtraction!")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 - num2
                print(f"The difference of the two numbers is {result}.")
                copy_to_keyboard(result, copy_to_keyboard_true)
            elif operation == 3:
                print("You have selected Multiplication!")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 * num2
                print(f"The product of the two numbers is {result}.")
                copy_to_keyboard(result, copy_to_keyboard_true)
            elif operation == 4:
                print("You have selected Division!")
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 / num2
                print(f"The quotient of the two numbers is {result}.")
                copy_to_keyboard(result, copy_to_keyboard_true)
            elif operation == 5:
                print("You have selected Exponents!")
                num1 = float(input("Enter the base number: "))
                num2 = float(input("Enter the exponent: "))
                result = num1 ** num2
                print(f"The result of the exponent is {result}.")
                copy_to_keyboard(result, copy_to_keyboard_true)
            elif operation == 6:
                print("You have selected Square/Cube/Any root!")
                num = float(input("Enter the number you want to find the root of: "))
                root = float(input("Enter the root you want to find of the number: "))
                result = num ** (1/root)
                print(f"The {root} root of the number is {result}.")
                copy_to_keyboard(result, copy_to_keyboard_true)
            elif operation == 7:
                print("Multiplication grid:")
                # Define the size of the times table grid
                size = int(input("Please input the size of multiplication grid: "))

                # Print the header row
                print("    ", end="")
                for i in range(1, size + 1):
                    print(f"{i:4}", end="")
                print()

                # Print the separator line
                print("    " + "-" * (size * 4))

                # Print the times table grid
                for i in range(1, size + 1):
                    print(f"{i:2} |", end="")
                    for j in range(1, size + 1):
                        print(f"{i * j:4}", end="")
                    print()
                print("Standard list of sqaures and cubes:")
                print("Number |",end="")
                print("Squares |",end="")
                print("Cubes |")

                for i in range(1,21):
                    print(i,i**2,i**3,sep="   |")
            elif operation == 8:
                print("You have selected Sin()!")
                num = float(input("Enter the number you want to find the sin of: "))
                sin = math.sin(num)
                print(f"The sin of the number is {sin}.")
                copy_to_keyboard(sin, copy_to_keyboard_true)
            elif operation == 9:
                print("You have selected Cos()!")
                num = float(input("Enter the number you want to find the cos of: "))
                cos = math.cos(num)
                print(f"The cos of the number is {cos}.")
                copy_to_keyboard(cos, copy_to_keyboard_true)
            elif operation == 10:
                print("You have selected Tan()!")
                num = float(input("Enter the number you want to find the tan of: "))
                tan = math.tan(num)
                print(f"The tan of the number is {tan}.")
                copy_to_keyboard(tan, copy_to_keyboard_true)
            elif operation == 11:
                print("You have selected Terms Of Pi()!")
                pi = math.pi
                num = float(input("Enter the number you want to find the terms of pi of: "))
                terms_of_pi = num / pi
                print(f"The terms of pi of the number is {terms_of_pi}pi.")
                copy_to_keyboard(f"{terms_of_pi}pi", copy_to_keyboard_true)
            elif operation == 12:
                print("You have selected Recipicoral()")
                num = float(input("Enter the number you want to find the recipicoral of: "))
                reciprocal_num = reciprocal(num)
                print(f"The recipicoral of {num} is {reciprocal_num}")
                copy_to_keyboard(reciprocal_num,copy_to_keyboard_true)

            else:
                print("Invalid operation!Please try again.")
                continue 
        elif category == 6:
            print("Welcome to the Ordering/Mass operations category!")
            print("Please select an operation:")
            print("""1. Ascending order
2. Descending order
3. Mass addition
4. Mass subtraction
5. Mass multiplication
6. Mass division
7. Finding the upper and lower bounds of a rounded number
8. Finding the upper and lower bounds of a number rounded to significant figures
9. Finding the upper and lower bounds of a truncated number
        """)
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Ascending order!")
                ordering_list = []
                while True:
                    number = input("Enter a number to add to the list or type 'done' to finish: ")
                    if number == "done":
                        break
                    else:
                        number = float(number)
                        ordering_list.append(number)
                ordering_list.sort()
                print(f"The numbers in ascending order are {ordering_list}.",sep=",")
                copy_to_keyboard(ordering_list, copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Descending order!")
                ordering_list = []
                while True:
                    number = input("Enter a number to add to the list or type 'done' to finish: ")
                    if number == "done":
                        break
                    else:
                        number = float(number)
                        ordering_list.append(number)
                ordering_list.sort(reverse=True)
                print(f"The numbers in descending order are {ordering_list}.",sep=",")
                copy_to_keyboard(ordering_list, copy_to_keyboard_true)
            elif operation == 3:
                print("You have selected Mass addition!")
                ordering_list = []
                while True:
                    number = input("Enter a number to add to the list or type 'done' to finish: ")
                    if number == "done":
                        break
                    else:
                        number = float(number)
                        ordering_list.append(number)
                try:    
                    sum_of_numbers = sum(ordering_list) 
                    print(f"The sum of the numbers are {sum_of_numbers}.")
                    copy_to_keyboard(sum_of_numbers, copy_to_keyboard_true)
                except:
                    print("Invalid values!Please try again.")
                    continue
            elif operation == 4:
                print("You have selected Mass subtraction!")
                ordering_list = []
                while True:
                    number = input("Enter a number to add to the list or type 'done' to finish: ")
                    if number == "done":
                        break
                    else:
                        number = float(number)
                        ordering_list.append(number)
                try:
                    print(f"The difference of the numbers is {subtract_list(ordering_list)}.")
                    copy_to_keyboard(subtract_list(ordering_list), copy_to_keyboard_true)
                except:
                    print("Invalid values!Please try again.")
                    continue
            elif operation == 5:
                print("You have selected Mass multiplication!")
                ordering_list = []
                while True:
                    number = input("Enter a number to add to the list or type 'done' to finish: ")
                    if number == "done":
                        break
                    else:
                        number = float(number)
                        ordering_list.append(number)
                try:    
                    print(f"The product of the numbers is {multiply_list(ordering_list)}.")
                    copy_to_keyboard(multiply_list(ordering_list), copy_to_keyboard_true)
                except:
                    print("Invalid values!Please try again.")
                    continue
            elif operation == 6:
                print("You have selected Mass division!")
                ordering_list = []
                while True:
                    number = input("Enter a number to add to the list or type 'done' to finish: ")
                    if number == "done":
                        break
                    else:
                        number = float(number)
                        ordering_list.append(number)
                try:    
                    print(f"The quotient of the numbers is {divide_list(ordering_list)}.")
                    copy_to_keyboard(divide_list(ordering_list), copy_to_keyboard_true)
                except:
                    print("Invalid values!Please try again.")
                    continue
            elif operation == 7:
                print("You have selected Finding the upper and lower bounds of a rounded number!")
                number = float(input("Enter the rounded number: "))
                decimal_places = int(input("Enter the number of decimal places the number is rounded to(0 for whole numbers): "))
                if decimal_places == 0:
                    lower_bound = number - 0.5
                    upper_bound = number + 0.5
                else:
                    lower_bound = number - (0.5 * (10 ** -decimal_places))
                    upper_bound = number + (0.5 * (10 ** -decimal_places))
                print(f"The lower bound of the number is {lower_bound} and the upper bound is {upper_bound}.")
                copy_to_keyboard(f"{lower_bound},{upper_bound}", copy_to_keyboard_true)
            elif operation == 8:
                print("You have selected Finding the upper and lower bounds of a number rounded to significant figures!")
                number = float(input("Enter the rounded number: "))
                significant_figures = int(input("Enter the number of significant figures the number is rounded to: "))
                order_of_magnitude = math.floor(math.log10(abs(number)))
                decimal_places = significant_figures - order_of_magnitude - 1
                if decimal_places <= 0:
                    lower_bound = number - (5 * (10 ** (order_of_magnitude - significant_figures + 1)))
                    upper_bound = number + (5 * (10 ** (order_of_magnitude - significant_figures + 1)))
                else:
                    lower_bound = number - (0.5 * (10 ** -decimal_places))
                    upper_bound = number + (0.5 * (10 ** -decimal_places))
                print(f"The lower bound of the number is {lower_bound} and the upper bound is {upper_bound}.")
                copy_to_keyboard(f"{lower_bound},{upper_bound}", copy_to_keyboard_true)
            elif operation == 9:
                print("You have selected Finding the upper and lower bounds of a truncated number!")
                number = float(input("Enter the truncated number: "))
                decimal_places = int(input("Enter the number of decimal places the number is truncated to(0 for whole numbers): "))
                if decimal_places == 0:
                    lower_bound = number
                    upper_bound = number + 1
                else:
                    lower_bound = number
                    upper_bound = number + (10 ** -decimal_places)
                print(f"The lower bound of the number is {lower_bound} and the upper bound is {upper_bound}.")
                copy_to_keyboard(f"{lower_bound},{upper_bound}", copy_to_keyboard_true)

            else:
                print("Invalid operation!Please try again.")
                continue
        elif category == 7:
            print("Welcome to the Scale factors category!")
            print("Please select an operation:")
            print("""1. Calculate the scale factor
            2. Calculate the new length
            3. Calcuate the original length""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Calculate the scale factor!")
                original_length = float(input("Enter the original length: "))
                new_length = float(input("Enter the new length: "))
                scale_factor = new_length / original_length
                print(f"The scale factor is {scale_factor}.")
                copy_to_keyboard(scale_factor, copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Calculate the new length!")
                original_length = float(input("Enter the original length: "))
                scale_factor = float(input("Enter the scale factor: "))
                new_length = original_length * scale_factor
                print(f"The new length is {new_length} {lenght_units}.")
                copy_to_keyboard(new_length, copy_to_keyboard_true)
            elif operation == 3:
                print("You have selected Calculate the original length!")
                new_length = float(input("Enter the new length: "))
                scale_factor = float(input("Enter the scale factor: "))
                original_length = new_length / scale_factor
                print(f"The original length is {original_length} {lenght_units}.")
                copy_to_keyboard(original_length, copy_to_keyboard_true)
            else:
                print("Invalid operation!Please try again.")
                continue
        elif category == 8:
            print("Welcome to the Decimal to fraction to percentage conversions category!")
            print("""Please select an operation:
            1. Decimal to fraction
            2. Fraction to decimal
            3. Decimal to percentage
            4. Percentage to decimal
            5. Fraction to percentage
            6. Percentage to fraction""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Decimal to fraction!")
                decimal = float(input("Enter the decimal you want to convert to a fraction: "))
                fraction = fractions.Fraction(decimal).limit_denominator()
                print(f"The fraction is {fraction}.")
                copy_to_keyboard(fraction, copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Fraction to decimal!")
                numerator = float(input("Enter the numerator of the fraction: "))
                denominator = float(input("Enter the denominator of the fraction: "))
                decimal = numerator / denominator
                print(f"The decimal is {decimal}.")
                copy_to_keyboard(decimal, copy_to_keyboard_true)
            elif operation == 3:
                print("You have selected Decimal to percentage!")
                decimal = float(input("Enter the decimal you want to convert to a percentage: "))
                percentage = decimal * 100
                print(f"The percentage is {percentage}%.")
                copy_to_keyboard(percentage, copy_to_keyboard_true)
            elif operation == 4:
                print("You have selected Percentage to decimal!")
                percentage = float(input("Enter the percentage you want to convert to a decimal: "))
                decimal = percentage / 100
                print(f"The decimal is {decimal}.")
                copy_to_keyboard(decimal, copy_to_keyboard_true)
            elif operation == 5:
                print("You have selected Fraction to percentage!")
                numerator = float(input("Enter the numerator of the fraction: "))
                denominator = float(input("Enter the denominator of the fraction: "))
                percentage = (numerator / denominator) * 100
                print(f"The percentage is {percentage}%.")
                copy_to_keyboard(percentage, copy_to_keyboard_true)
            elif operation == 6:
                print("You have selected Percentage to fraction!")
                percentage = float(input("Enter the percentage you want to convert to a fraction: "))
                fraction = fractions.Fraction(percentage / 100).limit_denominator()
                print(f"The fraction is {fraction}.")
                copy_to_keyboard(fraction, copy_to_keyboard_true)
            else:
                print("Invalid operation!Please try again.")
                continue
        elif category == 9:
    #       FORMULAS TO REMEMBER(in case it breaks again):
    #       Simple intrest: I = PRT/100(with intrest rate as %)
    #       Compound intrest: A = P(1 + r/100)^(t)(with compound intrest rate as %)
    #       DO NOT DELETE THIS!!!!!!!!
            print("Welcome to the Intrest category!")
            print("Please select a sub-category:")
            print("""1. Simple intrest
            2. Compound intrest""")
            sub_category = int(input("Enter the number of the sub-category you want to use: "))
            if sub_category == 1:
                print("You have selected Simple intrest!")
                print("Please select an operation:")
                print("""1. Calculate the simple intrest
                2. Calculate the principal
                3. Calculate the rate(%)
                4. Calculate the time""")
                operation = int(input("Enter the number of the operation you want to perform: "))
                if operation == 1:
                    print("You have selected Calculate the simple intrest!")
                    principal = float(input(f"Enter the principal({money_units}): "))
                    rate = float(input("Enter the rate(%): "))
                    time = float(input("Enter the time(years): "))
                    simple_intrest = (principal * rate * time) / 100
                    print(f"The simple intrest is {money_units} {simple_intrest} .")
                    copy_to_keyboard(simple_intrest, copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Calculate the principal!")
                    simple_intrest = float(input(f"Enter the simple intrest({money_units}): "))
                    rate = float(input("Enter the rate(%): "))
                    time = float(input("Enter the time(years): "))
                    principal = (simple_intrest * 100) / (rate * time)
                    print(f"The principal is {money_units} {principal} .")
                    copy_to_keyboard(principal, copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Calculate the rate(%)!")
                    principal = float(input(f"Enter the principal({money_units}): "))
                    simple_intrest = float(input(f"Enter the simple intrest({money_units}): "))
                    time = float(input("Enter the time(years): "))
                    rate = (simple_intrest * 100) / (principal * time)
                    print(f"The rate is {rate}%.")
                    copy_to_keyboard(rate, copy_to_keyboard_true)
                elif operation == 4:
                    print("You have selected Calculate the time!")
                    principal = float(input(f"Enter the principal({money_units}): "))
                    simple_intrest = float(input(f"Enter the simple intrest({money_units}): "))
                    rate = float(input("Enter the rate(%): "))
                    time = (simple_intrest * 100) / (principal * rate)
                    print(f"The time is {time} years.")
                    copy_to_keyboard(time, copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif sub_category == 2:
                print("You have selected Compound intrest!")
                print("Please select an operation:")
                print("""1. Calculate the compound intrest
                2. Calculate the principal
                3. Calculate the rate(%)
                4. Calculate the time""")
                operation = int(input("Enter the number of the operation you want to perform: "))
                if operation == 1:
                    print("You have selected Calculate the compound intrest!")
                    principal = float(input(f"Enter the principal({money_units}): "))
                    rate = float(input("Enter the rate(%): "))
                    time = float(input("Enter the time(years): "))
                    compound_intrest = principal * ((1 + (rate / 100)) ** time)
                    print(f"The compound intrest is {money_units} {compound_intrest} .")
                    copy_to_keyboard(compound_intrest, copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Calculate the principal!")
                    compound_intrest = float(input(f"Enter the compound intrest({money_units}): "))
                    rate = float(input("Enter the rate(%): "))
                    time = float(input("Enter the time(years): "))
                    principal = compound_intrest / ((1 + (rate / 100)) ** time)
                    print(f"The principal is {money_units} {principal} .")
                    copy_to_keyboard(principal, copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Calculate the rate(%)!")
                    principal = float(input(f"Enter the principal({money_units}): "))
                    compound_intrest = float(input(f"Enter the compound intrest({money_units}): "))
                    time = float(input("Enter the time(years): "))
                    rate = ((compound_intrest / principal) ** (1/time) - 1) * 100
                    print(f"The rate is {rate}%.")
                    copy_to_keyboard(rate, copy_to_keyboard_true)
                elif operation == 4:
                    print("You have selected Calculate the time!")
                    principal = float(input(f"Enter the principal({money_units}): "))
                    compound_intrest = float(input(f"Enter the compound intrest({money_units}): "))
                    rate = float(input("Enter the rate(%): "))
                    time = math.log(compound_intrest / principal) / math.log(1 + (rate / 100))
                    print(f"The time is {time} years.")
                    copy_to_keyboard(time, copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
            else:
                print("Invalid sub-category!Please try again.")
                continue
        elif category == 10:
    #      FORMULAS TO REMEMBER(in case it breaks again):
    #      sin(x) = opposite/hypotnuse
    #      cos(x) = adjacent/hypotnuse
    #      tan(x) = opposite/adjacent
            print("Welcome to the Trigomentry(SOHCAHTOA) category!")
            print("Please select an operation:")
            print("""1. Finding sin(x) 
    2. Finding cos(x)
    3. Finding tan(x)
    4. Finding hypotnuse(using sin(x))
    5. Finding hypotnuse(using cos(x))
    6. Finding opposite(using sin(x))
    7. Finding opposite(using tan(x))
    8. Finding adjacent(using cos(x))
    9. Finding adjacent(using tan(x))

    Please note that the angles are in degrees""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Finding sin(x)!")
                opposite = float(input("Enter the length of the opposite side: "))
                hypotnuse = float(input("Enter the length of the hypotnuse: "))
                sin = opposite / hypotnuse
                angle = math.degrees(math.asin(sin))
                print(f"The sin(x) is {sin} and the angle is {angle}°.")
                copy_to_keyboard(f"The sin(x) is {sin} and the angle is {angle}°.", copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Finding cos(x)!")
                adjacent = float(input("Enter the length of the adjacent side: "))
                hypotnuse = float(input("Enter the length of the hypotnuse: "))
                cos = adjacent / hypotnuse
                angle = math.degrees(math.acos(cos))
                print(f"The cos(x) is {cos} and the angle is {angle}°.")
                copy_to_keyboard(f"The cos(x) is {cos} and the angle is {angle}°.", copy_to_keyboard_true)
            elif operation == 3:
                print("You have selected Finding tan(x)!")
                opposite = float(input("Enter the length of the opposite side: "))
                adjacent = float(input("Enter the length of the adjacent side: "))
                tan = opposite / adjacent
                angle = math.degrees(math.atan(tan))
                print(f"The tan(x) is {tan} and the angle is {angle}°.")
                copy_to_keyboard(f"The tan(x) is {tan} and the angle is {angle}°.", copy_to_keyboard_true)
            elif operation == 4:
                print("You have selected Finding hypotnuse(using sin(x))!")
                opposite = float(input("Enter the length of the opposite side: "))
                angle = float(input("Enter the angle(degrees): "))
                sin = math.sin(math.radians(angle))
                hypotnuse = opposite / sin
                print(f"The hypotnuse is {hypotnuse} {lenght_units}.")
                copy_to_keyboard(hypotnuse, copy_to_keyboard_true)
            elif operation == 5:
                print("You have selected Finding hypotnuse(using cos(x))!")
                adjacent = float(input("Enter the length of the adjacent side: "))
                angle = float(input("Enter the angle(degrees): "))
                cos = math.cos(math.radians(angle))
                hypotnuse = adjacent / cos
                print(f"The hypotnuse is {hypotnuse} {lenght_units}.")
                copy_to_keyboard(hypotnuse, copy_to_keyboard_true)
            elif operation == 6:
                print("You have selected Finding opposite(using sin(x))!")
                hypotnuse = float(input("Enter the length of the hypotnuse: "))
                angle = float(input("Enter the angle(degrees): "))
                sin = math.sin(math.radians(angle))
                opposite = hypotnuse * sin
                print(f"The opposite is {opposite} {lenght_units}.")
                copy_to_keyboard(opposite, copy_to_keyboard_true)
            elif operation == 7:
                print("You have selected Finding opposite(using tan(x))!")
                adjacent = float(input("Enter the length of the adjacent side: "))
                angle = float(input("Enter the angle(degrees): "))
                tan = math.tan(math.radians(angle))
                opposite = adjacent * tan
                print(f"The opposite is {opposite} {lenght_units}.")
                copy_to_keyboard(opposite, copy_to_keyboard_true)
            elif operation == 8:
                print("You have selected Finding adjacent(using cos(x))!")
                hypotnuse = float(input("Enter the length of the hypotnuse: "))
                angle = float(input("Enter the angle(degrees): "))
                cos = math.cos(math.radians(angle))
                adjacent = hypotnuse * cos
                print(f"The adjacent is {adjacent} {lenght_units}.")
                copy_to_keyboard(adjacent, copy_to_keyboard_true)
            elif operation == 9:
                print("You have selected Finding adjacent(using tan(x))!")
                opposite = float(input("Enter the lenght of the opposite:"))
                angle = float(input("Enter the angle(degrees):"))
                tan = math.tan(math.radians(angle))
                adjacent = opposite * tan
                print(f"The adjacent is {adjacent} {lenght_units}.")
                copy_to_keyboard(adjacent,copy_to_keyboard_true)
            else:
                print("Invalid operation!Please try again.")
                continue
        elif category == 11:
            print("You have selected the Line category!")
            print("Please select an operation:")
            print("""1. Calculate the gradient/slope
    2. Calculate the y-intercept
    3. Calculate the x-intercept
    4. Calculate the equation of the line
    5. Calculate the distance between two points
    6.Calcuate the midpoint of two points
    7. Calcuate gradient of perpendicular line
    8. Calcuate gradient of parallel line
    9. Calcuate the equation of a perpendicular line
    10. Calcuate the equation of a parrellel line""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Calculate the gradient/slope!")
                x1 = float(input("Enter the x-coordinate of the first point: "))
                y1 = float(input("Enter the y-coordinate of the first point: "))
                x2 = float(input("Enter the x-coordinate of the second point: "))
                y2 = float(input("Enter the y-coordinate of the second point: "))
                gradient = (y2 - y1) / (x2 - x1)
                print(f"The gradient/slope is {gradient}.")
                copy_to_keyboard(gradient, copy_to_keyboard_true)
            elif operation == 2:
                print("You have selected Calculate the y-intercept!")
                x = float(input("Enter the x-coordinate of a point on the line: "))
                y = float(input("Enter the y-coordinate of the point on the line: "))
                gradient = float(input("Enter the gradient/slope of line: "))
                y_intercept = y - (gradient * x)
                print(f"The y-intercept is {y_intercept}.")
                copy_to_keyboard(y_intercept, copy_to_keyboard_true)
            elif operation == 3:
                print("You have selected Calculate the x-intercept!")
                y = float(input("Enter the y-coordinate of a point on the line: "))
                x = float(input("Enter the x-coordinate of the point on the line: "))
                gradient = float(input("Enter the gradient/slope of line: "))
                x_intercept = find_x_intercept(gradient, y)
                print(f"The x-intercept is {x_intercept}.")
                copy_to_keyboard(x_intercept, copy_to_keyboard_true)
            elif operation == 4:
                print("You have selected Calculate the equation of the line!")
                x1 = float(input("Enter the x-coordinate of the first point: "))
                y1 = float(input("Enter the y-coordinate of the first point: "))
                x2 = float(input("Enter the x-coordinate of the second point: "))
                y2 = float(input("Enter the y-coordinate of the second point: "))
                gradient = (y2 - y1) / (x2 - x1)
                y_intercept = y1 - (gradient * x1)#what if y-intercept negiative?
                print(f"The equation of the line is y = {gradient}x{y_intercept:+}.")
                copy_to_keyboard(f"The equation of the line is y = {gradient}x{y_intercept:+}.", copy_to_keyboard_true)
            elif operation == 5:
                print("You have selected Calculate the distance between two points!")
                x1 = float(input("Enter the x-coordinate of the first point: "))
                y1 = float(input("Enter the y-coordinate of the first point: "))
                x2 = float(input("Enter the x-coordinate of the second point: "))
                y2 = float(input("Enter the y-coordinate of the second point: "))
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                print(f"The distance between the two points is {distance} {lenght_units}.")
                copy_to_keyboard(distance, copy_to_keyboard_true)
            elif operation == 6:
                print("You have selected Calculate the midpoint of two points!")
                x1 = float(input("Enter the x-coordinate of the first point: "))
                y1 = float(input("Enter the y-coordinate of the first point: "))
                x2 = float(input("Enter the x-coordinate of the second point: "))
                y2 = float(input("Enter the y-coordinate of the second point: "))
                midpoint_x = (x1 + x2) / 2
                midpoint_y = (y1 + y2) / 2
                print(f"The midpoint of the two points is ({midpoint_x},{midpoint_y}).")
                copy_to_keyboard(f"The midpoint of the two points is ({midpoint_x},{midpoint_y}).", copy_to_keyboard_true)
            elif operation == 7:
                print("You have selected Calculate gradient of perpendicular line!")
                gradient = float(input("Enter the gradient of the other line: "))
                perpendicular_gradient = -1 / gradient
                print(f"The gradient of the perpendicular line is {perpendicular_gradient}(Fraction=-1/{gradient}).")
            elif operation == 8:
                print("The gradient of the parallel line is the same as the other line!")
            elif operation == 9:
                print("You have selected Calculate the equation of a perpendicular line!")
                gradient = float(input("Enter the gradient of the other line: "))
                y_intercept = float(input("Enter the y-intercept of the other line: "))
                x2 = float(input("Enter the x-coordinate of a point the perpendicular line passes through: "))
                y2 = float(input("Enter the y-coordinate of a point the perpendicular line passes through: "))
                perpendicular_gradient = -1 / gradient
                y_intercept = y2 - (perpendicular_gradient * x2)
                print(f"The equation of the perpendicular line is y = {perpendicular_gradient}x{y_intercept:+}.")
                copy_to_keyboard(f"The equation of the perpendicular line is y = {perpendicular_gradient}x{y_intercept:+}.", copy_to_keyboard_true)
            elif operation == 10:
                print("You have selected Calculate the equation of a parallel line!")
                gradient = float(input("Enter the gradient of the other line: "))
                x2 = float(input("Enter the x-coordinate of a point the parallel line passes through: "))
                y2 = float(input("Enter the y-coordinate of a point the parallel line passes through: "))
                parallel_gradient = gradient
                y_intercept = y2 - (parallel_gradient * x2)
                print("The equation of the parallel line is y = {parallel_gradient}x{y_intercept:+}.")
                copy_to_keyboard(f"The equation of the parallel line is y = {parallel_gradient}x{y_intercept:+}.", copy_to_keyboard_true)


            else:
                print("Invalid operation!Please try again.")
                continue

        elif category == 12:
            print("Welcome to the Equation category!")
            print("Please select an operation:")
            print("""1. Solve a equation
2.Solve two simultaoenous equations""")
            operation = int(input("Enter the number of the operation you want to perform(note:only supports x/y as vars): "))
            if operation == 1:
                print("You have selected Solve a equation!")
                eq.equation_calc()
            elif operation == 2:
                print("You have selected Solve two simultaoenous equations!")
                eq.simultanous_calc()
                
            else:
                print("Invalid operation!Please try again.")
                continue
        elif category == 13:
            pi = math.pi
            print("Welcome to the Circles/Sphere category!")
            print("Please select a shape:")
            print("""1. Circle
2. Sphere""")
            shape = int(input("Enter the number of the shape you want to use: "))
            if shape == 1:
                print("You have selected Circle!")
                print("Please select an operation:")
                print("""
1. Calculate the diameter/radius
2.Calcuate area of sector
3.Calcuate arc length
4.Calcuate area of segment
5.Calcuate chord lenght
6.Calcuate central angle""")
                operation = int(input("Enter the number of the operation you want to perform: "))
                if operation == 1:
                    print("You have selected Calculate the diameter/radius!")
                    print("Please select a method:")
                    print("""1. Using the radius
2. Using diameter
3. Using the circumference
4. Using the sector area
5. Using arc lenght
6. Using the segment area
7. Using the chord lenght""")
                    method = int(input("Enter the number of the method you want to use: "))
                    if method == 1:
                        radius = float(input("Enter the radius of the circle: "))
                        diameter = radius * 2
                        print(f"The diameter of the circle is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    elif method == 2:
                        diameter = float(input("Enter the diameter of the circle: "))
                        radius = diameter / 2
                        print("The radius of the circle is {radius} {lenght_units} and the diameter is {diameter} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    elif method == 3:
                        circumference = float(input("Enter the circumference of the circle: "))
                        diameter = circumference / pi
                        radius = diameter / 2
                        print(f"The diameter of the circle is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    elif method == 4:
                        sector_area = float(input("Enter the area of the sector: "))
                        angle = float(input("Enter the angle of the sector(degrees): "))
                        radius = math.sqrt((sector_area * angle) / (pi))
                        diameter = radius * 2
                        print(f"The diameter of the circle is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    elif method == 5:
                        arc_lenght =  float(input("Enter the arc lenght of the circle: "))
                        angle = float(input("Enter the angle of the sector(degrees): "))
                        radius = arc_lenght / (math.radians(angle))
                        diameter = radius * 2
                        print(f"The diameter of the circle is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    elif method == 6:
                        print("Please chose a method:")
                        print("""1. Using the central angle
2. Using the chord length""")
                        sub_method = int(input("Enter the number of the method you want to use: "))
                        if sub_method == 1:
                            print("You have chosen Using the central angle!")
                            segment_area = float(input("Enter the area of the segment: "))
                            angle = float(input("Enter the central angle of the segment(degrees): "))
                            radius = math.sqrt((segment_area * 360) / (pi))
                            diameter = radius * 2
                            print(f"The diameter of the circle is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                            copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                        elif sub_method == 2:
                            print("You have chosen Using the chord length!")
                            segment_area = float(input("Enter the area of the segment: "))
                            chord_length = float(input("Enter the chord length of the segment: "))
                            radius = math.sqrt((segment_area * 360) / (pi))
                            diameter = radius * 2
                            print(f"The diameter of the circle is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                            copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                        else:
                            print("Invalid method!Please try again.")
                            continue
                    elif method == 7:
                        print("You have chosen Using the chord length!")
                        chord_length = float(input("Enter the chord length of the circle: "))
                        angle = float(input("Enter the central angle of the segment(degrees): "))
                        radius = (chord_length / 2) / math.sin(math.radians(angle / 2))
                        diameter = radius * 2
                        print(f"The diameter of the circle is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                        
                            

                    else:
                        print("Invalid method!Please try again.")
                        continue
                
                elif operation == 2:
                    print("You have selected Calcuate area of sector!")
                    radius = float(input("Enter the radius of the circle: "))
                    angle = float(input("Enter the angle of the sector(degrees): "))
                    area = (angle / 360) * pi * (radius ** 2)
                    print(f"The area of the sector is {area} {area_units}.")
                    copy_to_keyboard(area, copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Calcuate arc length!")
                    radius = float(input("Enter the radius of the circle: "))
                    angle = float(input("Enter the angle of the sector(degrees): "))
                    arc_length = radius * math.radians(angle)
                    print(f"The arc length is {arc_length} {lenght_units}.")
                    copy_to_keyboard(arc_length, copy_to_keyboard_true)
                elif operation == 4:
                    #Apply the segment area formula: 0.5 × r² × (α – sin(α)).(a=central angle)
                    #Alt:Area of a sector-Area of triangle of sector
                    print("You have selected Calcuate area of segment!")
                    print("Please select a method:")
                    print("""1. Using the radius and the central angle
                          2. Using the radius and the chord length""")
                    method = int(input("Enter the number of the method you want to use: "))
                    if method == 1:
                        print("You have selected Using the radius and the central angle!")
                        radius = float(input("Enter the radius of the circle: "))
                        angle = float(input("Enter the central angle of the segment(degrees): "))
                        area = 0.5 * (radius ** 2) * (angle - math.sin(math.radians(angle)))
                        print(f"The area of the segment is {area} {area_units}.")
                        copy_to_keyboard(area, copy_to_keyboard_true)
                    elif method == 2:
                        print("You have selected Using the radius and the chord length!")
                        radius = float(input("Enter the radius of the circle: "))
                        chord_lenght = float(input("Enter the chord length of the segment: "))
                        area = 0.5 * (radius ** 2) * (2 * math.asin(chord_lenght / (2 * radius)) - math.sin(2 * math.asin(chord_lenght / (2 * radius))))
                        print(f"The area of the segment is {area} {area_units}.")
                        copy_to_keyboard(area, copy_to_keyboard_true)
                    else:
                        print("Invalid method!Please try again.")
                        continue
                elif operation == 5:
                    print("You have selected Calcuate chord lenght!")
                    radius = float(input("Enter the radius of the circle: "))
                    angle = float(input("Enter the central angle of the segment(degrees): "))
                    chord_length = 2 * radius * math.sin(math.radians(angle / 2))
                    print(f"The chord length is {chord_length} {lenght_units}.")
                    copy_to_keyboard(chord_length, copy_to_keyboard_true)
                elif operation == 6:
                    print("You have selected Calcuate the central angle!")
                    print("Please chose a method:")
                    print("""1.Using area of sector+radius
2.Using the arc lenght+radius
3. Using the segment area+radius
4. Using the chord lenght+radius""")
                    method = int(input("Enter the number of the method you want to use: "))
                    if method == 1:
                        print("You have selected Using area of sector+radius!")
                        radius = float(input("Enter the radius of the sector: "))
                        sector_area = float(input("Enter the area of the sector: "))
                        angle = (sector_area / (0.5 * pi * (radius ** 2))) * 360
                        print(f"The central angle is {angle}°.")
                        copy_to_keyboard(angle, copy_to_keyboard_true)
                    elif method == 2:
                        print("You have selected Using the arc lenght+radius!")
                        radius = float(input("Enter the radius of the sector: "))
                        arc_lenght = float(input("Enter the arc lenght of the sector: "))
                        angle = arc_lenght / radius
                        angle = math.degrees(angle)
                        print(f"The central angle is {angle}°.")
                        copy_to_keyboard(angle, copy_to_keyboard_true)
                    elif method == 3:
                        print("You have selected Using the segment area+radius!")
                        radius = float(input("Enter the radius of the sector: "))
                        segment_area = float(input("Enter the area of the segment: "))
                        angle = (segment_area / (0.5 * (radius ** 2))) + math.sin(segment_area / (0.5 * (radius ** 2)))
                        angle = math.degrees(angle)
                        print(f"The central angle is {angle}°.")
                        copy_to_keyboard(angle, copy_to_keyboard_true)
                    elif method == 4:
                        print("You have selected Using the chord lenght+radius!")
                        radius = float(input("Enter the radius of the sector: "))
                        chord_lenght = float(input("Enter the chord lenght of the sector: "))
                        angle = 2 * math.asin(chord_lenght / (2 * radius))
                        angle = math.degrees(angle)
                        print(f"The central angle is {angle}°.")
                        copy_to_keyboard(angle, copy_to_keyboard_true)
                    else:
                        print("Invalid method!Please try again.")
                        continue
                    
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif shape == 2:
                #V=2/3piR^2h
                print("You have selected Sphere!")
                print("Please select an operation:")
                print("""
1. Calculate the diameter/radius
2.Calcuate volume of spherical cone
3.Calcuate lenght of Great circle
4.Calcuate volume of spherical cap
5.Calcuate volume of spherical segment
6.Calcuate volume of spherical wedge""")
                operation = int(input("Enter the number of the operation you want to perform: "))
                if operation == 1:
                    print("You have selected Calculate the diameter/radius!")
                    print("Please select a method:")
                    print("""1. Using the radius
2. Using diameter
3. Using the great circle circumference""")
                    method = int(input("Enter the number of the method you want to use: "))
                    if method == 1:
                        radius = float(input("Enter the radius of the sphere: "))
                        diameter = radius * 2
                        print(f"The diameter of the sphere is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    elif method == 2:
                        diameter = float(input("Enter the diameter of the sphere: "))
                        radius = diameter / 2
                        print("The radius of the sphere is {radius} {lenght_units} and the diameter is {diameter} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    elif method == 3:
                        circumference = float(input("Enter the circumference of the great circle: "))
                        diameter = circumference / pi
                        radius = diameter / 2
                        print(f"The diameter of the sphere is {diameter} {lenght_units} and the raduis is {radius} {lenght_units}.")
                        copy_to_keyboard(f"{diameter},{radius}", copy_to_keyboard_true)
                    
                        
                            

                    else:
                        print("Invalid method!Please try again.")
                        continue
                
                elif operation == 2:
                    print("You have selected Calcuate volume of spherical cone!")
                    radius = float(input("Enter the radius of the cone: "))
                    height = float(input("Enter the height of the cone: "))
                    area = (2/3) * pi * (radius ** 2) * height
                    print(f"The volume of the spherical cone is {area} {volume_units}.")
                    copy_to_keyboard(area, copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Calcuate lenght of Great Circle!")
                    radius = float(input("Enter the radius of the sphere: "))
                    x = float(input("Enter the frist angle of latitude of the sphere(degrees): "))
                    y = float(input("Enter the second angle of latitude of the sphere(degrees): "))
                    a = float(input("Enter the first angle of longitude of the sphere(degrees): "))
                    b = float(input("Enter the second angle of longitude of the sphere(degrees): "))
                    arc_length = radius * math.acos(math.sin(math.radians(x)) * math.sin(math.radians(y)) + math.cos(math.radians(x)) * math.cos(math.radians(y)) * math.cos(math.radians(a - b)))
                    print(f"The lenght of the Great Circle is {arc_length} {lenght_units}.")
                    copy_to_keyboard(arc_length, copy_to_keyboard_true)
                elif operation == 4:
                    print("You have selected Calcuate volume of a spherical cap!")
                    radius = float(input("Enter the radius of the cap: "))
                    height = float(input("Enter the height of the cap: "))
                    area = (1/3) * pi * (height ** 2) * ((3 * radius) - height)
                    print(f"The volume of the cap is {area} {volume_units}.")
                    copy_to_keyboard(area, copy_to_keyboard_true)
                elif operation == 5:
                    # (1/6)πh((3r1)^2 + (3r2)^2 + h^2)
                    print("You have selected Calcuate volume of spherical segment!")
                    r1 = float(input("Enter the radius of the base circle of segment: "))
                    r2 = float(input("Enter the radius of the top circle of segment: "))
                    h = float(input("Enter the height of the segment: "))
                    volume = (1/6) * pi * h * ((3 * (r1 ** 2)) + (3 * (r2 ** 2)) + (h ** 2))
                    print(f"The volume of the segment is {volume} {volume_units}.")
                    copy_to_keyboard(volume, copy_to_keyboard_true)
                elif operation == 6:
                    #(θ/360°)(4/3)π(R^3)
                    print("You have selected Calcuate the volume of spherical wedge!")
                    radius = float(input("Enter the radius of the wedge: "))
                    angle = float(input("Enter the angle of the wedge(degrees): "))
                    volume = (angle / 360) * ((4/3) * pi * (radius ** 3))
                    print("The volume of the wedge is {volume} {volume_units}.")
                    copy_to_keyboard(volume, copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
                
            else:
                print("Invalid shape!Please try again.")
                continue
        elif category == 14:
            operation = calc("Others",["Chemistry/Physics calc","Ratio calc","Statistics calc(indev)","Probability calc","Surds calc","Unit conversion calc","Miscellaneous calc"],2)
            if operation == 1:
                operation = calc("Chemistry/Physics calc",["Relative mass calc","Atomic weight using relative mass calc","Moles calc","Thermodynamics calc","Electrochemistry calc","SVT calc"],1)
                if operation == 1:
                    print("You have selected Relative mass calc!")
                    mass_list = []
                    abundance_list = []
                    while True:
                        mass = input("Enter the mass of a isotope:(type done to stop recording) ")
                        if mass == "done":
                            break
                        abundance = input("Enter the abundance of the isotope(%): ")
                        
                        mass_list.append(float(mass))
                        abundance_list.append(float(abundance))
                    product_list = []
                    for i in range(len(mass_list)):
                        product = mass_list[i] * abundance_list[i]
                        product_list.append(product)

                    relative_mass = sum(product_list) / 100
                    print(f"The relative mass of the element is {relative_mass}.")
                    copy_to_keyboard(relative_mass, copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Atomic weight using relative mass calc!")
                    mass_list = []
                    abundance_list = []
                    product_list = []
                    while True:
                    
                    
                        mass = input("Enter the mass of a known isotope (or type 'done' to finish): ")
                        if mass == 'done':
                            break
                        else:
                            abundance = input("Enter the abundance of the known isotope: ")
                            mass_list.append(float(mass))
                            abundance_list.append(float(abundance))
                            product = float(mass) * float(abundance)
                            product_list.append(product)
                    relative_mass = float(input("Enter the relative mass of the isotope: "))
                    abunance = 100 - sum(abundance_list)
                    atomic_weight = relative_mass * 100
                    for i in range(len(mass_list)):
                        atomic_weight -= product_list[i]
                    atomic_weight /= abunance
                    print("The atomic weight of the unknown isotope is: ", atomic_weight)
                    copy_to_keyboard(atomic_weight, copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Moles calc!")
                    concentration = float(input("Enter the concentration of the solution (mol/L): "))
                    volume = float(input("Enter the volume of the solution (L): "))
                    moles = concentration * volume
                    print(f"The number of moles is {moles}.")
                    copy_to_keyboard(moles, copy_to_keyboard_true)
                elif operation == 4:
                    method = calc("Thermodynamics calc",["Enthalpy calc","Entropy calc","Gibbs free energy calc","Heat capacity calc"],3)
                    if method == 1:
                        print("You have selected Enthalpy calc!")
                        enthalpy = float(input("Enter the enthalpy (kJ/mol): "))
                        temperature = float(input("Enter the temperature (K): "))
                        enthalpy_change = enthalpy / temperature
                        print(f"The enthalpy change is {enthalpy_change} kJ/mol/K.")
                        copy_to_keyboard(enthalpy_change, copy_to_keyboard_true)
                    elif method == 2:
                        print("You have selected Entropy calc!")
                        entropy = float(input("Enter the entropy (J/mol/K): "))
                        temperature = float(input("Enter the temperature (K): "))
                        entropy_change = entropy / temperature
                        print(f"The entropy change is {entropy_change} J/mol/K.")
                        copy_to_keyboard(entropy_change, copy_to_keyboard_true)
                    elif method == 3:
                        print("You have selected Gibbs free energy calc!")
                        enthalpy = float(input("Enter the enthalpy (kJ/mol): "))
                        entropy = float(input("Enter the entropy (J/mol/K): "))
                        temperature = float(input("Enter the temperature (K): "))
                        gibbs_free_energy = enthalpy - (temperature * entropy)
                        print(f"The Gibbs free energy is {gibbs_free_energy} kJ/mol.")
                        copy_to_keyboard(gibbs_free_energy, copy_to_keyboard_true)
                    elif method == 4:
                        print("You have selected Heat capacity calc!")
                        heat_capacity = float(input("Enter the heat capacity (J/mol/K): "))
                        temperature_change = float(input("Enter the temperature change (K): "))
                        heat_capacity_change = heat_capacity * temperature_change
                        print(f"The heat capacity change is {heat_capacity_change} J/mol.")
                        copy_to_keyboard(heat_capacity_change, copy_to_keyboard_true)
                    else:
                        print("Invalid method!Please try again.")
                        continue
                elif operation == 5:
                    method = calc("Electrochemistry calc",["Electrochemical cell calc","Electrolysis calc","Faraday's law calc"],3)
                    if method == 1:
                        print("You have selected Electrochemical cell calc!")
                        cell_potential = float(input("Enter the cell potential (V): "))
                        current = float(input("Enter the current (A): "))
                        time = float(input("Enter the time (s): "))
                        charge = cell_potential * current * time
                        print(f"The charge is {charge} C.")
                        copy_to_keyboard(charge, copy_to_keyboard_true)
                    elif method == 2:
                        print("You have selected Electrolysis calc!")
                        current = float(input("Enter the current (A): "))
                        time = float(input("Enter the time (s): "))
                        charge = current * time
                        print(f"The charge is {charge} C.")
                        copy_to_keyboard(charge, copy_to_keyboard_true)
                    elif method == 3:
                        print("You have selected Faraday's law calc!")
                        current = float(input("Enter the current (A): "))
                        time = float(input("Enter the time (s): "))
                        charge = current * time
                        faraday_constant = 96485.3329
                        moles = charge / faraday_constant
                        print(f"The number of moles is {moles}.")
                        copy_to_keyboard(moles, copy_to_keyboard_true)
                    else:
                        print("Invalid method!Please try again.")
                        continue
                elif operation == 6:
                    operation = calc("SVT calc",["Calcuate displacement","Calcuate final velocity","Calcuate time"],1)
                    if operation == 1:
                        print("You have selected Calcuate displacement!")
                        initial_velocity = float(input("Enter the initial velocity (m/s): "))
                        final_velocity = float(input("Enter the final velocity (m/s): "))
                        time = float(input("Enter the time (s): "))
                        displacement = calculate_displacement(initial_velocity, final_velocity, time)
                        print(f"The displacement is {displacement} {lenght_units}.")
                        copy_to_keyboard(displacement, copy_to_keyboard_true)
                    elif operation == 2:
                        print("You have selected Calcuate final velocity!")
                        initial_velocity = float(input("Enter the initial velocity (m/s): "))
                        acceleration = float(input("Enter the acceleration (m/s²): "))
                        time = float(input("Enter the time (s): "))
                        final_velocity = calculate_final_velocity(initial_velocity, acceleration, time)
                        print(f"The final velocity is {final_velocity} {lenght_units}.")
                        copy_to_keyboard(final_velocity, copy_to_keyboard_true)
                    elif operation == 3:
                        print("You have selected Calcuate time!")
                        initial_velocity = float(input("Enter the initial velocity (m/s): "))
                        final_velocity = float(input("Enter the final velocity (m/s): "))
                        acceleration = float(input("Enter the acceleration (m/s²): "))
                        time = calculate_time(initial_velocity, final_velocity, acceleration)
                        print(f"The time is {time} seconds.")
                        copy_to_keyboard(time, copy_to_keyboard_true)
                    else:
                        print("Invalid operation!Please try again.")
                        continue
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif operation == 2:
                operation = calc("Ratio calc",["Finding all amounts in ratio","Finding total of ratio and unknwon amounts","Listing equinvant ratios","Expressing ratios in the form 1:n"],2)
                if operation == 1:
                    print("You have selected Finding all amounts in ratio!")
                    ratio = input("Enter the ratio (e.g. 2:3): ")
                    total_amount = float(input("Enter the total amount: "))
                    ratio_parts = ratio.split(":")
                    ratio_sum = sum(int(part) for part in ratio_parts)
                    amounts = [int(part) / ratio_sum * total_amount for part in ratio_parts]
                    print(f"The amounts are: {amounts}")
                    copy_to_keyboard(amounts, copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Finding total of ratio and unknwon amounts!")
                    ratio = input("Enter the ratio with known value at forefront(eg.2:3,2 being known): ")
                    part = input("Enter value of known part: ")
                    ratio_parts = ratio.split(":")
                    ratio_parts = [int(x) for x in ratio_parts]
                    total_parts = sum(ratio_parts)
                    known_part = ratio_parts[0]
                    known_part_value = int(part)
                    total_amount = (known_part_value * total_parts) / known_part
                    # Calculate the total amount based on the ratio and known part
                    # Print the result
                    print(f"The total amount is: {total_amount}")
                    print("The unknwown parts are:")
                    unknown_parts_list = []
                    for i in range(1, len(ratio_parts)):
                        unknown_part = ratio_parts[i]
                        unknown_part_value = (unknown_part * total_amount) / total_parts
                        print(f"Part {i + 1}: {unknown_part_value}")
                        unknown_parts_list.append(unknown_part_value)
                    copy_to_keyboard(f"{unknown_parts_list},{total_amount}", copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Listing equinvant ratios!")
                    ratio = input("Enter the ratio (e.g. 2:3): ")
                    number = int(input("Enter the number of equivalent ratios to generate(from it's simplest form): "))
                    ratio_parts = ratio.split(":")
                    ratio_parts = [int(x) for x in ratio_parts]
                    ratio_sum = sum(ratio_parts)
                    equivalent_ratios = []
                    for i in range(1, number + 1):
                        equivalent_ratio = [part * i for part in ratio_parts]
                        equivalent_ratios.append(":".join(map(str, equivalent_ratio)))
                    print(f"The equivalent ratios are: {equivalent_ratios}")
                    copy_to_keyboard(equivalent_ratios, copy_to_keyboard_true)
                elif operation == 4:
                    print("You have selected Expressing ratios in the form 1:n!")
                    ratio = input("Enter the ratio (e.g. 2:3): ")
                    ratio_parts = ratio.split(":")
                    ratio_parts = [int(x) for x in ratio_parts]
                    first_part = ratio_parts[0]
                    expressed_ratio = [part / first_part for part in ratio_parts]
                    print(f"The ratio in the form 1:n is: {expressed_ratio}")
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif operation == 3:
                print("You have selected Statistics calc(indev)!")
                operation = calc("Statistics calc",["Proprtionality calc","Mean","Median","Mode","Range","Standard Deviation","Variance"],2)
                if operation == 1:
                    print("You have selected Proprtionality calc!")
                    sub_operation = calc("Proportionality calc",["Direct Proportionality","Inverse Proportionality"],1)
                    if sub_operation == 1:
                        print("You have selected Direct Proportionality!")
                        x1 = float(input("Enter the first value of x: "))
                        y1 = float(input("Enter the first value of y: "))
                        x2 = float(input("Enter the second value of x: "))
                        y2 = (y1 * x2) / x1
                        print(f"The second value of y is: {y2}")
                        copy_to_keyboard(y2, copy_to_keyboard_true)
                    elif sub_operation == 2:
                        print("You have selected Inverse Proportionality!")
                        x1 = float(input("Enter the first value of x: "))
                        y1 = float(input("Enter the first value of y: "))
                        x2 = float(input("Enter the second value of x: "))
                        y2 = (x1 * y1) / x2
                        print(f"The second value of y is: {y2}")
                        copy_to_keyboard(y2, copy_to_keyboard_true)
                    else:
                        print("Invalid operation!Please try again.")
                        continue
                elif operation == 2:
                    print("You have selected Mean!")
                    data = input("Enter the data set separated by commas: ")
                    data_list = [float(x) for x in data.split(",")]
                    mean = sum(data_list) / len(data_list)
                    print(f"The mean is: {mean}")
                    copy_to_keyboard(mean, copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Median!")
                    data = input("Enter the data set separated by commas: ")
                    data_list = [float(x) for x in data.split(",")]
                    data_list.sort()
                    n = len(data_list)
                    if n % 2 == 0:
                        median = (data_list[n // 2 - 1] + data_list[n // 2]) / 2
                    else:
                        median = data_list[n // 2]
                    print(f"The median is: {median}")
                    copy_to_keyboard(median, copy_to_keyboard_true)
                elif operation == 4:
                    print("You have selected Mode!")
                    data = input("Enter the data set separated by commas: ")
                    data_list = [float(x) for x in data.split(",")]
                    frequency = {}
                    for item in data_list:
                        if item in frequency:
                            frequency[item] += 1
                        else:
                            frequency[item] = 1
                    mode = max(frequency, key=frequency.get)
                    print(f"The mode is: {mode}")
                    copy_to_keyboard(mode, copy_to_keyboard_true)
                elif operation == 5:
                    print("You have selected Range!")
                    data = input("Enter the data set separated by commas: ")
                    data_list = [float(x) for x in data.split(",")]
                    data_range = max(data_list) - min(data_list)
                    print(f"The range is: {data_range}")
                    copy_to_keyboard(data_range, copy_to_keyboard_true)
                elif operation == 6:
                    print("You have selected Standard Deviation!")
                    data = input("Enter the data set separated by commas: ")
                    data_list = [float(x) for x in data.split(",")]
                    mean = sum(data_list) / len(data_list)
                    variance = sum((x - mean) ** 2 for x in data_list) / len(data_list)
                    standard_deviation = math.sqrt(variance)
                    print(f"The standard deviation is: {standard_deviation}")
                    copy_to_keyboard(standard_deviation, copy_to_keyboard_true)
                elif operation == 7:
                    print("You have selected Variance!")
                    data = input("Enter the data set separated by commas: ")
                    data_list = [float(x) for x in data.split(",")]
                    mean = sum(data_list) / len(data_list)
                    variance = sum((x - mean) ** 2 for x in data_list) / len(data_list)
                    print(f"The variance is: {variance}")
                    copy_to_keyboard(variance, copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif operation == 4:
                operation = calc("Probability calc",["Probability of a outcome","Finding the probability of an event not happening","Relative frequency","Systematic listing of digit probabilities","Finding the total number of outcome using Product Rule","Sample space diagram generator"],2)
                if operation == 1:
                    print("You have selected Probability of a outcome!")
                    favorable_outcomes = int(input("Enter the number of favorable outcomes: "))
                    total_outcomes = int(input("Enter the total number of outcomes: "))
                    probability = favorable_outcomes / total_outcomes
                    print(f"The probability of the outcome is: {probability}")
                    copy_to_keyboard(probability, copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Finding the probability of an event not happening!")
                    favorable_outcomes = int(input("Enter the number of favorable outcomes: "))
                    total_outcomes = int(input("Enter the total number of outcomes: "))
                    probability = 1 - (favorable_outcomes / total_outcomes)
                    print(f"The probability of the event not happening is: {probability}")
                    copy_to_keyboard(probability, copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Relative frequency!")
                    successful_outcomes = int(input("Enter the number of successful outcomes: "))
                    total_trials = int(input("Enter the total number of trials: "))
                    relative_frequency = successful_outcomes / total_trials
                    print(f"The relative frequency is: {relative_frequency}")
                    copy_to_keyboard(relative_frequency, copy_to_keyboard_true)
                elif operation == 4:
                    print("You have selected Systematic listing of digit probabilities!")
                    digits = input("Enter the digits (e.g. 1,2,3): ")
                    digits_list = digits.split(",")
                    total_digits = len(digits_list)
                    probabilities = {digit: 1 / total_digits for digit in digits_list}
                    print(f"The probabilities are: {probabilities}")
                    copy_to_keyboard(probabilities, copy_to_keyboard_true)
                elif operation == 5:
                    print("You have selected Finding the total number of outcome using Product Rule!")
                    events = int(input("Enter the number of events: "))
                    outcomes_per_event = []
                    for i in range(events):
                        outcomes = int(input(f"Enter the number of outcomes for event {i + 1}: "))
                        outcomes_per_event.append(outcomes)
                    total_outcomes = 1
                    for outcomes in outcomes_per_event:
                        total_outcomes *= outcomes
                    print(f"The total number of outcomes is: {total_outcomes}")
                    copy_to_keyboard(total_outcomes, copy_to_keyboard_true)
                elif operation == 6:
                    print("You have selected Sample space diagram generator!")
                    events = int(input("Enter the number of events: "))
                    outcomes_per_event = []
                    for i in range(events):
                        outcomes = input(f"Enter the outcomes for event {i + 1} (e.g. H,T): ")
                        outcomes_list = outcomes.split(",")
                        outcomes_per_event.append(outcomes_list)
                    sample_space = [[]]
                    for outcomes in outcomes_per_event:
                        sample_space = [x + [y] for x in sample_space for y in outcomes]
                    sample_space_strings = [",".join(outcome) for outcome in sample_space]
                    print(f"The sample space is: {sample_space_strings}")
                    copy_to_keyboard(sample_space_strings, copy_to_keyboard_true)
                else:
                    print("Invalid operation!Please try again.")
                    continue
            elif operation == 5:
                calculation = calc("Surds calc",["Simplifying surds","Adding and subtracting surds","Multiplying and dividing surds","Multiplying out brackets including surds","Rationalising the denominator"],2)
                if calculation == 1:
                    print("You have selected Simplifying surds!")
                    expression = input("Enter the surd expression (e.g. sqrt(50)): ")
                    try:
                        simplified_expression = simplify_surd(expression)
                        print(f"The simplified surd is: {simplified_expression}")
                        copy_to_keyboard(simplified_expression, copy_to_keyboard_true)
                    except Exception as e:
                        print(f"Error simplifying surd: {e}")
                        continue
                elif calculation == 2:
                    print("You have selected Adding and subtracting surds!")
                    expression = input("Enter the surd expression (e.g. sqrt(2) + sqrt(8) - sqrt(18)): ")
                    try:
                        result = sp.simplify(expression)
                        print(f"The result of adding/subtracting the surds is: {result}")
                        copy_to_keyboard(result, copy_to_keyboard_true)
                    except Exception as e:
                        print(f"Error in calculation: {e}")
                        continue
                elif calculation == 3:
                    print("You have selected Multiplying and dividing surds!")
                    expression = input("Enter the surd expression (e.g. sqrt(2) * sqrt(8) / sqrt(18)): ")
                    try:
                        result = sp.simplify(expression)
                        print(f"The result of multiplying/dividing the surds is: {result}")
                        copy_to_keyboard(result, copy_to_keyboard_true)
                    except Exception as e:
                        print(f"Error in calculation: {e}")
                        continue
                elif calculation == 4:
                    print("You have selected Multiplying out brackets including surds!")
                    expression = input("Enter the surd expression (e.g. (sqrt(2) + sqrt(3))(sqrt(5) - sqrt(7))): ")
                    try:
                        result = sp.expand(expression)
                        print(f"The result of multiplying out the brackets is: {result}")
                        copy_to_keyboard(result, copy_to_keyboard_true)
                    except Exception as e:
                        print(f"Error in calculation: {e}")
                        continue
                elif calculation == 5:
                    print("You have selected Rationalising the denominator!")
                    expression = input("Enter the surd expression (e.g. 1/sqrt(2) + 1/(sqrt(3) + sqrt(5))): ")
                    try:
                        result = sp.simplify(expression)
                        print(f"The result of rationalising the denominator is: {result}")
                        copy_to_keyboard(result, copy_to_keyboard_true)
                    except Exception as e:
                        print(f"Error in calculation: {e}")
                        continue
                else:
                    print("Invalid calculation!Please try again.")
                    continue
        elif category == 15:
            print("Legal Info on ULTIMATE CALC™")
            print(f"ULTIMATE CALC™(Version {version}) is a trademark of M0bile132022.")
            print("© 2025 M0bile132022. All rights reserved.")
            print("This program is protected by the GNU General Public License v3.0.")
            print("This program is provided as is with no warranty.")
            print("For more information, visit https://www.ultimatecalc.com.")
            print("Other statstics:")
            print(f"Lines of code: {line_count}")
            print(f"Size:{file_size} bytes")
            print(f"Version: {version}")
            print(f"File path: {file_path}")
            copy_to_keyboard(f"ULTIMATE CALC™(Version {version}) is a trademark of M0bile132022.© 2025 M0bile132022. All rights reserved. This program is protected by the GNU General Public License v3.0. This program is provided as is with no warranty. For more information, visit https://www.ultimatecalc.com. Other statstics: Lines of code: {count_lines(file_path)} Size:{file_size} bytes Version: {version} File path: {file_path}", copy_to_keyboard_true)
            print("""Credits:
            1. M0bile132022 for code
            2. OpenAI for aid
            3. Python community for possiblity
            4. SymPy for the real complicated stuff
            5. Math community for purpose
            6. Stack Overflow for help
            7. GitHub community for storage
            8. Wikipedia for knowledge
            9. Yzfargo for 3rd party subroutines
            10. You for using it!!!""")
            
        elif category == 16:
            print("Welcome to settings!")
            print("Please select an operation:")
            print("""1. Change the lenght units
    2. Change the area units
    3. Change the volume units
    4. Change the money units
    5.Copy to keyboard setting""")
            operation = int(input("Enter the number of the operation you want to perform: "))
            if operation == 1:
                print("You have selected Change the lenght units!")
                print("Please select a unit:")
                print("""1. Metres
                    2. Centimetres
                    3. Millimetres
                    4. Kilometres
                    5. Inches
                    6. Feet
                    7. Yards
                    8. Miles""")
                unit = int(input("Enter the number of the unit you want to use: "))
                if unit == 1:
                    lenght_units = "m"
                elif unit == 2:
                    lenght_units = "cm"
                elif unit == 3:
                    lenght_units = "mm"
                elif unit == 4:
                    lenght_units = "km"
                elif unit == 5:
                    lenght_units = "in"
                elif unit == 6:
                    lenght_units = "ft"
                elif unit == 7:
                    lenght_units = "yd"
                elif unit == 8:
                    lenght_units = "mi"
                else:
                    print("Invalid unit!Please try again.")
                    continue
            elif operation == 2:
                print("You have selected Change the area units!")
                print("Please select a unit:")
                print("""1. Square metres
                    2.Square centimetres
                    3. Square millimetres
                    4. Square kilometres
                    5. Square inches
                    6. Square feet
                    7. Square yards
                    8. Square miles""")
                unit = int(input("Enter the number of the unit you want to use: "))
                if unit == 1:
                    area_units = "m²"
                elif unit == 2:
                    area_units = "cm²"
                elif unit == 3:
                    area_units = "mm²"
                elif unit == 4:
                    area_units = "km²"
                elif unit == 5:
                    area_units = "in²"
                elif unit == 6:
                    area_units = "ft²"
                elif unit == 7:
                    area_units = "yd²"
                elif unit == 8:
                    area_units = "mi²"
                else:
                    print("Invalid unit!Please try again.")
                    continue
            elif operation == 3:
                print("You have selected Change the volume units!")
                print("Please select a unit:")
                print("""1. Cubic metres
                    2. Cubic centimetres
                    3. Cubic millimetres
                    4. Cubic kilometres
                    5. Cubic inches
                    6. Cubic feet
                    7. Cubic yards
                    8. Cubic miles""")
                unit = int(input("Enter the number of the unit you want to use: "))
                if unit == 1:
                    volume_units = "m³"
                elif unit == 2:
                    volume_units = "cm³"
                elif unit == 3:
                    volume_units = "mm³"
                elif unit == 4:
                    volume_units = "km³"
                elif unit == 5:
                    volume_units = "in³"
                elif unit == 6:
                    volume_units = "ft³"
                elif unit == 7:
                    volume_units = "yd³"
                elif unit == 8:
                    volume_units = "mi³"
                else:
                    print("Invalid unit!Please try again.")
                    continue
            elif operation == 4:
                print("You have selected Change the money units!")
                print("Please select a unit:")
                print("""1. Pounds
                    2. Dollars
                    3. Euros
                    4. Yen/Yuan
                    5. Rupees
                    6. Ruble
                    7. Won""")
                unit = int(input("Enter the number of the unit you want to use: "))
                if unit == 1:
                    money_units = "£"
                elif unit == 2:
                    money_units = "$"
                elif unit == 3:
                    money_units = "€"
                elif unit == 4:
                    money_units = "¥"
                elif unit == 5:
                    money_units = "₹"
                elif unit == 6:
                    money_units = "₽"
                elif unit == 7:
                    money_units = "₩"
                else:
                    print("Invalid unit!Please try again.")
                    continue
            elif operation == 5:
                print("You have selected Copy to keyboard setting!")
                print("Please select an operation:")
                print("""1. Enable
    2. Disable""")
                operation = int(input("Enter the number of the operation you want to perform: "))
                if operation == 1:
                    copy_to_keyboard_true = True
                    print("Copy to keyboard has been enabled.") 
                elif operation == 2:
                    copy_to_keyboard_true = False
                    print("Copy to keyboard has been disabled.")
                else:
                    print("Invalid operation!Please try again.")
                    continue

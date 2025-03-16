   
#THE ULTIMATE CALC 
#By: @M0bile132022
#Date: 2025-03-11
#Version: 2.0.1
#Milestones:
#UPDATE 2.0:11/03/2025
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
#Note: This is a calculator that can do a lot of things, so don't be surprised if you see a lot of code.
#Note: This is a calculator that can do a lot of things, so don't be surprised if you see a lot of code.
import math
import time
import os
import fractions
import pyperclip

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
#Alt functions
def find_x_intercept(m, b):
    if m == 0:
        print("The slope (m) cannot be zero for a valid x-intercept.")
        return None
    x_intercept = -b / m
    return x_intercept
file_path = os.path.abspath(__file__)
file_size = os.path.getsize(file_path)
version = 2.0
lenght_units = "Line units"
angle_units = "Angle units"
volume_units = "Cubic units"
area_units = "Area units"
money_units = "Money units"
time_units = "Time units"
copy_to_keyboard_true = True
if __name__ == "__main__": 
    while True:
        print(f"Welcome to the ULTIMATE calc Ver {version}!")
        print("""Please select a category:
        1. Surface Area and Volume
        2. Pythagoras therom
        3. Perimiter and Area(P:A ratio)
        4. Standard form
        5. The Basics
        6. Ordering/Mass operations
        7. Scale factors
        8. Decimal to fraction to percentage conversions
        9. Intrest
        10. Trigomentry
        11. Lines(beta)
        13. Legal/Other Info on ULTIMATE CALC™
        14. Settings
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
                    print(f"The surface area of the cylinder is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    radius = float(input("Enter the radius of the cylinder: "))
                    height = float(input("Enter the height of the cylinder: "))
                    vol = pi * (radius ** 2) * height
                    print(f"The volume of the cylinder is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the cylinder: "))
                    height = float(input("Enter the height of the cylinder: "))
                    sa = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
                    vol = pi * (radius ** 2) * height
                    ratio = sa / vol
                    print(f"The surface area of the cylinder is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                    print(f"The volume of the cylinder is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
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
                    print(f"The surface area of the cone is {sa} {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    radius = float(input("Enter the radius of the cone: "))
                    height = float(input("Enter the height of the cone: "))
                    vol = (1/3) * pi * (radius ** 2) * height
                    print(f"The volume of the cone is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the cone: "))
                    height = float(input("Enter the height of the cone: "))
                    slant_height = float(input("Enter the slant height:"))
                    sa = pi * radius * (radius + slant_height)
                    vol = (1/3) * pi * (radius ** 2) * height
                    ratio = sa / vol
                    print(f"The surface area of the cone is {sa} {area_units}")
                    print(f"The volume of the cone is {vol} {volume_units}.")
                    print(f"The SA:VOL ratio of the cone is {ratio}.")
                    copy_to_keyboard(f"{sa},{vol},{ratio}",copy_to_keyboard_true)
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
                    print(f"The surface area of the sphere is {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Volume!")
                    radius = float(input("Enter the radius of the sphere: "))
                    vol = (4/3) * pi * (radius ** 3)
                    print(f"The volume of the sphere is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the sphere: "))
                    sa = 4 * pi * (radius ** 2)
                    vol = (4/3) * pi * (radius ** 3)
                    ratio = sa / vol
                    print(f"The surface area of the sphere is {area_units}.")
                    copy_to_keyboard(sa,copy_to_keyboard_true)
                    print(f"The volume of the sphere is {vol} {volume_units}.")
                    copy_to_keyboard(vol,copy_to_keyboard_true)
                    print(f"The SA:VOL ratio of the sphere is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
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
                    print(f"The perimiter of the circle is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    radius = float(input("Enter the radius of the circle: "))
                    area = pi * (radius ** 2)
                    print(f"The area of the circle is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the circle: "))
                    perimiter = 2 * pi * radius
                    area = pi * (radius ** 2)
                    ratio = perimiter / area
                    print(f"The perimiter of the circle is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                    print(f"The area of the circle is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                    print(f"The P:A ratio of the circle is {ratio}.")
                    copy_to_keyboard(ratio,copy_to_keyboard_true)
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
                    print("The perimiter of the semicircle is {perimiter} {lenght_units}.")
                    copy_to_keyboard(perimiter,copy_to_keyboard_true)
                elif operation == 2:
                    print("You have selected Area!")
                    radius = float(input("Enter the radius of the semicircle: "))
                    area = (1/2) * pi * (radius ** 2)
                    print(f"The area of the semicircle is {area} {area_units}.")
                    copy_to_keyboard(area,copy_to_keyboard_true)
                elif operation == 3:
                    print("You have selected Both!")
                    radius = float(input("Enter the radius of the semicircle: "))
                    perimiter = (pi * radius) + (2 * radius)
                    area = (1/2) * pi * (radius ** 2)
                    ratio = perimiter / area
                    print(f"The perimiter of the semicircle is {perimiter} {lenght_units}.")
                    print(f"The area of the semicircle is {area} {area_units}.")
                    print("The P:A ratio is {ratio}.")
                    copy_to_keyboard(f"{perimiter},{area},{ratio}",copy_to_keyboard_true)
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
    10. Tan()""")
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
                print("Standard Multiplication grid:")
                # Define the size of the times table grid
                size = 20

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

            else:
                print("Invalid operation!Please try again.")
                continue 
        elif category == 6:
            print("Welcome to the Ordering category!")
            print("Please select an operation:")
            print("""1. Ascending order
    2. Descending order""")
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
    8. Calcuate gradient of parallel line""")
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
                print(f"The gradient of the perpendicular line is {perpendicular_gradient}.")
            elif operation == 8:
                print("The gradient of the parallel line is the same as the other line!")
            else:
                print("Invalid operation!Please try again.")
                continue

        elif category == 12:
            print("Circles will be added soon!(Update 2.0)")
            continue
        
        elif category == 13:
            continue
            # This category split into two parts: Planet > earth (and vice versa(noting earth>planet will do it in days)) then optional prompt to convert converted time to different units
            # 1 SOLAR day on mercury = 176 days on earth/4224 hours on earth/253440 minutes on earth/15206400 seconds on earth/25.4 weeks on earth/5.7 months on earth/0.48 years on earth
            # 1 SOLAR hour on mercury = 7.33 days on earth
            # 1 SOLAR minute on mercury = 0.122 days on earth
            # 1 SOLAR second on mercury = 0.00203 days on earth
            # 1 SOLAR week on mercury = 1232 days on earth
            # 1 SOLAR month on mercury(1/12 of year as has no moon) = 7.33 days on earth
            # 1 SOLAR year on mercury = 88 days on earth
            # 1 SOLAR day on Venus = 117 days on earth
            # 1 SOLAR day on Mars = 1.03 days on earth
            print("Welcome to the Planetary time category!")
            print("Please note, that this is an experimental category and may not be accurate.")
            print("Please aslo note this calcuator is based off solar time, as we would use on Earth")
            print("Please select a planet/celestial body:")
            print("""1. Mercury
    2. Venus
    3. Earth
    4. Moon
    5. Mars
    6. Phobos
    7. Deimos
    8. Jupiter
    9. Saturn
    10. Uranus
    11. Neptune
    12. Pluto
    13. Ceres
    14. Sun""")
            planet = int(input("Enter the number of the planet you want to use: "))
            if planet == 1:
                print("You have selected Mercury!")
                print("Please select an operation:")
                print("""1. Convert a period of Earth time to Mercury time
        2. Convert a period of Mercury time to Earth time""")
                operation = int(input("Enter the number of the operation you want to perform: "))
                if operation == 1:
                    print("You have selected Convert a period of Earth time to Mercury time!")
                    print("Please chose a unit of Earth time:")
                    print("""1. Seconds
        2. Minutes
        3. Hours
        4. Days
        5. Weeks
        6. Months
        7. Years""")
                    unit = int(input("Enter the number of the unit you want to use: "))
                    earth_time = float(input("Enter the period of Earth time: "))
                    if unit == 1:
                        mercury_time = earth_time / 15206400
                    elif unit == 2:
                        mercury_time = earth_time / 253440
                    elif unit == 3:
                        mercury_time = earth_time / 4224
                    elif unit == 4:
                        mercury_time = earth_time / 176
                    elif unit == 5:
                        mercury_time = earth_time / 25.4
                    elif unit == 6:
                        mercury_time = earth_time / 5.7
                    elif unit == 7:
                        mercury_time = earth_time / 0.48
                    else:
                        print("Invalid unit!Please try again.")
                        continue


        

                
                

            

                

        elif category == 14:
            print("Legal Info on ULTIMATE CALC™")
            print("ULTIMATE CALC™(Version 1.53) is a trademark of M0bile132022.")
            print("© 2025 M0bile132022. All rights reserved.")
            print("This program is protected by the GNU General Public License v3.0.")
            print("This program is provided as is with no warranty.")
            print("For more information, visit https://www.ultimatecalc.com.")
            print("Other statstics:")
            print(f"Lines of code: {count_lines(file_path)}")
            print(f"Size:{file_size} bytes")
            print(f"Version: {version}")
            print(f"File path: {file_path}")
            copy_to_keyboard(f"ULTIMATE CALC™(Version {version}) is a trademark of M0bile132022.© 2025 M0bile132022. All rights reserved. This program is protected by the GNU General Public License v3.0. This program is provided as is with no warranty. For more information, visit https://www.ultimatecalc.com. Other statstics: Lines of code: {count_lines(file_path)} Size:{file_size} bytes Version: {version} File path: {file_path}", copy_to_keyboard_true)
        elif category == 15:
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

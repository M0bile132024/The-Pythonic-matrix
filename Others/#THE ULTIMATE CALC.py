#THE ULTIMATE CALC 
#By: @M0bile132022
#Date: 2025-02-2
#Version: 1.631
'''Description: This is a ULTIMATE calculator that can perform ULTIMATE operations such as SA:VOL, 
PHYSIC EQUATIONS, , 
pythagoras therom,
Perimiter/Area,
The basics,
Ordering,
Scale factors,
Decimal to fraction to percentage conversions,
Planetary time and arcs/sectors/chords(included in others(in a future update)),
Standard form and more!
'''
#Note: This is a calculator that can do a lot of things, so don't be surprised if you see a lot of code.
#Note: This is a calculator that can do a lot of things, so don't be surprised if you see a lot of code.
#Note: This is a calculator that can do a lot of things, so don't be surprised if you see a lot of code.
import math
import os
import fractions
import tkinter

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
file_path = os.path.abspath(__file__)
file_size = os.path.getsize(file_path)
version = 1.63
lenght_units = "Line units"
angle_units = "Angle units"
volume_units = "Cubic units"
area_units = "Area units"
while True:
    print("Welcome to the ULTIMATE calc!")
    print("""Please select a category:
    1. Surface Area and Volume
    2. Pythagoras therom
    3. Perimiter and Area(P:A ratio)
    4. Standard form
    5. The Basics
    6. Ordering
    7. Scale factors
    8. Decimal to fraction to percentage conversions
    9. Legal Info on ULTIMATE CALC™
    10. Settings(unavailable as of ver 1.631)
    More functions are coming soon!!!!!""")
    category = int(input("Enter the number of the category you want to use: "))
    

    if category == 1:
        print("Welcome to the Surface Area and Volume category!")
        print("""Please select a shape:
        1. Cube
        2. Rectangular Prism
        3. Cylinder
        4. Cone
        5. Sphere""")
        shape = int(input("Enter the number of the shape you want to use: "))
        if shape == 1:
            print("You have selected the Cube!")
            operation = operation_dialogue()
            if operation == 1:
                print("You have selected Surface Area!")
                side = float(input("Enter the side length of the cube: "))
                sa = 6 * (side ** 2)
                print(f"The surface area of the cube is {sa} {area_units}.")
            elif operation == 2:
                print("You have selected Volume!")
                side = float(input("Enter the side length of the cube: "))
                vol = side ** 3
                print(f"The volume of the cube is {vol} cubic units.")
            elif operation == 3:
                print("You have selected Both!")
                side = float(input("Enter the side length of the cube: "))
                sa = 6 * (side ** 2)
                vol = side ** 3
                ratio = sa / vol
                print(f"The surface area of the cube is {sa} {area_units}.")
                print(f"The volume of the cube is {vol} cubic units.")
                print(f"The SA:VOL ratio of the cube is {ratio}.")
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
                print(f"The surface area of the rectangular prism is {area_units}.")
            elif operation == 2:
                print("You have selected Volume!")
                length = float(input("Enter the length of the rectangular prism: "))
                width = float(input("Enter the width of the rectangular prism: "))
                height = float(input("Enter the height of the rectangular prism: "))
                vol = length * width * height
                print(f"The volume of the rectangular prism is {vol} cubic units.")
            elif operation == 3:
                print("You have selected Both!")
                length = float(input("Enter the length of the rectangular prism: "))
                width = float(input("Enter the width of the rectangular prism: "))
                height = float(input("Enter the height of the rectangular prism: "))
                sa = 2 * ((length * width) + (width * height) + (height * length))
                vol = length * width * height
                ratio = sa / vol
                print(f"The surface area of the rectangular prism is {sa}.")
                print(f"The volume of the rectangular prism is {vol} cubic units.")
                print(f"The SA:VOL ratio of the rectangular prism is {ratio}.")
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
                print(f"The surface area of the cylinder is {area_units}.")
            elif operation == 2:
                print("You have selected Volume!")
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                vol = pi * (radius ** 2) * height
                print(f"The volume of the cylinder is {vol} cubic units.")
            elif operation == 3:
                print("You have selected Both!")
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                sa = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
                vol = pi * (radius ** 2) * height
                ratio = sa / vol
                print(f"The surface area of the cylinder is {area_units}.")
                print(f"The volume of the cylinder is {vol} cubic units.")
                print(f"The SA:VOL ratio of the cylinder is {ratio}.")
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
                print(f"The surface area of the cone is {area_units}.")
            elif operation == 2:
                print("You have selected Volume!")
                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                vol = (1/3) * pi * (radius ** 2) * height
                print(f"The volume of the cone is {vol} cubic units.")
            elif operation == 3:
                print("You have selected Both!")
                radius = float(input("Enter the radius of the cone: "))
                height = float(input("Enter the height of the cone: "))
                sa = pi * radius * (radius + slant_height)
                vol = (1/3) * pi * (radius ** 2) * height
                ratio = sa / vol
                print(f"The surface area of the cone is {area_units}.")
                print(f"The volume of the cone is {vol} cubic units.")
                print(f"The SA:VOL ratio of the cone is {ratio}.")
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
            elif operation == 2:
                print("You have selected Volume!")
                radius = float(input("Enter the radius of the sphere: "))
                vol = (4/3) * pi * (radius ** 3)
                print(f"The volume of the sphere is {vol} cubic units.")
            elif operation == 3:
                print("You have selected Both!")
                radius = float(input("Enter the radius of the sphere: "))
                sa = 4 * pi * (radius ** 2)
                vol = (4/3) * pi * (radius ** 3)
                ratio = sa / vol
                print(f"The surface area of the sphere is {area_units}.")
                print(f"The volume of the sphere is {vol} cubic units.")
                print(f"The SA:VOL ratio of the sphere is {ratio}.")
            else:
                print("Invalid operation!Please try again.")
                continue 
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
            print(f"The length of the hypotenuse is {hypotenuse}.")
        elif operation == 2:
            print("You have selected Calculate one of the other sides!")
            side1 = float(input("Enter the length of the hypotnuse: "))
            side2 = float(input("Enter the length of the side known: "))
            unknown_side = math.sqrt((side1 ** 2) - (side2 ** 2))
            print(f"The length of the unknown side is {unknown_side}.")
        else:
            print("Invalid operation!Please try again.")
            continue 
    elif category == 3:
        print("Welcome to the Perimiter and Area category!")
        print("""Please select a shape:
        1. Square
        2. Rectangle
        3. Triangle
        4. Circle""")
        shape = int(input("Enter the number of the shape you want to use: "))
        if shape == 1:
            operation = twod_operation_dialogue("Square")
            if operation == 1:
                print("You have selected Perimiter!")
                side = float(input("Enter the length of a side of the square: "))
                perimiter = 4 * side
                print(f"The perimiter of the square is {perimiter} units.")
            elif operation == 2:
                print("You have selected Area!")
                side = float(input("Enter the length of a side of the square: "))
                area = side ** 2
                print(f"The area of the square is{area_units}.")
            elif operation == 3:
                print("You have selected Both!")
                side = float(input("Enter the length of a side of the square: "))
                perimiter = 4 * side
                area = side ** 2
                ratio = perimiter / area
                print(f"The perimiter of the square is {perimiter} units.")
                print(f"The area of the square is{area_units}.")
                print(f"The P:A ratio of the square is {ratio}.")
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
                print(f"The perimiter of the rectangle is {perimiter} units.")
            elif operation == 2:
                print("You have selected Area!")
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = length * width
                print(f"The area of the rectangle is{area_units}.")
            elif operation == 3:
                print("You have selected Both!")
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                perimiter = 2 * (length + width)    
                area = length * width
                ratio = perimiter / area
                print(f"The perimiter of the rectangle is {perimiter} units.")
                print(f"The area of the rectangle is{area_units}.")
                print(f"The P:A ratio of the rectangle is {ratio}.")
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
                print(f"The perimiter of the triangle is {perimiter} units.")
            elif operation == 2:
                print("You have selected Area!")
                base = float(input("Enter the length of the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = (1/2) * base * height
                print(f"The area of the triangle is{area_units}.")
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
                print(f"The perimiter of the triangle is {perimiter} units.")
                print(f"The area of the triangle is{area_units}.")
                print(f"The P:A ratio of the triangle is {ratio}.")
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
                print(f"The perimiter of the circle is {perimiter} units.")
            elif operation == 2:
                print("You have selected Area!")
                radius = float(input("Enter the radius of the circle: "))
                area = pi * (radius ** 2)
                print(f"The area of the circle is {area_units}.")
            elif operation == 3:
                print("You have selected Both!")
                radius = float(input("Enter the radius of the circle: "))
                perimiter = 2 * pi * radius
                area = pi * (radius ** 2)
                ratio = perimiter / area
                print(f"The perimiter of the circle is {perimiter} units.")
                print(f"The area of the circle is {area_units}.")
                print(f"The P:A ratio of the circle is {ratio}.")
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
        elif operation == 2:
            print("You have selected Convert from standard form!")
            try:
                number = input("Enter the number you want to convert from standard form(ENG notation): ")
                number = float(number)
                print(f"The number in standard form is {number}.")
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
6. Square/cube/any root""")
        operation = int(input("Enter the number of the operation you want to perform: "))
        if operation == 1:
            print("You have selected Addition!")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print(f"The sum of the two numbers is {result}.")
        elif operation == 2:
            print("You have selected Subtraction!")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print(f"The difference of the two numbers is {result}.")
        elif operation == 3:
            print("You have selected Multiplication!")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"The product of the two numbers is {result}.")
        elif operation == 4:
            print("You have selected Division!")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"The quotient of the two numbers is {result}.")
        elif operation == 5:
            print("You have selected Exponents!")
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            result = num1 ** num2
            print(f"The result of the exponent is {result}.")
        elif operation == 6:
            print("You have selected Square/Cube/Any root!")
            num = float(input("Enter the number you want to find the root of: "))
            root = float(input("Enter the root you want to find of the number: "))
            result = num ** (1/root)
            print(f"The {root} root of the number is {result}.")
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
        elif operation == 2:
            print("You have selected Calculate the new length!")
            original_length = float(input("Enter the original length: "))
            scale_factor = float(input("Enter the scale factor: "))
            new_length = original_length * scale_factor
            print(f"The new length is {new_length}.")
        elif operation == 3:
            print("You have selected Calculate the original length!")
            new_length = float(input("Enter the new length: "))
            scale_factor = float(input("Enter the scale factor: "))
            original_length = new_length / scale_factor
            print(f"The original length is {original_length}.")
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
        elif operation == 2:
            print("You have selected Fraction to decimal!")
            numerator = float(input("Enter the numerator of the fraction: "))
            denominator = float(input("Enter the denominator of the fraction: "))
            decimal = numerator / denominator
            print(f"The decimal is {decimal}.")
        elif operation == 3:
            print("You have selected Decimal to percentage!")
            decimal = float(input("Enter the decimal you want to convert to a percentage: "))
            percentage = decimal * 100
            print(f"The percentage is {percentage}%.")
        elif operation == 4:
            print("You have selected Percentage to decimal!")
            percentage = float(input("Enter the percentage you want to convert to a decimal: "))
            decimal = percentage / 100
            print(f"The decimal is {decimal}.")
        elif operation == 5:
            print("You have selected Fraction to percentage!")
            numerator = float(input("Enter the numerator of the fraction: "))
            denominator = float(input("Enter the denominator of the fraction: "))
            percentage = (numerator / denominator) * 100
            print(f"The percentage is {percentage}%.")
        elif operation == 6:
            print("You have selected Percentage to fraction!")
            percentage = float(input("Enter the percentage you want to convert to a fraction: "))
            fraction = fractions.Fraction(percentage / 100).limit_denominator()
            print(f"The fraction is {fraction}.")
        else:
            print("Invalid operation!Please try again.")
            continue
    elif category == 9:
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
#Note:Category 10 under consturction
'''    elif category == 10:
        print("Settings")
        print("Please select an operation:")
        print("""1.Change units
2.Copy answer to keyboard""")
        operation = int(input("Enter the number of the operation you want to perform: "))
        if operation == 1:
            print("You have selected Change units!")
            print("Please select a unit to change:")
            print("""1. Length
2.Angle
3.Volume
4.Area""")
            unit = int(input("Enter the number of the unit you want to change: "))
            if unit == 1:
                print("You have selected Length!")
                print("Please select the current unit:(Default is lenght units)")
                print("""1. Meters
2. Kilometers
3. Centimeters
4. Millimeters
5. Inches
6. Feet
7. Yards
8. Miles""")
                current_unit = int(input("Enter the number of the current unit: "))
                print("Please select the new unit:(Default is lenght units)")'''
                
   



            
            



# THE ULTIMATE TRACK(er)
#Date:16/03/2025
#Version:Beta(not tested) 1.1
#Author:M0bile132022
''' Description:This is an ULTIMATE tracker that can track ULTIMATE things
such as:
1. Sparxs bookwork'''
import time
import json
import os
import pyperclip

#Function to copy text to keyboard

def copy_to_keyboard(text,true_or_false):
    if true_or_false == True:    
        pyperclip.copy(text)
        print("Text copied sucessfully")
copy_to_keyboard_true = True
version = 1.2
bookwork_ID = []
bookwork_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0
j = 0
question = 1
name = ""
while True:
    print(f"Welcome to the Ultimate Tracker Ver:Beta {version}!")
    print("Please chose an category you wish to do:")
    print("""1. Track Sparxs bookwork
    More will be added soon""")
    category = int(input("Please chose an operation:"))
    if category == 1:
        while True:
        
            print("You have chosen to track Sparxs bookwork")
            print("Please chose an operation you wish to do:")
            print("""1. Add bookwork
            2. View recorded bookwork
            3. Find a bookwork
            4. Update a bookwork
            5. Delete a bookwork
            6. Exit the program(Note:Will not save if exited)
            7.Save current bookwork as
            8. Save current bookwork(to last save file)
            9.Load new bookwork(will override current bookwork)""")
            operation = int(input("Please chose an operation:"))
            if operation == 1:
                print("You have chosen to add bookwork")
                print("Type 'exit' to exit,'next' to move to the next question,or 'chose' to chose a question")
                
                while True:
                    if f"{question}{alphabet[i]}" in bookwork_ID:
                        i += 1
                        continue
                    bookwork_ID.append(f"{question}{alphabet[i]}")
                    bookwork = input(f"Please input the bookwork for {bookwork_ID[j]}:")
                    if bookwork == "exit":
                        bookwork_ID.pop()
                        break
                    elif bookwork == "next":
                        bookwork_ID.pop()
                        question += 1
                        i = 0
                        print("Moving onto next question")
                        continue
                    elif bookwork == "chose":
                        bookwork_ID.pop()
                        while True:
                            question = int(input("Please input the question number you wish to chose:"))
                            letter = str(input("Please input the letter of the alphabet you wish to chose:"))
                            while letter not in alphabet:
                                letter = str(input("Please input a valid letter of the alphabet you wish to chose:"))
                            #check if id already exists
                            i = alphabet.index(letter)
                            if f"{question}{letter}" in bookwork_ID:
                                input = input("ID already exists.Press enter to try again,or type 'update' to update the bookwork")
                                if input == "update":
                                    bookwork_list[bookwork_ID.index(f"{question}{letter}")] = input(f"Please input the new bookwork for {f'{question}{letter}'}:")
                                continue
                            else:
                                break
                        
                        print("Question chosen")
                        continue
                    else:
                        bookwork_list.append(bookwork)
                        print("Bookwork added")
                        i += 1
                        j += 1
                    if i == 26:
                        i = 0
                        question += 1
                print("Bookwork sucessfully added")
            elif operation == 2:
                print("You have chosen to view recorded bookwork:")
                if len(bookwork_list) == 0:
                    print("Your bookwork list is currently empty.Please try adding some new bookwork")
                else:
                    temp_dict = {}
                    for k in range(len(bookwork_list)):
                        print(f"Bookwork {bookwork_ID[k]}:{bookwork_list[k]}")
                        temp_dict[bookwork_ID[k]] = bookwork_list[k]
                    copy_to_keyboard(json.dumps(temp_dict),copy_to_keyboard_true)
            elif operation == 3:
                print("You have chosen to find a bookwork")
                find = input("Please input the bookwork ID you wish to find:")
                if find in bookwork_ID:
                    print(f"Bookwork {find}:{bookwork_list[bookwork_ID.index(find)]}")
                    copy_to_keyboard(bookwork_list[bookwork_ID.index(find)],copy_to_keyboard_true)
                else:
                    print("Bookwork not found")
            elif operation == 4:
                print("You have chosen to update a bookwork")
                update = input("Please input the bookwork ID you wish to update:")
                if update in bookwork_ID:
                    bookwork_list[bookwork_ID.index(update)] = input(f"Please input the new bookwork for {update}:")
                    print("Bookwork updated")
                else:
                    print("Bookwork not found")
            elif operation == 5:
                print("You have chosen to delete a bookwork")
                delete = input("Please input the bookwork ID you wish to delete:")
                if delete in bookwork_ID:
                    bookwork_list[bookwork_ID.index(delete)] = ""
                    bookwork_ID.remove(delete)
                    print("Bookwork deleted")
                else:
                    print("Bookwork not found")
            elif operation == 6:
                print("Exiting the program")
                time.sleep(1)
                break
            elif operation == 7:
                print("You have chosen to save the current bookwork")
                name = input("Please input a name of the file you wish to save the bookwork to:")
                #validate the name
                if name == "":
                    print("Invalid name.Please try again")
                    continue
                with open(f"{name}.json","w") as f:
                    json.dump({"bookwork_list": bookwork_list, "bookwork_ID": bookwork_ID}, f)
            elif operation == 8:
                print("You have chosen to save the current bookwork to the last save file")
              

                #need to delete old stuff in file/delete old file
                with open(f"{name}.json","w") as f:
                    if name in os.listdir():
                        os.remove(f"{name}.json")
                        json.dump({"bookwork_list": bookwork_list, "bookwork_ID": bookwork_ID,"Question":question,"Letter":i,"Iterations":j}, f)
            elif operation == 9:
                print("You have chosen to load new bookwork")
                name = input("Please input the name of the file you wish to load the bookwork from:")
                #check if the file exists
                if name in os.listdir():
                    with open(f"{name}.json","r") as f:
                        data = json.load(open(f"{name}.json", "r"))
                        bookwork_list = data["bookwork_list"]
                        bookwork_ID = data["bookwork_ID"]
                        question = data["Question"]
                        i = data["Letter"]
                        j = data["Iterations"]
                    print("Bookwork loaded")
                else:
                    print("File not found")

    else:
        print("Invalid input.Please try again.")


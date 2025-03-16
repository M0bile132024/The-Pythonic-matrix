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
#will come in handy later
from THE_ULTIMATE_CALC import copy_to_keyboard, copy_to_keyboard_true
version = 1.1
bookwork_ID = []
bookwork_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0
j = 0
question = 1
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
            7.Save current bookwork
            8.Load new bookwork""")
            operation = int(input("Please chose an operation:"))
            if operation == 1:
                print("You have chosen to add bookwork")
                print("Type 'exit' to exit,and 'next' to move to the next question")
                
                while True:
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
                    else:
                        bookwork_list.append(bookwork)
                        print("Bookwork added")
                        i += 1
                        j += 1
                    if i == 26:
                        i = 0
                print("Bookwork sucessfully added")
            elif operation == 2:
                print("You have chosen to view recorded bookwork:")
                if len(bookwork_list) == 0:
                    print("Your bookwork list is currently empty.Please try adding some new bookwork")
                else:
                    for k in range(len(bookwork_list)):
                        print(f"Bookwork {bookwork_ID[k]}:{bookwork_list[k]}")
                    copy_to_keyboard(bookwork_list,copy_to_keyboard_true)
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
                with open(f"{name}.json","w") as f:
                    json.dump({"bookwork_list": bookwork_list, "bookwork_ID": bookwork_ID}, f)
            elif operation == 8:
                print("You have chosen to load new bookwork")
                name = input("Please input the name of the file you wish to load the bookwork from:")
                #check if the file exists
                if name in os.listdir():
                    with open(f"{name}.json","r") as f:
                        data = json.load(open(f"{name}.json", "r"))
                        bookwork_list = data["bookwork_list"]
                        bookwork_ID = data["bookwork_ID"]
                    print("Bookwork loaded")
                else:
                    print("File not found")

    else:
        print("Invalid input.Please try again.")


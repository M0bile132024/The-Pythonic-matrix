# THE ULTIMATE TRACK(er)
#Date:31/03/2025
#Version:V 1.35
#Author:M0bile132022
''' Description:This is an ULTIMATE tracker that can track ULTIMATE things
such as:
1. Sparxs bookwork'''
import time
import json
import os
import pyperclip
import FTP
#Function to copy text to keyboard

def copy_to_keyboard(text,true_or_false):
    if true_or_false == True:    
        pyperclip.copy(text)
        print("Text copied sucessfully")
copy_to_keyboard_true = True
version = 1.35
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
2.FTP(Fitness Tracker Program)
3.Loot Tracker(coming 1.4.25)
4.Cat Tracker(coming 1.4.25)
    More will be added soon""")
    category = int(input("Please chose an operation:"))
    if category == 1:
        while True:
        
            print("Welcome to the Sparxs Bookwork Tracker!!!")
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
                    temp_dict = ""
                    for k in range(len(bookwork_list)):
                        print(f"Bookwork {bookwork_ID[k]}:{bookwork_list[k]}")
                        temp_dict += f"\nBookwork {bookwork_ID[k]}:{bookwork_list[k]}"
                    copy_to_keyboard(temp_dict,copy_to_keyboard_true)
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
                if name == "":
                    print("Invalid name.Please try again")
                    continue
                directory = input("Please input the directory you wish to save the file to(if non-existent, new directory will be made)")
                #validate the name
                if not os.path.exists(directory):
                    try:
                        os.makedirs(directory)
                    except:
                        print("Invalid directory name.Please try again")
                        continue
                file_path = os.path.join(directory, name)
               
                with open(f"{file_path}.json","w") as f:
                    json.dump({"bookwork_list": bookwork_list, "bookwork_ID": bookwork_ID}, f)
            elif operation == 8:
                print("You have chosen to save the current bookwork to the last save file")
              

                #need to delete old stuff in file/delete old file
                with open(f"{file_path}.json","w") as f:
                    if file_path in os.listdir():
                        os.remove(f"{file_path}.json")
                        json.dump({"bookwork_list": bookwork_list, "bookwork_ID": bookwork_ID,"Question":question,"Letter":i,"Iterations":j}, f)
                    else:
                        print("Save file not found")
            elif operation == 9:
                print("You have chosen to load new bookwork")
                file_path = input("Please input the file path of the file you wish to load the bookwork from:")
                #check if the file exists
                if file_path in os.listdir():
                    with open(f"{file_path}.json","r") as f:
                        data = json.load(open(f"{file_path}.json", "r"))
                        bookwork_list = data["bookwork_list"]
                        bookwork_ID = data["bookwork_ID"]
                        question = data["Question"]
                        i = data["Letter"]
                        j = data["Iterations"]
                    print("Bookwork loaded")
                else:
                    print("File not found")
    elif category == 2:
        FTP.FTP()
    else:
        print("Invalid input.Please try again.")


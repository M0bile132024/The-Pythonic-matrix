# Date:15/03/2025
# Version:1.0
# FTP improvements
import time
import sys
#Fitness tracker program
days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#OG:step_list = []
#Correction: 0's added to allow for indexing
step_list = [0,0,0,0,0,0,0]
while True:
    #Menu sys good
    print("Welcome to the Fitness Tracker Program(FTP) 1.0!!!")
    #Formatting error OG:.....1.Add step counts.....
    #minor fixed
    print("""Please chose an operation you wish to do:
    1. Add step counts for each day of the week
    2. View recorded step counts for this week
    3. Delete a step count
    4. Exit the program(Note:Will not save if exited)""")
    operation = int(input("Please chose an operation:"))
    #Extension:Operation 1:This needs a rework
    #Extension:
    if operation == 1:
        #Correctely asked for step counts each day of week
        print("You have chosen to add step counts for each day of the week")
        step_count = 0
        
        if 0 in step_list:  
            for i in range(7):
                if step_list[i] != 0:
                    print(f"You have already added a step count for {days_of_week[i]}")
                    continue
                else:
                #Validation of step values excellent BUT it allows negiative values
                #OG:while step_count == 0 or step_count > 100000:
                #Correction:
                    while step_count <= 0 or step_count >= 100000:
                        step_count = int(input(f"Please input how steps were taken on {days_of_week[i]} (Max:100,000):"))
                        
                        #Extension:Add invalid input message
                        #Extension:
                        if step_count <= 0 or step_count >= 100000:
                            print("Invalid input.Please try again.")
                    step_list[i] = step_count
                    step_count = 0
            print("Values sucessfully added")
        else:
            print("You have already added step counts for each day of the week")
        
    elif operation == 2:
        print("You have chosen to view recorded step counts:")
        if len(step_list) == 0:
            print("Your step list for this week is currently empty.Please try adding some new step values")
        else:
            #Viewing sys/delete sys nice
            for k in range(7):
                print(f"On {days_of_week[k]} you took {step_list[k]} steps")
                #Extension:Add total step count for entire week
                #Extension:
            print(f"Total steps taken this week: {sum(step_list)}")
    elif operation == 3:
        print("You have chosen to delete a step count")
        if len(step_list) == 0:
            print("Your step list for this week is currently empty.Please try adding some new step values")
        else:
            #Huge mistake here,I forgot about the indexing system(ie. 0-6)
            #OG:
            #day = 0
            #while day == 0 or day > 7:
            #    day = int(input("Please chose a day of the week(1-7) to remove a step count from:"))
            #step_list.pop(day)
            #Correction:
            day = 0
            while day <= 0 or day > 7:
                day = int(input("Please chose a day of the week(1-7) to remove a step count from:"))
                if day <= 0 or day > 7:
                    print("Invalid input.Please try again.")
                else:
                    break
            step_list[day-1] = 0
            print("Step count sucessfully removed")
    #Esle=any invalid inputs kills program
    #OG:else:
    #Correction:
    elif operation == 4:
        #Exit functional,but message can be improv
        #OG:print("Ok bye,bye")
        #Correction:
        print("Thank you for using FTP.Goodbye!")
        #Sys.exit=Overkill for such small program
        #OG:sys.exit()
        #Correction:
        break
    #EX:Should aslo include invalid input sys as so to reloop
    #Extension:
    else:
        print("Invalid operation.Please try again")
        continue
#Overall,good program,just needs a few tweaks
#Rating:8/10
#Main improv:1. Add invalid input message
#              2. Add total step count for entire week
#              3. Else=any invalid inputs kills program
#              4. Validation of step values excellent BUT it allows negiative values
#              5. Huge mistake here,I forgot about the indexing system(ie. 0-6)










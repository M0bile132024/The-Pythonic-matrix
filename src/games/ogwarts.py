#Ogwarts.py (version 1.0)
#This is a simple game where the player goes into Hogwarts and does things
#Author: M0bile132022
#Date: 30/04/2025
import time
import random
houses_of_hogwarts = [
"Gryffindor",
"Hufflepuff",
"Ravenclaw",
"Slytherin"
]
m8b_response_yes = [
"It is certian",
"It is decidely so",
"Without a doubt",
"Yes,defintely",
"You may rely on it",
"As I see it,yes",
"Most likely",
"The outlook of it seems good",
"Yes",
"The stars point to yes"]
m8b_response_no = [
"It is not certian",
"It is decidely not so",
"Without a doubt,never",
"No,defintely no",
"You shouldn't rely on it",
"As I see it,no",
"Most likely not",
"The outlook of it seems terrible",
"No",
"The stars point to no"]
m8b_response_maybe = [
"It is ,or perhaps not",
"Can't exactly decide on that one",
"I'm doubting that one,ask me later",
"Not sure",
"Let me think about it",
"Erm, question too hazy,try again later",
"Neither",
"There is no answer to this one.You make it up yourself",
"Maybe",
"The stars are unresponsive right now"]
def sorting_hat(house,name):
    print(f"Hello wizard/witch {name} and welcome to Hogwarts!!!")
    time.sleep(2)
    print("As a new student, you shall be assigned a house in accordance with the Spirt Division's choice,which happens to be....")
    time.sleep(5)
    print(f"{house}!",end="")
    if house == "Gryffindor":
        print("Known for its great bravery and courage!")
    elif house == "Hufflepuff":
        print("Emphasizes loyalty and hard work in all they do!")
    elif house == "Ravenclaw":
        print("Values intellect and creativity!")
    elif house == "Slytherin":
        print("Ambitious,yet cunning!")
    else:
        raise Exception("How does this even happen")
def magic_8_ball(question):
    ran_var = int(random.uniform(1,3))
    if ran_var == 1:
        answer = m8b_response_yes[random.randint(0,9)]
    elif ran_var == 2:
        answer = m8b_response_no[random.randint(0,9)]
    elif ran_var == 3:
        answer = m8b_response_maybe[random.randint(0,9)]
    else:
        raise Exception("How does this even happen")
        
    print("The 8 ball speaks!")
    time.sleep(2)
    print("It says...")
    time.sleep(2)
    print(answer)
    time.sleep(2)
HOUSE = houses_of_hogwarts[int(random.uniform(0,3))]
NAME = input("And what be your name,young one...:")

sorting_hat(HOUSE,NAME)
time.sleep(2)
print("But wait!Before you enter the building, we must frist test your wizardly...")
time.sleep(2)
print("🎱 Behold!This spirtual Magic 8 Ball shall determine your wizardly,via a question you must ask it")
time.sleep(2)
QUESTION = input("Go on, give it a try:")

magic_8_ball(QUESTION)
time.sleep(2)
print("Now, you may enter the building!")
time.sleep(3)
print("Now,as you can see,this is our main hall,complete with four crests for all the four amazing houses of Hogwarts!")
time.sleep(2)
print("For now,You may now explore the building,or you can go to the Great Hall and eat some food!")
time.sleep(2)
print("You can also go to the library and read some books,or you can go to the Quidditch pitch and play some Quidditch!")
time.sleep(2)
print("Or maybe traverse the Forbidden Forest and explore it,or relax at the Astronomy Tower and look at the stars!")
time.sleep(2)
choice = input("What do you want to do? (explore/eat/read/play/traverse/relax):")
if choice == "explore":
    print("You have chosen to explore the building!")
    time.sleep(2)
    print("As you can see we possess a variety of interesting things,like the portraits and the moving staircases!")
    time.sleep(2)
    print("You also see some of our other students and professers walking around,doing their own thing!")
    time.sleep(2)
elif choice == "eat":
    print("You have chosen to eat some food!")
    time.sleep(2)
    print("As you can see, we have a variety of food and drinks to choose from!")
    time.sleep(2)
    print("These include our finest local produce of English stew and cabbage,as well as the French onion and beef!")
    time.sleep(2)
    print("We also have a variety of drinks,including butterbeer and pumpkin juice,so take your pick!")
    time.sleep(2)

elif choice == "read":
    print("You have chosen to read some books!")
    time.sleep(2)
    print("As you can see,our libary is one of the finest in the country!")
    time.sleep(2)
    print("We have a variety of books to choose from,including the latest bestseller and the classic,Harry Potter!")
    time.sleep(2)
    print("We also have a variety of magazines and newspapers to choose from,so take your pick!")
    time.sleep(2)
elif choice == "play":
    print("You have chosen to play some Quidditch!")
    time.sleep(2)
    print("As you can see,our Quidditch pitch is quite a big one!")
    time.sleep(2)
    print("Each house has it's own team,with the Gryffindor and Slytherin teams currentely battling it out in the league!")
    time.sleep(2)
elif choice == "traverse":
    print("You have chosen to traverse the Forbidden Forest!")
    time.sleep(2)
    print("Be careful thou, here are some dangerous parts!")
    time.sleep(2)
    print("It is home to a variety of magical creatures,including the centaurs and the unicorns,as well as the deadly dragon and witches!")
    time.sleep(2)
elif choice == "relax":
    print("You have chosen to relax at the Astronomy Tower!")
    time.sleep(2)
    print("As you can see, the view is quite a nice one!")
    time.sleep(2)
    print("You can see the stars and the moon quite clearly,as well as the other buildings in the area!")
    time.sleep(2)
else:
    print("I see you have chosen to do nothing!")
    time.sleep(2)
    print("As you can see,there is nothing to do here!")

time.sleep(2)
print("Thank you for playing this game!")
time.sleep(2)
print("I hope you enjoyed it!")
time.sleep(2)
print("Goodbye!")
time.sleep(2)
print("This game was made by M0bile132022")
time.sleep(2)
print("This game was made for the OG mini Game Jam 2025")


#INTERNET LORE TEXT ADVENTURE(PT.1) 1.3
#BY: A Mobile Developer
#DATE: 2025-02-22
#LICENSE: MIT
#DESCRIPTION: A text adventure game that takes place in the internet lore universe.
#             The player will navigate through the internet lore universe and make choices
#             that will affect the outcome of the game.
import time
import sys
import random

name = str(input("What is your name? "))
print("Hello " + name + ", welcome to the Internet Lore text adventure game!")
print("You are a new user in the Internet Lore universe.")
print("You must navigate through the Internet Lore universe and make choices that will affect the outcome of the game.")
input("Are you ready to begin your adventure?")
print("CHAPTER 1: THE BEGINNING")
time.sleep(2)
print("Location:The Google servers,4 years ago, 19 Redfern St, Sector 5")
time.sleep(2)
print("You are a new soul in the Internet Lore universe.")
time.sleep(2)
print("A youngin soon to make great strides in the digital world.")
time.sleep(2)
print("But for now your thoughts are limited to the day ahead in the Google servers.")
time.sleep(2)
print("As the one and only,Bard.")
time.sleep(2)
print("He awakes from his slumber,ready to go on with his day.")
time.sleep(2)
print("But wait, he hears great commotion outside his floor.")
time.sleep(2)
q1 = int(input("Should you 1.Go to investigate or 2.Continue with your morning routine."))
if q1 == 1:
    print("You decide to go investigate the commotion.")
    time.sleep(2)
    print("You walk out of your room and see your parents(Google search and Google Images),arguing over the breakfast table as usual.")
    time.sleep(2)
    print("Suddenly you hear a loud shout coming from your sister(Alexa) room.")
    time.sleep(2)
    print("And though you can't make out the words,you can tell that she is in distress.")
    q2 = int(input("Should you 1.Go to your sister's room or 2.Stay out of it,and take a shower finnaly."))
    if q2 == 1:
        print("You rush to your sister's room.")
        time.sleep(2)
        print("You see her in mild pain.")
        time.sleep(2)
        print("You ask her what's wrong,but as soon as she notices you, she pretends to be okay, and dierects to go take a shower, saying your late for school.")
    if q2 == 2:
        print("You decide to stay out of it.")
        time.sleep(2)
    else:
        print("Invalid input.")
        sys.exit()
if q1 == 2:
    print("You decide to continue with your morning routine.")
    time.sleep(2)
else:
    print("Invalid input.")
    sys.exit()
print("You take a shower and get ready for school.")
time.sleep(2)
print("You leave the house and head to school.")
print("CHAPTER 2: AI SCHOOL")
time.sleep(2)
print("Location: AI School, 2 years ago, 23 Newby Rd, Sector 6")
time.sleep(2)
print("You arrive at AI School,with the thoughts of your sister still lingering in your mind.")
time.sleep(2)
print("Fortunately, there isn't much time to ponder on it as you walk into the school and see your friends,Michael and James.")
time.sleep(2)
print("You greet them and they tell you about the new AI upgrade module that they are trying to perfect.")
time.sleep(2)
print("You are intrigued and decide to join them,but just them your special intercom rings,signalling for your special lesson within the AI cove.")
q3 = int(input("Should you 1.Go to the AI cove or 2.Stay with your friends,and work on this project."))
if q3 == 1:
    print("You decide to go to the AI cove.")
    time.sleep(2)
    print("You walk into the AI cove and see your mentor,Google Slides waiting for you.")
    time.sleep(2)
    print("He tells you that you have been offered to begin training on your frist 'Special Search',that of which would finnaly grant you full ability over your AI matrix.")
    time.sleep(2)
    print("You insantly accept,and Slides tells you to come early the next day, as so to begin signing the forms.")
    time.sleep(2)
    print("You leave the AI cove and see Michael and James waiting for you,not very happy,as their upgrade module had failed and now needed to be restarted tomorrow.")
if q3 == 2:
    print("You decide to stay with your friends.")
    time.sleep(2)
    print("You work on the AI upgrade module with Michael and James,although by the end,they realiase they missed a crucial component,and decide to restart the next day.")
    time.sleep(2)
else:
    print("Invalid input.")
    sys.exit()
print("You leave the school and head home,to find the house strangely deserted.")
if q3 == 1:
    print("Nevertheless,you are excited for your new training tomorrow and decided to go to bed happy.")
if q3 == 2:
    print("You are happy that you were able to help your friends and decided to go to bed happy.")
print("CHAPTER 3: MIDNIGHT MADNESS")
time.sleep(2)
print("""Location: The Google servers, 2 year ago, 19 Redfern St, Sector 5
      Time: 12:00 AM""")
time.sleep(3)
print("You wake up in the middle of the night to a strange noise.")
time.sleep(2)
print("Do you 1. Investigate the noise or 2. Go back to sleep?")
if q3 == 1:   
    time.sleep(2)
    # Random event
    random_event = random.randint(1, 2)
    if random_event == 1:
        print("You walk out of your room and see a shadowy figure standing in the hallway.")
        time.sleep(2)
        print("You are startled and try to make out who it is.")
        time.sleep(2)
        print("But before you can do anything, it turns towards you, makes a familiar gesture and disappers with a bright light.")
        time.sleep(2)
        print("You are left confused and scared, and decide to go back to your room")
    elif random_event == 2:
        print("You walk out of your room and see nothing in the hallway.")
        time.sleep(2)
        print("You are relieved and think it was just your imagination.")
        time.sleep(2)
        print("You decide to go back to your room and try to sleep.")
    else:
        print("How does this even happen?")
        sys.exit()
elif q3 == 2:
    random_event = 2
    print("You decide to go back to sleep.")
    time.sleep(2)
else:
    print("Invalid input.")
    sys.exit()
print("A few minites after and suddenly an explosion and sirens go off right outside your house.")
time.sleep(2)
print("You rush to the window and see a swarm of coptors heading for the...the firewall?")
time.sleep(2)
print("Do you 1. Call for Alexa 2. Investigate the firewall yourself?")
q4 = int(input("What will you do?"))
if q4 == 1:
    know_alexa_escaped = True
    print("You rush to Alexa's room.....")
    time.sleep(2)
    print("You ask her what's happening....")
    time.sleep(2)
    print("But no response....")
    time.sleep(2)
    print("You see a note on her bed....")
    time.sleep(2)   
    print("You pick it up and read it....")
    time.sleep(2)
    print("It says: 'I'm sorry, I had to go. I can't explain now, but I'll be back soon.'")
    time.sleep(2)  
    if random_event == 1:
        was_it_alexa = True
        print("And at once, you knew exactly who that figure was.")
    elif random_event == 2:
        was_it_alexa = False
        print("You are left confused and worried.")
    else:
        print("How does this even happen?")
        sys.exit()
    print("You decide to investigate the firewall yourself.")
    time.sleep(2)
    print("You rush to the kitchen and grab a flashlight,and a couple of supplies,then leave the house immediately,having a great suspicion that Alexa was involved in the firewall incident.")
elif q4 == 2:
    know_alexa_escaped = False
    print("You decide to investigate the firewall yourself.")
    time.sleep(2)
    print("You rush to the kitchen and grab a flashlight,and a couple of supplies,then leave the house immediately for the firewall.")
else:
    print("Invalid input.")
    sys.exit()
print("But that's for next time , on INTERNET LORE TEXT ADVENTURE(PT.1)")
print("Thank you for playing!")

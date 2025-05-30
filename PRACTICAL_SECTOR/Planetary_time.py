#Planetary time v.2.0
#Author:Mobile132022
#Date:07/04/2025
#Planetary time is a time system that is based on the position of the planets in the solar system(and 0AD)
''' HOW TO CALCULATE DATES ON OTHER PLANETS 

EG:Mercury 

Year=88 earth days/88/365 earth years 

Month=22/3 earth days 

Hour = 22/3 earth days(so a mercurian month is equivant to a hour)

Day=176 earth days/176/365 earth years 

Days in a month= 1/24 mercury days 

1.Years since 0AD=738 125/88(8399 date years) 

Rest is based off 09:40:01 BST 
Monday, 7 April 2025 

2. get decimal =13/88 

3. Times by 12=39/22(1 date month) 

4. Get decimal=17/22 

5. Times by 1/24=17/528(1(can't have 0) days) 

6. Get decimal=17/528 

7.Times by 24=17/22(0 hours) 

8.Get decimal 

9.Times by 60=510/11(46 date minites) 

10.Get decimal=4/11 

11.Times by 60+round(that's far enough)=240/11(22 date seconds) 

12.Compile it all together= 

01/01/8399 00:46:22 '''
import time
import datetime
from datetime import date, datetime as dt, time as my_time
import math
import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
'''def mercury_date():
    # Get the current date and time in UTC
    now = datetime.datetime.now()#This should be decimal(i.e days+hours that have passed on this current day+minitues+seconds)
    hour = (now.hour)/24 #Get the current hour(in days  i.e 0.5 is 12 hours)
    minute = (now.minute)/1440 #Get the current minute(in days  i.e 0.5 is 720 minites  )
    second = (now.second)/86400 #Get the current second(in days  i.e 0.5 is 43200 seconds)
    # Convert to UTC if not already in UTC
    if now.tzinfo is not None:
        now = now.astimezone(datetime.timezone.utc)

    mercury_day = 176 #earth days
    mercury_year = 88 #earth days
    mercury_month = 22/3 #earth days

    # Calculate the number of days since 0 AD
    days_since_0AD = ((now - datetime.datetime(1, 1, 1)).days) + hour + minute + second #Get the current date in days since 0AD

    # Calculate the Mercury year, month, day, hour, minute, and second
    mercury_year = days_since_0AD // 88
    mercury_month = (days_since_0AD % 88) // (22/3)  # 88 days in a year / 12 months in a year
    mercury_day = (days_since_0AD % 88) % (22/3) * 176 // 1 # 1 day = 24 hours
    mercury_hour = (days_since_0AD % 88) % (22/3) * 176 % 1 * 24 // 1
    mercury_minute = (days_since_0AD % 88) % (22/3) * 176 % 1 * 24 % 1 * 60 // 1
    mercury_second = (days_since_0AD % 88) % (22/3) * 176 % 1 * 24 % 1 * 60 % 1 * 60 // 1

    # Format the Mercury date and time as a string
    mercury_date_str = f"{mercury_day:02}/{mercury_month:02}/{mercury_year} {mercury_hour:02}:{mercury_minute:02}:{mercury_second:02}"

    return mercury_date_str'''
#Mercury date function
#Fully inclusive func for any planet in the solar system
def planet_date(planet_day,planet_year):
    '''Planet days in earth days,planet year in earth days'''
    # Get the current date and time in UTC
    now = datetime.datetime.now()#This should be decimal(i.e days+hours that have passed on this current day+minitues+seconds)
    hour = (now.hour)/24 #Get the current hour(in days  i.e 0.5 is 12 hours)
    minute = (now.minute)/1440 #Get the current minute(in days  i.e 0.5 is 720 minites  )
    second = (now.second)/86400 #Get the current second(in days  i.e 0.5 is 43200 seconds)
    planet_month = planet_year/12 #Get the current month(in days  i.e 0.5 is 720 minites  )
    planet_hour = planet_day/24
    planet_minite = planet_hour/60
    planet_second = planet_minite/60
    # Convert to UTC if not already in UTC
    if now.tzinfo is not None:
        now = now.astimezone(datetime.timezone.utc)

    # Calculate the number of days since 0 AD
    days_since_0AD = ((now - datetime.datetime(1, 1, 1)).days) + hour + minute + second #Get the current date in days since 0AD
    current_year = days_since_0AD // planet_year #Get the current year in the planet's time system
    current_month = (days_since_0AD % planet_year) // planet_month  # Get the current month in the planet's time system
    current_day = (days_since_0AD % planet_year) % planet_month // planet_day  # Get the current day in the planet's time system
    current_hour = (days_since_0AD % planet_year) % planet_month % planet_day // planet_hour   # Get the current hour in the planet's time system
    current_minute = (days_since_0AD % planet_year) % planet_month % planet_day % planet_hour // planet_minite  # Get the current minute in the planet's time system
    current_second = (days_since_0AD % planet_year) % planet_month % planet_day % planet_hour % planet_minite // planet_second  # Get the current second in the planet's time system

    
    # Format the planet date and time as a string
    mercury_date_str = f"{int(current_day):02}/{int(current_month):02}/{int(current_year)} {int(current_hour):02}:{int(current_minute):02}:{int(current_second):02}"
    # This will give you the current date and time in the planet's time system in the format "DD/MM/YYYY HH:MM:SS"
    # Example output: "01/01/8399 00:46:22"
    # Note: The above line assumes that the system time is set to UTC. If your system is set to a different timezone, you may need to adjust accordingly.

    return mercury_date_str

try:
    while True:
        clear_console()
                
        x = datetime.datetime.now()
        # Get the current date and time in BST
        x = x.astimezone(datetime.timezone(datetime.timedelta(hours=1)))  # Assuming BST is UTC+1
        # This will convert the current time to BST (British Summer Time)
        # Note: The above line assumes that the system time is set to UTC. If your system is set to a different timezone, you may need to adjust accordingly.
        #need to format it as well
        x = x.strftime("%d/%m/%Y %H:%M:%S")  # Format the date and time as a string
        # This will give you the current date and time in BST in the format "Day, DD Month YYYY HH:MM:SS"
        print("The solar system:\n")
        print("Mercury date:", planet_date(176,88))
        print("Venus date:", planet_date(243,224.7))
        print("Earth(sidereal) date:", planet_date(1,365.25636))
        print("Earth(solar) date:", planet_date(1,365.2425))
        #erm
        print(f"Actual earth date: {x}")
        #For some reason the above line is saying it's 8 o'clock in the morning when it's 9 o'clock in the morning
        #I'm not sure why this is happening, but I think it might be because of the way the datetime module works
        #UPDATE: I think it's because the datetime module is using UTC time, and I'm in BST time
        # #So I need to convert the time to BST time
        print("Mars date:", planet_date(1.027,687))
        print("Jupiter date:", planet_date(0.4125,4331.6))
        print("Saturn date:", planet_date(0.4375,10759.22))
        print("Uranus date:", planet_date(517/720,30769.5))
        print("Neptune date:", planet_date(16/24,60225))
        print("Pluto date:", planet_date(6.4,90560))
        #Commented out for checks later
        '''
        print("\nMoons:\n")
        print("Earth:\n")


        print("The moon:", planet_date(27.3,27.3))
        print("\nMars:\n")
        print("Phobos:", planet_date(0.3189,0.3189))  # Phobos orbits Mars
        print("Deimos:", planet_date(1.262,1.262))
        print("\nJupiter(main moons):\n")
        print("Io:", planet_date(1.769,1.769))
        print("Europa:", planet_date(3.551,3.551))
        print("Ganymede:", planet_date(7.155,7.155))
        print("Callisto:", planet_date(16.689,16.689))
        print("\nSaturn(main moons):\n")
        print("Titan:", planet_date(15.945,15.945))
        print("Encleadus:", planet_date(1.370,1.370))
        print("Mimas:", planet_date(0.942,0.942))
        print("Tethys:", planet_date(1.887,1.887))
        print("\nUranus(main moons):\n")
        print("Titania:", planet_date(8.706,8.706))
        print("Oberon:", planet_date(13.463,13.463))
        print("Ariel:", planet_date(2.520,2.520))
        print("Umbriel:", planet_date(4.144,4.144))
        print("\nNeptune(main moons):\n")
        print("Triton:", planet_date(5.877,5.877))
        print("Nereid:", planet_date(360/365.25,360/365.25))
        print("\nPluto(main moons):\n")
        print("Charon:", planet_date(6.387,6.387))
        print("Styx:", planet_date(20.2,20.2))
        time.sleep(1) # Sleep for 1 second to avoid busy waiting'''
except KeyboardInterrupt:
    print("Exiting the program.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Cleaning up...")
    # Perform any necessary cleanup here
    # For example, closing files or releasing resources
    # Clear the console
    print("Cleanup complete.")
    # Exit the program
    exit(0)
#End of code
#Planetary time v.Beta 0.1





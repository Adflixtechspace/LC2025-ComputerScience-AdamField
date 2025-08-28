import time
epoch = time.time()
seasonNumber = 0
flag = "down"
zerohours = ""
zerominutes = ""
while flag == "down":
    season = input("Is it summer time? Y/N ")
    if season == "Y":
        seasonNumber = 3600
        flag = "up"
    elif season == "N":
        seasonNumber = 0
        flag = "up"
    else:
        print("Invalid response")
        flag = "down"  
seconds_today = (epoch%86400)+seasonNumber
hours_today = (seconds_today//3600)
seconds_tohour = (seconds_today%3600)
clock_hours = str(int(hours_today))
if len(clock_hours) < 2:
    zerohours = "0"
minutes_today = (seconds_tohour//60)
clock_minutes = str(int(minutes_today))
if len(clock_minutes) < 2:
    zerominutes = "0"
CurrentTime = print(zerohours+clock_hours+":"+zerominutes+clock_minutes)
    
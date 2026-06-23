# Main File responsible for launching the whole thing.
import random
import berries_load
from pick import pick

# So I'm gonna have this file offer 3 options to be executed:
# 1st will be the default experience from the OG version of the program that just gets you the berries
# 2nd will get you a random 50 items sorted into the excel sheet (50 seems more practical if I'm gonna be rude and batch call)
# 3rd will use a downloaded local version of the item API and sort 500 items or all 2000 if you want (It'll take awhile) that's gonna be local I'm rude, but not like...Batch call a thousand calls Evil

# This is something fun idk when I'm gonna use it
def profSays():
    professors = ['Oak','Elm','Birch','Rowan','Juniper','Sycamore','Kukui','Magnolia','Sonia','Laventon','Sada','Turo']
    print(f'Prof.{random.sample(professors,1)[0]} says: There\'s a time and place for that!')
#Takes advantage of a simple module Wong made found in this SO thread: https://stackoverflow.com/a/70254575
# Git here: 
title="What items would you like to load into excel?: "
options= ['1. Berries Only','2. Random 50 items','3. Everything','I do what I want']
option, index=pick(options,title,indicator='=>',default_index=0)
match index:
    # I want this to run with the original functionality I wanted when I was only partially insane
    case 0:
        print('Berries')
        berries_load.berryFileCheckAndStart()
    case 1:
        print("Random 50")
        list = random.sample(range(1,2176),50)
        print(list)
    case 2:
        print("Everything")
    case 3:
        profSays()
    # It won't happen but hey man I'm bored
    case _:
        print('OOB MISSINGNO ACTIVE')
#Number Game

import random
import time
from threading import Timer


print(' \t \t Welcome to the number game !!!')
#All the numeral choices available to users
all_choices = [1,2,3,4,5,6,7,8,9]
while True:
    #Random no. of stars displayed to users
    no_of_stars=random.choice(all_choices)
    print('*'*no_of_stars)
    timeout = 10 #10 seconds timeout for entering choice
    t = Timer(timeout, print, ['Sorry, Time is up '])
    t.start()
    prompt = "Enter the number of stars displayed \n HURRY !!! You have %d seconds to choose the correct answer...\n" % timeout
    answer = int(input(prompt)) #user's input of the number of stars
    t.cancel()
    if answer==no_of_stars: 
        all_choices.remove(answer)
        print("Congratulations !!! \n You win !!!")
    else:
        print('Uh-Oh! Wrong choice. \n You lost !')


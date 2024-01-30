#import required libraries
from random import choice
from time import sleep
from sense_hat import SenseHat

#intialize list of replies
replies = ["Signs point to yes",
        "Without a doubt",
        "Don't count on it",
        "You may rely on it",
        "Looking good",
        "Cannot predict now",
        "It is decidedly so",
        "Outlook not so good",
        "Better not tell you now",
        "As I see it, yes"

    ]

#intialize SenseHat object
sense = SenseHat()

#test
sense.show_message("Ask a question", scroll_speed=0.06)
sleep(3)
#sense.show_message(choice(replies), scroll_speed=0.07)

#enable reply upon shaking RP4
while True:
    #get xyz coordinates from accelerometer
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x) #abs converts number values to positive. We don't care where pi is, only that it is being shaken
    y = abs(y)
    z = abs(z)

    #condition in code to check for movement and reply when detected
    #change x, y ,z thresholds if you want lighter or stronger shake
    if x > 2 or y > 2 or z > 2:
        sense.show_message(choice(replies), scroll_speed=0.06)

    else:
        sense.clear()
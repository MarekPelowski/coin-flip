from random import randint

flip = 127
status = ""

def chance():
    global status
    x = randint(1, 2)
    if x == 1:
        status = "tails"
    elif x == 2:
        status = "heads"


def calculation():
    for x in range(flip):
        chance()
        print(status)


calculation()
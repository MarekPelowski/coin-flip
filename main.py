from random import randint

flip = int(input("Enter the amount of coin flips: "))
status = ""
tails = 0
heads = 0

def status_check():
    global tails, heads
    if status == "tails":
        tails = tails + 1
    elif status == "heads":
        heads = heads + 1


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
        print(status, "\n")
        status_check()


calculation()
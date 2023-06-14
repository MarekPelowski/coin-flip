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


for x in range(flip):
    chance()
    status_check()
    print(status, "\n")
tails_percent = (tails * 100) / flip
heads_percent = (heads * 100) / flip

print("tails: ", tails_percent)
print("heads: ", heads_percent)
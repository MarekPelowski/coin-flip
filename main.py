from random import randint

flip = int(input("Enter the amount of coin flips: "))
status = ""
tails = 0
heads = 0
streak_tails = 0
streak_heads = 0
streak_best_tails = []
streak_best_heads = []




def status_check():
    global tails, heads, streak_heads, streak_tails, streak_best_tails, streak_best_heads
    if status == "tails":
        tails = tails + 1
        streak_tails = streak_tails + 1
        streak_best_heads.insert(0, streak_heads)
        streak_heads = 0

    elif status == "heads":
        heads = heads + 1
        streak_heads = streak_tails + 1
        streak_best_tails.insert(0, streak_heads)
        streak_tails = 0



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
    print(status)
tails_percent = (tails * 100) / flip
heads_percent = (heads * 100) / flip


print("tails: ", round(tails_percent, 4), "%")
print("heads: ", round(heads_percent, 4), "%")
print("\ntails streak: ", max(streak_best_tails))
print("heads streak: ", max(streak_best_heads))
import random


def car_registration():
    boks = "abcdefghijklmnopqrstuvwxyz"
    nummer= ""
    for i in [0,1]:
        nummer += random.choice(boks).upper()
    for i in range(5):
        siffer = random.randint(0,9)
        while i== 0 and siffer == 0:
            siffer = random.randint(0,9)
        nummer += str(siffer)
    return nummer    
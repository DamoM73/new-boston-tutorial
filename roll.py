import random

for i in range(0,9500):
    success = 0
    for die in range(1,6):
        roll = random.randrange(1,10)
        if roll == 10:
            success += 2
        elif roll > 6:
            success += 1
    if success > 50:
        print(success)


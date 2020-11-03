import random
import time

def winingGame():
    target=random.randint(2,4)
    print(f"Your target to press after {target} seconds")
    input('Press Enter to start')
    start=time.perf_counter()
    input(f'Press after {target} seconds')
    end=time.perf_counter()-start
    if end == target :
        print('Amazing the absolute timing')
    elif end < target :
        print(f'Ooops You pressed early by {target-end:.3f}')
    elif end > target :
        print(f'Ooops You pressed late by {end-target:.3f}')


winingGame()
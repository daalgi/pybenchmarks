from random import random
import numpy as np

from base import Test


def python():
    return random()

def numpy_random():
    return np.random.random()


repetitions_list = [int(1e1), int(1e2), int(1e3), int(1e4), int(1e6), int(2e6)]
for repetitions in repetitions_list:
    print(f"\nREPETITIONS = {repetitions}")
    Test(python, repetitions=repetitions, verbose=False)
    Test(numpy_random, repetitions=repetitions, verbose=False)
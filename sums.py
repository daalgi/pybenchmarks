import timeit, time
import numpy as np
from numba import jit, prange

from base import Test, random_vector


def python_loop_in_range(vector):
    s = 0
    for i in range(0, len(vector)):
        s += vector[i]
    return s

def python_loop_in_list(vector):
    s = 0
    for v in vector:
        s += v
    return s

def python_sum(vector):
    return sum(vector)

def numpy_sum(vector):
    return np.sum(vector)

@jit(nopython=True)
def numba_in_range(vector):
    s = 0
    for i in range(0, len(vector)):
        s += vector[i]
    return s

@jit(nopython=True, parallel=True)
def numba_parallel(vector):
    s = 0
    for i in prange(length):
        s += vector[i]
    return s


lengths = [int(1e1), int(1e2), int(1e3), int(2e3), int(1e4), int(1e5)]
repetitions = 10000
for length in lengths:
    print(f"\nVECTOR LENGTH = {length:.0E} -- REPETITIONS = {repetitions}")
    vector = random_vector(length)

    if length < 2e3:
        Test(python_loop_in_range, vector, repetitions=repetitions)
        Test(python_loop_in_list, vector, repetitions=repetitions)
        Test(python_sum, vector, repetitions=repetitions)
        
    Test(numpy_sum, vector, repetitions=repetitions)
    
    Test(numba_in_range, vector, repetitions=repetitions)
    Test(numba_parallel, vector, repetitions=repetitions)
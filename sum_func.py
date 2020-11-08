import timeit, time, random
import numpy as np
from numba import jit, prange

from base import Test, random_vector


@jit
def func(x):
    return x ** 1.5 - 0.5 * x + 8 / (2 * x ** 2 + 1)

def python_loop_in_range(vector):
    s = 0
    for i in range(len(vector)):
        s += vector[i] ** 1.5 - 0.5 * vector[i] + 8 / (2 * vector[i] ** 2 + 1)
    return s

def python_loop_in_range_f(vector):
    s = 0
    for i in range(len(vector)):
        s += func(vector[i])
    return s

def python_loop_in_list(vector):
    s = 0
    for x in vector:
        s += x ** 1.5 - 0.5 * x + 8 / (2 * x ** 2 + 1)
    return s

def python_loop_in_list_f(vector):
    s = 0
    for v in vector:
        s += func(v)
    return s

def python_list_comprehension(vector):
    return sum([x ** 1.5 - 0.5 * x + 8 / (2 * x ** 2 + 1) for x in vector])

def python_list_comprehension_f(vector):
    return sum([func(x) for x in vector])

def numpy_(vector):
    return np.sum([x ** 1.5 - 0.5 * x + 8 / (2 * x ** 2 + 1) for x in vector])

def numpy_f(vector):
    #return np.sum([func(x) for x in vector])
    return func(vector)

@jit(nopython=True)
def numba_in_range(vector):
    s = 0
    for i in range(len(vector)):
        s += vector[i] ** 1.5 - 0.5 * vector[i] + 8 / (2 * vector[i] ** 2 + 1)
    return s

@jit(nopython=True)
def numba_in_range_f(vector):
    s = 0
    for i in range(len(vector)):
        s += func(vector[i])
    return s

@jit(nopython=True, parallel=True)
def numba_parallel(vector):
    s = 0
    for i in prange(len(vector)):
        s += vector[i] ** 1.5 - 0.5 * vector[i] + 8 / (2 * vector[i] ** 2 + 1)
    return s

@jit(nopython=True, parallel=True)
def numba_parallel_f(vector):
    s = 0
    for i in prange(len(vector)):
        s += func(vector[i])
    return s


lengths = [int(1e1), int(1e2), int(1e3), int(2e3), int(1e4), int(1e5)]
repetitions = 10000
for length in lengths:
    print(f"\nVECTOR LENGTH = {length:.0E} -- REPETITIONS = {repetitions}")
    vector = random_vector(length)

    if length < 2e3:
        Test(python_loop_in_range, vector, repetitions=repetitions)
        Test(python_loop_in_range_f, vector, repetitions=repetitions)
    
        Test(python_loop_in_list, vector, repetitions=repetitions)
        Test(python_loop_in_list_f, vector, repetitions=repetitions)

        Test(python_list_comprehension, vector, repetitions=repetitions)
        Test(python_list_comprehension_f, vector, repetitions=repetitions)

        Test(numpy_, vector, repetitions=repetitions)

    Test(numpy_f, vector, repetitions=repetitions)

    Test(numba_in_range, vector, repetitions=repetitions)
    Test(numba_in_range_f, vector, repetitions=repetitions)
    
    Test(numba_parallel, vector, repetitions=repetitions)
    Test(numba_parallel_f, vector, repetitions=repetitions)
    
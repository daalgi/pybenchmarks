import timeit, time, random
import numpy as np

from base import Test

def python_loop_in_list(a, b):
    matrix_out = []
    for r in a:
        row_out = []
        for c in zip(*b):
            products = []
            for i, j in zip(r, c):
                inputs = i, j
                products.append(i * j)
            row_out.append(sum(products))
            
        matrix_out.append(row_out)
    return matrix_out

def python_list_comprehension(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]

def numpy_matmul(a, b):
    return np.matmul(a, b)

def numpy_dot(a, b):
    return np.dot(a, b)


lengths = [2, 3, 4, 5, 6, 10, 20, 50, 100]#int(1e2), int(1e3)]
repetitions = 10000
for length in lengths:
    print(f"\nMATRIX SIZE = {length:.0f}x{length:.0f} -- REPETITIONS = {repetitions}")
    a = np.random.random((length, length))
    b = np.random.random((length, length))
    if length < 50:
        Test(python_loop_in_list, (a, b), repetitions=repetitions, verbose=False)
        Test(python_list_comprehension, (a, b), repetitions=repetitions, verbose=False)
    Test(numpy_matmul, (a, b), repetitions=repetitions, verbose=False)
    Test(numpy_dot, (a, b), repetitions=repetitions, verbose=False)
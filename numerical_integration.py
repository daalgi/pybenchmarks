import numpy as np
import scipy.integrate
import quadpy

from base import Test


RADIUS = 10

def width(r: float):
    if abs(r) <= RADIUS:
        return 2 * np.sqrt(RADIUS * RADIUS - r * r)
    return 0

def stress_at(r: float):
    if r < RADIUS / 2:
        return (RADIUS / 2 - r) * 0.05
    return 0

def f(r: float):
    return stress_at(r) * width(r) * r

def fv(r):
    return stress_at(r[0]) * width(r[0]) * r[0]

def scipy_quad(a, b):   
    return scipy.integrate.quad(f, a, b)[0]

def scipy_quad_vec(a, b):   
    return scipy.integrate.quad_vec(f, a, b)[0]

def quadpy_integration(a, b):
    return quadpy.quad(fv, a, b)

# def numba_scipy(integrand, a, b):
#     return 0

repetitions = 2000

print(f"\nNUMERICAL INTEGRATION -- REPETITIONS = {repetitions}")

a = +RADIUS
b = -RADIUS

# print(scipy_integration(a, b))
Test(scipy_quad, (a, b), repetitions=repetitions, verbose=False)
Test(scipy_quad_vec, (a, b), repetitions=repetitions, verbose=False)
# Test(numba_scipy, (a, b), repetitions=repetitions, verbose=False)
# print(quadpy_integration(a, b))
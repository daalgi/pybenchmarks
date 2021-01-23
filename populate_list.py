from base import Test


NUMBER = 8.8

def full_size_zeros(length):
    s = [0] * length
    for i in range(length):
        s[i] = NUMBER
    return s

def full_size_nones(length):
    s = [None] * length
    for i in range(length):
        s[i] = NUMBER
    return s

def appending(length):
    s = []
    for i in range(length):
        s.append(NUMBER)
    return s


lengths = [int(1e1), int(1e2), int(1e3), int(1e4), int(2e4), int(5e4)]
repetitions = int(1e4)
for length in lengths:
    print(f"\nVECTOR LENGTH = {length:.0E} -- REPETITIONS = {repetitions}")

    Test(full_size_zeros, length, repetitions=repetitions, verbose=False)
    Test(full_size_nones, length, repetitions=repetitions, verbose=False)
    Test(appending, length, repetitions=repetitions, verbose=False)
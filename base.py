import time
import numpy as np


SECONDS_BY = {
    "min": 1/60,
    "s": 1,
    "ms": 1e3,
    "ns": 1e9
}

class Test:

    def __init__(self, function, 
        args = None, 
        repetitions: int = 1, 
        verbose=False, 
        test_name_spaces: int = 30,
        time_spaces: int = 15,
        time_decimals: int = 4,
        units: str = "ms"
    ):
        name = function.__name__
        
        # Evaluate the function performance
        if args is None:
            # Function without arguments
            t = time.time()    
            for i in range(repetitions):
                a = function()
            t = time.time() - t
        elif isinstance(args, tuple):
            # Function without arguments
            t = time.time()    
            for i in range(repetitions):
                a = function(*args)
            t = time.time() - t
        else:
            # Function with arguments
            t = time.time()    
            for i in range(repetitions):
                a = function(args)
            t = time.time() - t            

        # Print results
        res = f'{name}()'
        res += f'{" " * (test_name_spaces-len(name))}'
        res += f'\t{t*SECONDS_BY[units]:>{time_spaces}.{time_decimals}f}'
        res += f' {units}'
        print(res)

        # Print result returned from the function
        if verbose:
            if isinstance(a, (list, np.ndarray, np.generic)):
                n = len(a)
                print(a[:min(n, 3)])
            else:
                print(a)


def random_vector(length):
    return np.random.random(length)
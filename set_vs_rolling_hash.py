from random import randint

from base import Test


def set_in_str(strings: set, s: str):
    return s in strings

def set_in_int(strings: set, s: int):
    return s in strings

def rolling_hash(strings: set, s: str):
    return


if __name__ == "__main__":

    string_len = 20
    max_length = int(1e6)
    lengths = [int(1e1), int(1e2), int(1e3), int(1e4), int(1e5), int(1e6)]
    strings = [
        "".join(
            chr(randint(0, 26) + ord('a')) for _ in range(string_len)
        ) for _ in range(max_length)
    ]
    integers = list(range(max_length))
    # String not in the set, for comparison
    string = 'z' * (string_len + 1)
    integer = max_length

    repetitions = int(1e2)
    for length in lengths:
        print(f"\nSET LENGTH = {length:.0E} -- REPETITIONS = {repetitions}")

        curr_strings = strings[:length]
        curr_integers = integers[:length]

        Test(set_in_str, (curr_strings, string), repetitions=repetitions, verbose=False)
        Test(set_in_int, (curr_integers, integer), repetitions=repetitions, verbose=False)

        # Test(rolling_hash, length, repetitions=repetitions, verbose=False)
        
from base import Test


def if_assignment_each_iter(length):
    maxi = -float("inf")
    for num in range(length):
        if num > maxi:
            maxi = num
    return maxi


def if_assignment_only_once_needed(length):
    maxi = -float("inf")
    for num in range(length - 1, -1, -1):
        if num > maxi:
            maxi = num
    return maxi


def max_each_iter(length):
    maxi = -float("inf")
    for num in range(length):
        maxi = max(maxi, num)
    return maxi


def max_each_iter_but_only_once_needed(length):
    maxi = -float("inf")
    for num in range(length - 1, -1, -1):
        maxi = max(maxi, num)
    return maxi


if __name__ == "__main__":

    lengths = [int(1e1), int(1e2), int(1e3), int(1e4), int(1e5), int(1e6)]
    repetitions = int(1e2)
    for length in lengths:
        print(f"\nVECTOR LENGTH = {length:.0E} -- REPETITIONS = {repetitions}")

        Test(if_assignment_each_iter, length, repetitions=repetitions, verbose=False)
        Test(max_each_iter, length, repetitions=repetitions, verbose=False)
        Test(
            if_assignment_only_once_needed,
            length,
            repetitions=repetitions,
            verbose=False,
        )
        Test(
            max_each_iter_but_only_once_needed,
            length,
            repetitions=repetitions,
            verbose=False,
        )

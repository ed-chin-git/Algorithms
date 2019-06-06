#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    # Number of cookies cookie monster can eat is:
    # 0, 1, 2, 3
    ways = 0
    for i in range(1, 4):  # start at 1
        if cache is not None:
            #  use cache list
            if cache[n - i] == 0:
                cache[n - i] = eating_cookies(n - i, cache)
            ways += cache[n - i]
        else:
            # Naive recursion
            ways += eating_cookies(n - i)
    if cache is not None:
        # send results to cache
        cache[n] = ways
    return ways

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

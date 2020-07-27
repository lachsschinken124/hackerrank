#!/bin/python3

import os
import sys
from math import factorial as fac
modulo = 10**9 + 7
# Complete the solve function below.
def solve(n, m):
    return fac(n+m-1) // fac(n) // fac(m-1) % modulo


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

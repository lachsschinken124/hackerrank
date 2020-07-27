#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleycount = 0
    sealevel = 0
    for i, char in enumerate(s):
        if char == "D" and sealevel == 0:
            valleycount += 1
            sealevel -= 1
        elif char == "D":
            sealevel -= 1
        elif char == "U":
            sealevel += 1
    return valleycount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python

# Complete the function below.


def maxXor(one,two):
    ret = 0
    for first in xrange(one,two+1):
        for second in xrange(first, two+1):
            xor = first ^ second
            if ret < xor:
                ret = xor
    return ret
            

    

l = int(raw_input());


r = int(raw_input());

res = maxXor(l,r);
print(res)
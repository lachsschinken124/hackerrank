# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, floor
t = int(raw_input())
for c1 in xrange(0,t):
    a, b = [int(c2) for c2 in raw_input().split()]
    print int(sqrt(b))-int(sqrt(a-1))
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
array = []
sum1, sum2 = 0,0
for s in xrange(0,n):
    line = raw_input().split()
    line = [ int(x) for x in line ]
    array.append(line)
    sum1 += line[s]
    sum2 += line[n-s-1]
print abs(sum1-sum2)
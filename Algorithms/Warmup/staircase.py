# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
for x in xrange(0,n):
    print " "*(n-x-1) + "#"*(x+1)
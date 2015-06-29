# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
rw = raw_input().split()
if not len(rw) == n:
    print "bijkadk"
for x in xrange(0,n):
    rw[x] = int(rw[x])
print sum(rw)
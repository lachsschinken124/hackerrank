# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for c1 in xrange(0,t):
    n,k = [int(c2) for c2 in raw_input().split()]
    students = [int(c3) for c3 in raw_input().split()]
    ontime = 0
    for s in students:
        if s <= 0:
            ontime += 1
    if ontime >= k:
        print "NO"
    else:
        print "YES"
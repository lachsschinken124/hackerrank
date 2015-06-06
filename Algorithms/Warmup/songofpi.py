# Enter your code here. Read input from STDIN. Print output to STDOUT
pi = "31415926535897932384626433833"
pilist = []
for item in pi:
    pilist.append(item)
length = int(raw_input())
for z in xrange(0, length):
    line = raw_input().split()
    cond = True
    for x in xrange(0,len(line)):
        if not (int(pilist[x]) == len(line[x])):
            cond = False
    if cond:
        print "It's a pi song."
    else:
        print "It's not a pi song."
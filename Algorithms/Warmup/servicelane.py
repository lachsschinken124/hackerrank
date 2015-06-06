# Enter your code here. Read input from STDIN. Print output to STDOUT
lhigh, rows = raw_input().split()
high = raw_input().split()
lhigh, rows = int(lhigh), int(rows)
for x in xrange(0,rows):
    enter, exit = raw_input().split()
    enter, exit = int(enter), int(exit)
    maxwidth = 3
    for y in xrange(enter,exit+1):
        currentWidth = int(high[y])
        if currentWidth < maxwidth:
            maxwidth = currentWidth
    print maxwidth
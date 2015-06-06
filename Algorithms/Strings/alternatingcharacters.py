# Enter your code here. Read input from STDIN. Print output to STDOUT
numberoflines = input()
for something in xrange(0,numberoflines):
    line = raw_input()
    dele = 0
    lastchar = ""
    for char in str(line):
        if char == lastchar:
            dele += 1
        lastchar = char
    print dele
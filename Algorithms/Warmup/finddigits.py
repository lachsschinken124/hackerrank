trues = 0
linecount = input()
for trash in xrange(0,linecount):
    line = input()
    for n in str(line):
        if int(n) == 0:
            continue
        if int(line) % int(n) == 0:
            trues += 1
    print trues
    trues = 0
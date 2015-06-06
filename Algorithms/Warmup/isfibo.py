# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b= 1, 0
fibs = []
while a < 10000000000:
    a, b = a + b, a
    fibs.append(a)
numlines = input()
for something in xrange(0, numlines):
    number = input()
    if int(number) in fibs:
        print "IsFibo"
    else:
        print "IsNotFibo"
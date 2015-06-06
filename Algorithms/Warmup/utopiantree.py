# Enter your code here. Read input from STDIN. Print output to STDOUT

t = input()
for something in xrange(0,t):
    cycle = input()
    height = 1
    for curr in xrange(1,cycle+1):
        if curr % 2 == 1:
            height *= 2
        else:
            height += 1
    print height
        
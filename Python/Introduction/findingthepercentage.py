# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
dictionary = {}
for c1 in xrange(0,n):
    inp = raw_input().split()
    name = inp.pop(0)
    dictionary[name] = inp
search = raw_input()
if search in dictionary:
    numlist = dictionary[search]
    out = 0
    for num in numlist:
        out += float(num)
    print "{0:.2f}".format(float(out)/len(numlist))
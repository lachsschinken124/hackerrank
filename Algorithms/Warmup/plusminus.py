# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
array = [int(x) for x in raw_input().split() ]
pos, neg, zero = 0,0,0
for x in array:
    if x > 0:
        pos += 1
    elif x == 0:
        zero += 1
    else:
        neg += 1
length = float(len(array))
print pos/length
print neg/length
print zero/length
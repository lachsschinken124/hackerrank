# Enter your code here. Read input from STDIN. Print output to STDOUT

abc = "abcdefghijklmnopqrstuvwxyz"
if not len(abc) == 26:
    raise Exception("abc variable wrong")

def caesar(char, rot):
    if not char.isalpha():
        return char
    upper = char.isupper()
    char = char.lower()
    pos = abc.index(char)
    pos += rot
    while pos > 25:
        pos -= 26
    if upper:
        return abc[pos].upper()
    return abc[pos]

n = int(raw_input())
string = raw_input()
k = int(raw_input())
finals = ""

for s in string:
    finals += caesar(s,k)
print finals
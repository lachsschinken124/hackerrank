string = raw_input()
 
found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
last = ""
counter = 0
allow = True
ordered = []
for x in string:
    ordered.append(x)
ordered.sort()
#print ordered
for x in ordered:
    if last == x:
        counter += 1
    else:
        if last == "":
            last = x
            counter = 1
            continue
        elif counter % 2 == 0:
            counter = 1
            last = x
            continue
        else:
            if allow:
                allow = False
                last = x
                counter = 1
                continue
            print "NO"
            found = False
            break
if found:
    print "YES"
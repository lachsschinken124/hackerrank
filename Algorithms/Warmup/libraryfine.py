# Enter your code here. Read input from STDIN. Print output to STDOUT
def fine():
    actual = raw_input().split()
    expected = raw_input().split()
    
    actual = [int(x) for x in actual]
    expected = [int(x) for x in expected]

    # Check if year is the same
    if actual[2] > expected[2]:
        return 10000 
    elif actual[1] > expected[1] and actual[2] == expected[2]:
        return 500 * (actual[1]-expected[1]) 
    elif actual[0] > expected[0] and actual[1:] == expected[1:]:
        return 15 * (actual[0]-expected[0])
    else:
        return 0
    
print fine()
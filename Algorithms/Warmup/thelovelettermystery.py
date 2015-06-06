alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = int(raw_input())
for c1 in xrange(0,n):
	inp = list(raw_input())
	changeCount = 0
	posn = -1
	for pos in xrange(0,len(inp)/2):
		changeCount += abs(alp.index(inp[pos]) - alp.index(inp[posn]))
		posn -= 1
	print changeCount



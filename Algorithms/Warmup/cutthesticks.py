n = int(raw_input())
sticksraw = raw_input().split()
sticks = []
for c3 in sticksraw:
	sticks.append(int(c3))
stop = False
while len(sticks) > 0:
	print len(sticks)
	shortest = 1001
	for c1 in xrange(0,len(sticks)):
		if shortest > sticks[c1]:
			shortest = sticks[c1]
	nl = []
	for c2 in xrange(0, len(sticks)):
		curr = sticks[c2] - shortest
		if not curr == 0:
			nl.append(curr)
	sticks = nl
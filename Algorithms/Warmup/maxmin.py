N = input()
K = input()
candies = [input() for _ in range(0,N)]
candies.sort()
best = candies[-1];
    
for i in xrange(N - K + 1):
	
    if (candies[i + K - 1] - candies[i]) < best:
	    
	best = candies[i + K - 1] - candies[i]

print best
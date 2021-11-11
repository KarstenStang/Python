import itertools

def calc(values):
	if len(values) == 1:
		return values

	results = []
	for i in range(1, len(values)):
		for a in calc(values[i:]):
			for b in calc(values[:i]):
				if b > 0:
					results += [a+b, a-b, a*b, a/b]

	return results

maxLen = 0
maxSet = ""
for a in range(7):
	for b in range(a + 1, 8):
		for c in range(b + 1, 9):		
			for d in range(c + 1, 10):
				results = []
				for values in list(itertools.permutations([a,b,c,d])):
					results += [val for val in calc(values) if abs(int(val)) == val]

				results = sorted(list(set(results)))
				for i in range(len(results)):
					if i != results[i]:
						if i > maxLen:
							maxLen = i -1
							maxSet = str(a) + str(b) + str(c) + str(d)
						break

print(maxSet)

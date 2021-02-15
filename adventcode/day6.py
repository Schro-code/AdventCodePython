
with open("input6.txt") as f:
	data = f.read().strip().split("\n\n")

#inp = [a.split("\n") for a in data]
print(set.intersection({1,2,3},[1,2,3,4]))
#print(set(inp[0][0]))
def p1(data):
	return sum([len(set(i)) if not "\n" in i else len(set(i))-1  for i in data])

def p2(data):
	sol = 0
	for i in data:
		for e in i:
			if len(e) == 0:
				break
			vlue = set(e)
			#print(vlue)
			for a in i:
				vlue = vlue.intersection(set(a))
		sol += len(vlue) 
	return sol

#print(p2(inp))

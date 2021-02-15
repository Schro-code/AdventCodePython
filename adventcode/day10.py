with open("input10.txt") as f:
	inp = f.read().splitlines()

def parseInp(inp):
	a =  sorted([int(a) for a in inp]) 
	return [0] + a + [max(a)+3]

def p1(inp):
	differences = []
	for index in range(len(inp)-1):
		differences.append(int(inp[index+1])-int(inp[index]))	
	return differences[:]

def star1(inp):
	diff = p1(inp)
	oneJolt = diff.count(1)
	threeJolt = diff.count(3)
	return oneJolt*threeJolt
def p2(inp):
	value = 1
	unos = 0
	for i in inp:
		if i == 3:
			if unos == 2:
				value *= 2
			if unos == 3:
				value *=4
			if unos == 4:
				value *=7
			unos = 0
		else:
			unos +=1
	return value




example = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines()

#print(p2(p1(parseInp(example))))

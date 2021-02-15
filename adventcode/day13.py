

with open("input13.txt") as f:
	inp =f.read().splitlines()

def parseInp(inpt):
	return [int(inpt[0])] + [int(i) for i in inp[1].split(",") if i != "x"]

def parseInp2(inp):
	inp = [i if i == "x" else int(i) for i in inp[1].split(",")]
	index = 0
	xindex = 0
	x = 0
	data = []
	while xindex < len(inp):	
		if inp[xindex] == "x":		
			xindex += 1
		else:
			index = xindex
			xindex +=1
			data.append((inp[index],inp[index]-x%inp[index]))
			#x = 
		x += 1
	return data

def star2(inp):
	x = inp[0][1]      #x = 0 mod 13
	step = inp[0][0]
	index = 0
	while index+1 < len(inp):	
		if x%inp[index+1][0]==inp[index+1][1]:
			step *= inp[index+1][0]
			index += 1
		else:
			x += step
	return x

def star1(arrival,inp):
	clock = arrival
	while True:
		sub = list(map(lambda x:clock%x,inp))
		if 0 in sub:
			timestamp = clock
			index = sub.index(0)
			return inp[index]*(clock-arrival)		
		clock +=1

#inp1 = parseInp(inp)
#print("day 13 star1 : {}".format(star1(inp1[0],inp1[1:])))
#inp2 = parseInp2(inp)
#print("day 13 star2 : {}".format(star2(inp2)))

print(True < False)

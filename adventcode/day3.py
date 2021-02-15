

with open("input3.txt") as inp:
	listainput = inp.read().splitlines() 

def p1(inp):
	width = len(inp[0])
	tall = len(inp)
	return sum([ 1 if inp[i][3*i%width]=="#" else 0 for i in range(tall)])

def p2(inp,av):
	avance = [(1,1),(1,3),(1,5),(1,7),(2,1)]
	width = len(inp[0])
	tall = len(inp)
	i,j,sol =0,0,0
	while i < tall-1:		
		sol += inp[i][j%width] == "#"
		i += avance[av][0]
		j += 	avance[av][1]
	return sol

print(p2(listainput,0)*p2(listainput,1)*p2(listainput,2)*p2(listainput,3)*p2(listainput,4))



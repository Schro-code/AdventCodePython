
with open("input5.txt") as inp:
	inp = inp.read().splitlines() 


def p2(inp):
	lista = []
	for e in inp:
		lista.append(row(e))

	for i in range(min(lista),max(lista)):
		if not i in lista:
			return i


def row(coordenates):
	i,j = 0,127
	x,y = 0,7
	for e in coordenates[:7]:
		if e == "F":
			j -= int((j-i)/2)+1

		if e == "B":
			i += int((j-i)/2)+1
	for e in coordenates[7:]:
		#print(e,x,y)
		if e == "L":
			y -= int((y-x)/2)+1

		if e == "R":
			x += int((y-x)/2)+1

	return i*8+x
print(p2(inp))
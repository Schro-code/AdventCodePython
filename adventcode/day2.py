
with open("input.txt") as inp:
  listaconlineas = inp.read().splitlines()


def p1(inp):  #"a-b x: yyyy"
	password = inp.split()  #[a-b,x:,yyyy]
	letter = password[1][0]
	string = password[-1]
	cond = password[0].split("-")
	c = string.count(letter)

	return int(cond[0])<= c <=int(cond[1])


def solution(puzzle):
	sol = 0
	for e in puzzle:		
		sol +=p1(e)
	return sol

def p2(inp): #"a-b x: yyyy"
	password = inp.split()  #[a-b,x:,yyyy]
	letter = password[1][0]
	string = password[-1]
	cond = password[0].split("-")
	return (letter == string[int(cond[0])-1])^(letter == string[int(cond[1])-1])


def solution2(puzzle):
	sol = 0
	for e in puzzle:		
		sol +=p2(e)
	return sol
print(solution2(listaconlineas))
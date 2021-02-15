import re

with open("input8.txt") as f:
	data = f.read().splitlines()

#print(data)

def parseInp(inp):
	inp = [re.split(r"\s",instr)+[False] for instr in inp]
	
	return inp
	
def p1(inp):

	acc = 0
	index = 0
	while True:		
		#['acc', '+22', False]
		if index == len(inp):
			return acc
		if inp[index][-1]:
			return False

		inp[index][-1]=True

		if inp[index][0] == "acc":			
			acc += int(inp[index][1])
			index +=1

		elif inp[index][0] == "jmp":			
			index += int(inp[index][1])
		else:			
			index +=1

def p2(inp):
	vlue = False
	index = 0
	while True:
		program = [i[:]for i in inp]
		if program[index][0] == "nop" :
			program[index][0] = "jmp"
			vlue = p1(program)

		elif program[index][0] == "jmp":
			program[index][0] = "nop"
			vlue = p1(program)
		if type(vlue) == int:
			return vlue
		print(program)
		index += 1



			
"""data = nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()
print()
print(p2(parseInp(data)))
#print(parseInp(data))
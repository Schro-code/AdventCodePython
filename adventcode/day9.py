

with open("input9.txt") as f:
	inp = f.read().splitlines()

#print(inp)

def p1(inp):
	i,j=0,24
	while True:
		exist = valid(inp[j+1],inp[i:j+1])
		if not exist:
			return inp[j+1]
		i+=1
		j+=1

def valid(value,preamble):

	a = [True if int(preamble[i])+int(preamble[j])==int(value) else False for i in range(len(preamble)) for j in range(i+1,len(preamble))]
	return True in a


def p2(inp,number):
	i,j=0,1
	while j < len(inp):	
		value = sum(inp[i:j])
		if value == number:

			return max(inp[i:j])+min(inp[i:j])
		if value > number:
			i+= 1
			j = i+1
		else:
			j += 1 



example = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()
example = [int(e) for e in example]
inp = [int(e) for e in inp]
#print(p2(example,127))
print(p2(inp,10884537))



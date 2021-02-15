import re
with open("input14.txt") as f:
	inp = f.read().splitlines()


def parseInp(inp):
	data = []
	for line in inp:  #mask = 11110100010101111011001X0100XX00100X    mem[44304] = 31572  
		inst, value = re.split(" = ",line)
		if inst == "mask":
			data.append(("mask",value))
		else:
			mem = re.match(r"mem\[(\d*)\]",inst)
			data.append((int(mem.group(1)),int(value)))

	return data


def value_after_bitmask(bitmask,default):
	return int("".join([bit if bit != "X" else str(default) for bit in bitmask]),2)

def decimal_to_binary(decimal):
	return bin(decimal).replace("b","")

def real_bitmask_and_adress(bitmask,adress):
	bitmask = bitmask[::-1]
	adress = adress[:0:-1]
	for index in range(len(bitmask)):
		if index == len(adress):
			return bitmask[::-1]
		else:
			if adress[index] == "1" and bitmask[index] != "X":
				bitmask = bitmask[:index] + "1" + bitmask[index+1:]
				#bitmask[index] = "1"
	return bitmask[::-1]

def get_all_adresses(adress, index = 0):
	list_of_adresses = []
	if adress.isnumeric():
		return [adress]
	while index < len(adress):
		if adress[index] == "X":
			adress_0 = adress[: index] + "0" + adress[index+1:]		
			list_of_adresses += get_all_adresses(adress_0,index)
			adress_1 = adress[: index] + "1" + adress[index+1:]		
			list_of_adresses += get_all_adresses(adress_1,index)
		index +=1
	return list_of_adresses


def star1(inp):
	memory = dict()
	for inst in inp:
		if inst[0] == "mask":
			bitmask = inst[1]
		else:
			AND = value_after_bitmask(bitmask,1)
			OR = value_after_bitmask(bitmask,0)
			memory[inst[0]] = inst[1] & AND | OR
	return sum(memory.values())


def star2(inp):
	memory = dict()
	for inst in inp:
		if inst[0] == "mask":
			bitmask = inst[1]	
		else:
			real_adress = real_bitmask_and_adress(bitmask,decimal_to_binary(inst[0]))
			all_adresses = get_all_adresses(real_adress)
			for adress in all_adresses:
				memory[adress] = inst[1]
	return sum(memory.values())




print(f"Day 14 star1 : {star1(parseInp(inp))}")
print("Day 14 star2 : {}".format(star2(parseInp(inp))))


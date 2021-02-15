import re


with open("input4.txt") as f:
	data = f.read().split("\n\n")



def p1(data):
	value = 0
	for i in data:
		value += valid2(i)
	return value

def valid(passport):
	passport_list = passport.split()
	if len(passport_list) == 8:
	 	return True
	elif len(passport_list) == 7:
		for e in passport_list:
			if "cid" in e:
				return False
		return True
	return False

def valid2(passport):
	passport_list = passport.split()
	#rint(passport_list)
	if len(passport_list) == 8:
		for i in passport_list:
			if not aux(i):
				return False
		return True
	 	
	elif len(passport_list) == 7:
		for e in passport_list:
			if "cid" in e:
				return False
		for i in passport_list:
			if not aux(i):
				return False	
		return True
	return False

def aux(string):
	a = string.split(":")
	if a[0] == "byr":
		return 1920 <= int(a[1]) <=2002 and len(a[1]) == 4
	elif a[0] == "iyr" :
		return 2010 <= int(a[1]) <=2020 and len(a[1]) == 4
	elif a[0] == "eyr":
		if a[1].isnumeric():
			return 2020 <= int(a[1]) <=2030 and len(a[1]) == 4
		return False
	elif a[0] == "cid":
		return True
	elif a[0] == "hgt":
		return (a[1][-2:] == "cm" and 150 <= int(a[1][:-2]) <= 193) or (a[1][-2:] == "in" and 59 <= int(a[1][:-2]) <= 76)
	elif a[0] == "hcl":
		lis = [str(a) for a in range(10)]
		if a[1][0] != "#":
			return False
		if len(a[1])==7:
			for i in a[1][1:]:
				if not i in lis and not i in "abcdef":
					return False
			return True
		return False

	elif a[0] == "ecl" :
		return a[1] in ["amb","blu","brn","gry","grn","hzl","oth"]

	elif a[0] == "pid" :
		return len(a[1]) == 9 and a[1].isnumeric()

#rint(aux("byr:1937"))
print(p1(data))
print(valid2("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"))
print(aux("cid:129"))
import re

with open("input12.txt") as f:
	inp = f.read().splitlines()


def getRotation(waypoint,amount): #waypoint [x,y]
	waypoint = waypoint[:]
	if amount <0:
		amount = 360+amount
	amount %= 360
	if amount == 90:
		waypoint = [waypoint[1],-waypoint[0]]
	if amount == 180:
		waypoint = [-waypoint[0],-waypoint[1]]
	if amount == 270 :
		waypoint =  [-waypoint[1],waypoint[0]]
	return waypoint

def star2(inp):

	waypoint = [10,1]

	north = 0
	east =  0
	for instr in inp:

		if instr[0] == "L":
			waypoint = getRotation(waypoint,-int(instr[1:]))
		if instr[0] == "R":
			waypoint = getRotation(waypoint,int(instr[1:]))
		elif instr[0] == "N":
			waypoint[1] += int(instr[1:])
		elif instr[0] == "S":
			waypoint[1] -= int(instr[1:])
		elif instr[0] == "W":
			waypoint[0] -= int(instr[1:])
		elif instr[0] == "E":
			waypoint[0] += int(instr[1:])
		
		if instr[0] == "F":
			north +=  int(instr[1:])*waypoint[1]
			east +=  int(instr[1:])*waypoint[0]
		print(instr,east,north,waypoint)
	return abs(north) + abs(east)

example = """F10
N3
F7
R90
F11""".splitlines()
print(star2(inp))		

		

def star1(inp):
	dirrection = 90    #north 0, west 270, south 180, east 90
	north = 0
	east = 0
	for instr in inp:
		if instr[0] == "R":
			dirrection += int(instr[1:])
		elif instr[0] == "L":
			dirrection -= int(instr[1:])
		elif instr[0] == "F":
			if dirrection == 0: #North
				north += int(instr[1:])
			elif dirrection == 180: #South
				north -= int(instr[1:])
			elif dirrection == 90: #East
				east += int(instr[1:])
			elif dirrection == 270: #East
				east -= int(instr[1:])
		elif instr[0] == "N":
			north += int(instr[1:])
		elif instr[0] == "S":
			north -= int(instr[1:])
		elif instr[0] == "W":
			east -= int(instr[1:])
		elif instr[0] == "E":
			east += int(instr[1:])
		dirrection = dirrection%360
	return abs(north) + abs(east)


				
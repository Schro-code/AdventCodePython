inp = [int(i) for i in "12,1,16,3,11,0".split(",")]





def star1(inp):
	turn = len(inp)+1

	before_and_last_spoken = {spoken:[turn]for turn,spoken in enumerate(inp,1)}
	last = inp[-1]
	while turn != 30000001:
		print(turn)
		if last in before_and_last_spoken.keys():
			if len(before_and_last_spoken[last]) == 1:
				last = 0
				if last in before_and_last_spoken.keys():
					before_and_last_spoken[last].append(turn)
				else:
					before_and_last_spoken[last] =[turn]

			else:
				last = before_and_last_spoken[last][-1] - before_and_last_spoken[last][-2]
				if last in before_and_last_spoken.keys():
					before_and_last_spoken[last].append(turn)
				else:
					before_and_last_spoken[last] =[turn]

		else:
			before_and_last_spoken[last] =[turn]
		turn +=1
	return last





print(star1(inp))

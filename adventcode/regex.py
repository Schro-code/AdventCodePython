import re
sentence = """abcdefg.abc
	asd1
asd123"""
pattern = re.compile(r"[.")
matches = pattern.finditer(sentence)

for match in matches:
	print(match)


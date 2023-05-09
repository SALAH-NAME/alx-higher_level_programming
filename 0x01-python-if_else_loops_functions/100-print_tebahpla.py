#!/usr/bin/python3

for alf in reversed(range(65,123)):
	if alf < 97 and alf > 90:
		pass
	else:
		print("{}".format(chr(alf)), end='')

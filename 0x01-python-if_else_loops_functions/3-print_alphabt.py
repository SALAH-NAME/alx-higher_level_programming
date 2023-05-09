#!/usr/bin/python3
for alf in range(97,123):
	if alf == ord('q') or alf == ord('e'):
		continue
	print("{}".format(chr(alf)), end='')

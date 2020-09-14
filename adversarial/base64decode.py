#!/usr/local/bin/python

import base64

with open("encrypted.txt") as file:
	lines=file.readlines()
	for line in lines:
		decoded=base64.b64decode(line.encode())
		print(decoded.decode('latin'))
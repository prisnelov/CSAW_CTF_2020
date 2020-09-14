#!/usr/bin/env python3

import hashpumpy
import requests
from base64 import *

data = {"author":"mrNobody","note":"hacked"}

resp = requests.post("http://crypto.chal.csaw.io:5003/new", data=data).text

identifier = resp[19:].split(":")[0]
integrity = resp.split(":")[1][0:40]
decoded_identifier = b64decode(identifier)
identifier_suffix = "&admin=True&access_sensitive=True&entrynum=7"

for i in range(256):
	new_integrity=hashpumpy.hashpump(integrity, decoded_identifier, identifier_suffix, i)

	resp = requests.post("http://crypto.chal.csaw.io:5003/view", data={"id":b64encode(new_integrity[1].decode('unicode-escape').encode('unicode-escape')), "integrity":new_integrity[0]}).text
	if "flag" in resp:
		print(resp.split("\n")[2].split(":")[2][1:])
		print("secret length:", i)
		break


#!/usr/bin/env python3

import requests

#declaring entrynumm in the middle makes us to overwrite the value(in python dictionaries if same keys are declared then the value in the last key is taken)
data = {"author":"mrNobody","entrynum":"none","note":"hacked&admin=True&access_sensitive=True&entrynum=7"}

resp = requests.post("http://crypto.chal.csaw.io:5003/new", data=data).text

identifier = resp[19:].split(":")[0]
integrity = resp.split(":")[1][0:40]

resp = requests.post("http://crypto.chal.csaw.io:5003/view", data={"id":identifier, "integrity":integrity}).text

print(resp.split("\n")[2].split(":")[2][1:])
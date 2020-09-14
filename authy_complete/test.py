#!/usr/bin/env python3

import base64
import hashlib

payload = {"author":"1337","note":"AAAAAAAA&admin=True&access_sensitive=True&entrynum=7","entrynum":"none"}

if "author" not in payload.keys():
    print(">:(\n")
if "note" not in payload.keys():
    print(">:(\n")

if "admin" in payload.keys():
    print(">:(\n>:(\n")
if "access_sensitive" in payload.keys():
    print(">:(\n>:(\n")

info = {"admin": "False", "access_sensitive": "False" }
info.update(payload)
info["entrynum"] = 783

infostr = ""
for pos, (key, val) in enumerate(info.items()):
    infostr += "{}={}".format(key, val)
    if pos != (len(info) - 1):
        infostr += "&"

infostr = infostr.encode()

identifier = base64.b64encode(infostr).decode()

hasher = hashlib.sha1()
hasher.update(b"SECRET" + infostr)

print("info:", info)
print("infostr:", infostr.decode())

def view(info):
    if "id" not in info.keys():
        print("1>:(\n")
    if "integrity" not in info.keys():
        print("2>:(\n")

    identifier = base64.b64decode(info["id"]).decode()
    checksum = info["integrity"]

    params = identifier.replace('&', ' ').split(" ")
    note_dict = { param.split("=")[0]: param.split("=")[1]  for param in params }

    encode = base64.b64decode(info["id"]).decode('unicode-escape').encode('ISO-8859-1')
    hasher = hashlib.sha1()
    hasher.update(b'SECRET' + encode)
    gen_checksum = hasher.hexdigest()
    print(note_dict)
    if checksum != gen_checksum:
        print(">:(\n>:(\n>:(\n")

    try:
        entrynum = int(note_dict["entrynum"])
        if 0 <= entrynum <= 10:

            if (note_dict["admin"] not in [True, "True"]):
                print("3>:(\n")
            if (note_dict["access_sensitive"] not in [True, "True"]):
                print("4>:(\n")

            if (entrynum == 7):
                print("\nAuthor: admin\nNote: You disobeyed our rules, but here's the note: " + "FLAG" + "\n\n")
            else:
                print("Hmmmmm....")

        else:
            print("""\nAuthor: {})
Note: {}\n\n""".format(note_dict["author"], note_dict["note"]))

    except Exception as e:
        print(e)

view({"id":identifier, "integrity":hasher.hexdigest()})



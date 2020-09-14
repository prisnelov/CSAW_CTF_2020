#!/usr/bin/env python3

import zwsp_steg
import base64

f=open("encodedFile1","r")
encoded=f.read()
decoded=zwsp_steg.decode(encoded)
print(decoded)



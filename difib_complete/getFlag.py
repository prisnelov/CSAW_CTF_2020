#!/usr/bin/env python3

#importing Bifid 
from pycipher import Bifid
from string import *
from pwn import *

#given message:
message="snbwmuotwodwvcywfgmruotoozaiwghlabvuzmfobhtywftopmtawyhifqgtsiowetrksrzgrztkfctxnrswnhxshylyehtatssukfvsnztyzlopsv"

#list that holds all the lines of the rambling file
rambls=[]

#opening the given file and creating a list
with open("ramblings", "r") as file:
	pangrams=file.readlines()
	for pangram in pangrams:
		#removing punctuation, spaces, new lines, and "j" as Bifid ciphers do not involve j
		x=pangram.lower().translate(str.maketrans("","",punctuation)).replace(" ", "").replace("\n", "").replace("j", "")
		rambls.append(x)

#as the challenge name(difib=>reverse of bifid) suggest the real stuff in this challenge is to reverse the key 
for rambl in rambls[::-1]:
	#the keys should be less than 25 characters without j
	if len(rambl) < 26:
		#Bifid(<key>, <period(box grid)>).decipher(<cipher>)
		message=Bifid(rambl,5).decipher(message).lower()

#consider x as spaces
print(message.replace("x", " "))#================> ust some unnecessary te t that holds absolutely no meaning whatsoever and bears no significance to you in any way

#so by guessing we can arrive at "just some unnecessary text that holds absolutely no meaning whatsoever and bears no significance to you in any way"

#submit to the gaurd and get the flag \0/
connection=remote("crypto.chal.csaw.io","5004")
connection.sendlineafter("!", "just some unnecessary text that holds absolutely no meaning whatsoever and bears no significance to you in any way")
print(connection.recvall())

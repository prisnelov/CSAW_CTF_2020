#!/usr/bin/env python3
from pwn import *

#establishing remote connection and makind the connection interactive
connection = remote('crypto.chal.csaw.io', 5001)
answerList=[]#contains answer list

#used to loop through the answer list
def answerFiller():
	for i in answerList:
		connection.sendlineafter(":","a", timeout=1)
		connection.sendlineafter("?",i)

#used to convert "ECB"=>0 and "CBC"=>1 and printing flag
def converter():
	binFlag=""
	flag=""
	#convert "ECB"=>0 and "CBC"=>1
	for y in answerList: 
		if y == "ECB":
			binFlag+="0"
		else:
			binFlag+="1"
	#take 8 bits change to character and append to flag
	for x in range(0, len(answerList), 8):
		flag+=chr(int(binFlag[x:x+8], 2))
		print(flag)

i=0
#looping to find the answerList
while True:
	try:
		connection.sendlineafter(":","a", timeout=1)
		answerList.append("ECB")#appending ECB at the end and checking whether it's correct if it is correct proceed and save to answerList
		connection.sendlineafter("?",answerList[i])
		i+=1
	#connection breaks or wrong answer
	except EOFError:
		answerList.pop()#delete the last answer("ECB") in answerList
		answerList.append("CBC")#append "CBC"
		print("*"*50)
		converter()
		print("*"*50)
		connection = remote('crypto.chal.csaw.io', 5001)#establish connection again
		answerFiller()#loop through the answer and continue ones the answerList is finished
		continue

connection.interactive()
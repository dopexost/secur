#!/usr/bin/python

#Code for Python 2.7.

import re
import commands

scan = "sudo /usr/bin/clamscan -i -r %s"
path = "/home/%s"
big = '>'
file = "io.txt"

result = 'FindeINC.py'

f = open('login.txt','r')
for line in f.readlines(): line

more = big + '%s' 
alfa = (line[1]) + '%s'
login = line + '%s'

logins = re.sub("\s*\n\s*", ' ', login.strip()) 

#commands
stroka = str(scan % path % alfa % logins % more % file)
operationCheck = scan % path % alfa % logins % more % file
operationSend = 'mail -s "Virus Monitor" bigcaches@yandex.ru < io.txt'
operationRemove = 'rm io.txt'
#print stroka
resultCheck = commands.getoutput(operationCheck)
file_io = open('io.txt' , 'a')
file_io.write(logins)
file_io.close()
resultSend = commands.getoutput(operationSend)
resultRemove = commands.getoutput(operationRemove)
f.close() 



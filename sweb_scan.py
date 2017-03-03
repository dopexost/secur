#!/usr/bin/python

#Code for Python 2.7.

import commands
 
print ("-----------------------") 
m = raw_input ("  \033[1;36mlogin :\033[1;m")
#print (" ")
n = raw_input ("  \033[1;36mServer :\033[1;m")
print ("-----------------------")
my_file = open("login.txt", "w")
my_file.write("/"+m)
my_file.close()

operationServ = "scp scan.py " + n + ":/home/alsoldatov"
operationLogin = "scp login.txt " + n + ":/home/alsoldatov"

resultServ = commands.getoutput(operationServ)
resultLogin = commands.getoutput(operationLogin)

print('.........................................................................DONE............................................................ ')

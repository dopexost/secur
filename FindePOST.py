#!/usr/bin/python

#Code for Python 2.7.
#coding=UTF-

import commands

string = "access_log"

operations = "ls /var/log/nginx"

results = commands.getoutput(operations)

print ("-----------------------")
print results 
print ("-----------------------")
n = raw_input ("  \033[1;36mLogs Name :\033[1;m")
print (" ")
m = raw_input ("  \033[1;36mSite Name :\033[1;m")


if n == string: operation = "cat /var/log/nginx/" + (n) + " | grep  " + (m) + " > logname.txt " 

else: operation = "zcat /var/log/nginx/" + (n) + " | grep  " + (m) + " > logname.txt "

result = commands.getoutput(operation)

operationfind = "cat logname.txt | grep POST"

find = commands.getoutput(operationfind)

print ("-------------------------------- ")
print "        Work Done" + result
print ("-------------------------------- ")
print ("\033[1;31mPOST\033[1;m")
print find

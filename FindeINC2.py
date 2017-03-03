#!/usr/bin/python

#Code for Python 2.7.

import os, sys, fnmatch

stroka = "grep"

mask = '*'
pattern = "try{Boolean\(\)\.prototype\.q}catch\("


with open("baseVirus") as file:
    array = [row.strip() for row in file]
    #new_array = stroka.join((str(i) for i in array))

#for i in xrange(lan(array)) 

def walk(arg,dir,files):
   for file in files:
     if fnmatch.fnmatch(file,mask):
        name = os.path.join(dir,file)
        try:
          data = open(name,'rb').read()
          if data.find(pattern) != -1:
            print name
        except:
            pass    
os.path.walk('.',walk,[]) 


#my_file = open("baseVirus")
#my_string = my_file.read()
print("work done:")
#print new_array[2]
print array[5]

#!/usr/bin/python

#Code for Python 2.7.

import commands

result = 'FindeINC.py'

#commands
operation1 = 'grep -rl "\[\$GLOBALS\[" * '

operation2 = 'grep -rlE "\.chr\(" * '

operation3 = 'grep -rlE "auth_pass" * '

operation4 = 'grep -lr  "df5" * '

operation5 = 'grep -rl str_rot13 * '

operation6 = 'grep -lr "s20=strtoupper" * '

operation7 = 'grep -rl "Your IP" * '

operation8 = 'grep -lr "ob_start(); var_dump" * '

operation9 = 'grep -rl "eval(eval" * '

operation10 = 'grep -rlE "ver{" * '

operation11 = 'grep -rlE "fs_login_session" * '

operation12 = 'grep -lr "cookiename" * '


result1 = commands.getoutput(operation1)
result2 = commands.getoutput(operation2)
result3 = commands.getoutput(operation3)
result4 = commands.getoutput(operation4)
result5 = commands.getoutput(operation5)
result6 = commands.getoutput(operation6)
result7 = commands.getoutput(operation7)
result8 = commands.getoutput(operation8)
result9 = commands.getoutput(operation9)
result10 = commands.getoutput(operation10)
result11 = commands.getoutput(operation11)
result12 = commands.getoutput(operation12)


print("                                                           FIND INC VERSION 1.0")
print(' ')
print "\033[1;31m---------------------------------------------------GLOBALs-start--------------------------------------------------------------\033[1;m"
print '%s' %  (result1)
if result1 == (result):
 result1 = ('Not Found')
print "\033[1;31m---------------------------------------------------GLOBALs-finish-------------------------------------------------------------\033[1;m"

print (' ')

print "\033[1;32m-----------------------------------------------------Chr-start----------------------------------------------------------------\033[1;m"
if result2 == (result):
 result2 = ('Not Found')
print '%s' % (result2)
print "\033[1;32m-----------------------------------------------------Chr-finish---------------------------------------------------------------\033[1;m"

print(' ')

print "\033[1;34m---------------------------------------------------Auth_pass-start------------------------------------------------------------\033[1;m"
if result3 == (result):
 result3 = ('Not Found')
print '%s' % (result3)
print "\033[1;34m---------------------------------------------------Auth_pass-finish-----------------------------------------------------------\033[1;m"

print(' ')

print "\033[1;33m------------------------------------------------------#df5-start--------------------------------------------------------------\033[1;m"
if result4 == (result):
 result4 = ('Not Found')
print '%s' % (result4)
print "\033[1;33m-----------------------------------------------------#df5-finish--------------------------------------------------------------\033[1;m"

print(' ')

print "\033[0;31m---------------------------------------------------Str_rot13-start------------------------------------------------------------\033[1;m"
if result5 == (result):
 result5 = ('Not Found')
print '%s' % (result5)
print "\033[0;31m---------------------------------------------------Str_rot13-finish-----------------------------------------------------------\033[1;m"

print(' ')

print "\033[0;34m--------------------------------------------------S20=strtoupper-start--------------------------------------------------------\033[1;m"
if result6 == (result):
 result6 = ('Not Found')
print '%s' % (result6)
print "\033[0;34m--------------------------------------------------S20=strtoupper-finish-------------------------------------------------------\033[1;m"

print(' ')

print "\033[0;32m------------------------------------------------------Your-IP-start-----------------------------------------------------------\033[1;m"
if result7 == (result):
 result7 = ('Not Found')
print '%s' % (result7)
print "\033[0;32m------------------------------------------------------Your-IP-finish----------------------------------------------------------\033[1;m"

print(' ')

print "\033[0;36m-------------------------------------------------ob_start()-var_dump-start----------------------------------------------------\033[1;m"
if result8 == (result):
 result8 = ('Not Found')
print '%s' % (result8)
print "\033[0;36m-------------------------------------------------ob_start()-var_dump-finish---------------------------------------------------\033[1;m"

print(' ')

print "\033[1;33m---------------------------------------------------------eval-start-----------------------------------------------------------\033[1;m"
if result9 == (result):
 result9 = ('Not Found')
print '%s' % (result9)
print "\033[1;33m---------------------------------------------------------eval-finish----------------------------------------------------------\033[1;m"

print(' ')

print "\033[0;31m----------------------------------------------------------ver-start-----------------------------------------------------------\033[1;m"
if result10 == (result):
 result10 = ('Not Found')
print '%s' % (result10)
print "\033[0;31m----------------------------------------------------------ver-finish----------------------------------------------------------\033[1;m"

print(' ')

print "\033[1;35m--------------------------------------------------fs_login_session-start------------------------------------------------------\033[1;m"
if result11 == (result):
 result11 = ('Not Found')
print '%s' % (result11)
print "\033[1;35m--------------------------------------------------fs_login_session-finish-----------------------------------------------------\033[1;m"

print(' ')

print('.........................................................................DONE............................................................ ')


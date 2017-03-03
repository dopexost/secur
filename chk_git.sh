#!/bin/bash

while read line
do 
	user=`echo $line | awk '{print $1}'`
	server=`echo $line | awk '{print $2}'`
	sitefolder=`echo $line | awk '{print $3}'`
	echo -e '\033[0;31m'$user $server $sitefolder'\033[0m'
	if [ $# -eq 0 ]
		then
			command='git status'
		else
			command=$1
	fi
	ssh $server "dssu $user 'cd $sitefolder; $command'" </dev/null 2>&1 | grep -vF '/usr/sbin/mcpu is not running. Starting.' 

done <<EOF
dvboxru vh55 ~/arkalika/public_html
dvboxru vh55 ~/arkalikaus/public_html
dvboxru vh55 ~/arkalikaru/public_html
lerernet vh91 ~/public_html
bezgrainfo vh8 ~/public_html
dmitry4 vh236 ~/poxudet.com/public_html
printnsru vh39 ~/public_html
sportsusru vip36 ~/xyz-brakes/public_html
sportsusru vip36 ~/ruff/public_html
sportsusru vip36 ~/sport-suspension/public_html
sportsusru vip36 ~/hp-brakesru/public_html
specavt6ru specavtosnab.ru ~/specavtosnab.ru/public_html
swissspbru vh215 ~/public_html
EOF

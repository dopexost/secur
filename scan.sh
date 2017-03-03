#!/bin/bash
while read line
do
ssh alsoldatov@"$line" "./scan.py; ls;" < /dev/null
done < /home/alsoldatov/security/list.txt

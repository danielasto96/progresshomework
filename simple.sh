#!/bin/sh
if [ -d "/home/dani/homework" ]
then
        echo "Directory exists."
else
        echo "Error: Directory does not exists."
fi
mkdir homework
cd homework
touch content.txt
date >> content.txt
wc -l content.txt
date

#[ ! -d "/home/dani/homework" ] && mkdir -p /home/dani/homework
# That's the way how we create directory without IF does not exists

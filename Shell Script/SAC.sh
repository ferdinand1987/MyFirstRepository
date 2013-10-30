#! /bin/bash

count=0
echo "count=$count"
cat $1 | while true
do
	if read myline
	then
		let count+=1
	else
		echo "count=$count"
		break
	fi
done
echo "count=$count"

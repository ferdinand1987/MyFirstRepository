#! /bin/bash

if [[ $# -lt 2 || $# -gt 3 ]]
then
	echo "Please input: bash SearchAndCount SourceFile OutputFile(not necessary) TargetCharacter"
else
	SourceFile=$1

	if [[ $# == 2 ]]
	then
		OutputFile="Output.txt"
		Target=$2
	else
		OutputFile=$2
		Target=$3
	fi

	if [[ ${#Target} > 1 ]]
	then
		echo "The third parameter must be a character!"
	else
		Total=0
		cat $SourceFile | while true
		do
			if read myline
			then
				Count=0
				for (( i=0; i<${#myline}; i++ ))
				do
					if [[ "${myline:i:1}" == "$Target" ]]
					then
						let Count+=1
						echo -e "\033[1;42m\c"
						echo -e "$Target\c"
						echo -e "\033[0m\c"
					else
						echo -e "${myline:i:1}\c"
					fi
				done
				echo "  :$Count"
				let Total+=Count
			else
				echo "The number of matched $Target is $Total"
				echo "The number of matched $Target is $Total" >> $OutputFile
				break
			fi
		done
	fi
fi

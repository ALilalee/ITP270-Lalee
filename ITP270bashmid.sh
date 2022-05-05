#!/bin/bash
if [ "${UID}" -ne "0" ]
then 
	echo 'not root user, use sudo'
	exit 1
fi

for i in {0..1}; do
    read -p "Username: " U
    read -p "Password: " P
    if [ "${#P}" -le "7" ]
    then
        while [ "${#P}" -le "7" ]
        do
        echo "too short"
        read -p "Password: " P
        done
	useradd -M ${U}
         echo ${U}
         echo ${P}
    else
	useradd -M ${U}
         echo ${U}
         echo ${P}
    fi
 done  

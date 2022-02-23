#!/bin/bash

# Make sure the script is being executed with superuser privileges. (30)
if [["${UID}" -ne 0]]
then 
	echo 'not root user, use sudo'
	exit 1
fi

# Get the username (login). (30)
read -p "Enter Username to add: " UNAME

# Get the real name (contents for the description field). (30)
read -p "Enter full name: " NAME

# Get the password. (30)
read -p "Enter Password : " PASWRD

# Create the user with the password. (30)
useradd -c "${NAME}" -M ${UNAME}


# Check to see if the useradd command succeeded. (30)
if [["${?}" -ne 0 ]]
then
	echo "Account creation failed."
	exit 1
fi

# Set the password. (30)
echo ${PASWRD} | passwd -e ${UNAME}

# Check to see if the passwd command succeeded. (30)
if [["${?}" -ne 0]]
then 
	echo "Password could not be set."
	exit 1
fi

# Force password change on first login. (30)
#
#
#
#
#
#
#



# Display the username, password, and the host where the user was created. (30)
echo
echo "username:"
echo ${UNAME}
echo
echo "password:"
echo ${PASWRD}
echo
echo "host:"
echo "${HOSTNAME}"

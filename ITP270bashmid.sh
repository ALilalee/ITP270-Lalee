#!/bin/bash


# - That creates 2 users (Use a for loop to repeat the add user process twice ) - 20 points

# - Takes 2 inputs (Username and password) - 20 points

# - Validate the password so it is at least 8 characters long (use a while loop and If-else condition) - 30 points

# - Print the new user's username and password in the terminal - 10 points

# - Upload the script in to your Github repository - 10 points

# - Paste the Github link of the script in answer box. - 10 points

for i in 0{1..2}
do
    read -p "Username: " username 
    read -p "Password: " password
    if ["${password}" >= 8]
    echo "username"
    echo "password"
    

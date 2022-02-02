#!/usr/bin/python3

print("Welcome to the ITP270 Spring 2022 course!")

user_choice = input("Do you want to proceed with the Program[Y/n]?")

if user_choice == "Y":
	user_name = input("Enter your user name: ")
	user_course = input("Enter the name of the course: ")
	print("Thanks " + user_name + " for taking the course " + user_course + ".")
else: 
	print("Have a good day!")
 


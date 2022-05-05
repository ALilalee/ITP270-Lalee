import os

def authorize():
    print('Username: Ali')
    pword = input('Password: ')
    while pword != 'cement':
        print('incorrect password')
        pword = input('Password: ')
    else: return True
        
def granted(input):
    if input == True:
        f = open("target.txt", "r")
        print(f.read())
    else: print("oof")
    

granted(authorize())

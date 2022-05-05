import pandas as pd
import hashlib
from hashlib import md5



# take hash of test  ---done
# make algorithm to hash items in dic then compare to password hash ---done
# input hash , compare hash, output word ---done
#  launch test.py, enter password 
phash = input("Enter hash: ")
target = input("Enter dictionary file: ")

md5_hash = hashlib.md5()
b = phash.encode('utf-8')

def dictionary_attack(dictionary_word, target_hash):
    pass_bytes = dictionary_word.encode('utf-8')
    pass_hash = md5(pass_bytes)
    digest = pass_hash.hexdigest()
    if digest == target_hash:
        return True

def dica(ohash):
     with open(target, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            if dictionary_attack(stripped_line, phash) == True:
                print(stripped_line + ' is the password!')
                return stripped_line
                break

dica(b)
# exec(open(target).read())
















# def dica(ohash):
#      with open("dic.txt", "r") as a_file:
#         for line in a_file:
#             stripped_line = line.strip()
#             md5_hash.update(stripped_line.encode('utf-8'))
#             if md5_hash.hexdigest() == phash:
#                 print(stripped_line +' is the password!')
#                 break
#             # print(stripped_line +"  "+ md5_hash.hexdigest() +"    |"+ str(stripped_line.encode('utf-8')) +"|")



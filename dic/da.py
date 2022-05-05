import os
from keyboard import press

os.system('vim test.txt')

def open():
	os.system('vim test.txt')	
	press('t')
	press('e')
	press('s')
	press('t')
	press('enter')
open()



# Create a function called middle_element that has one parameter named lst. 
# If there are an odd number of elements in lst, the function should return the middle element. 
# If there are an even number of elements, the function should return the average of the middle two elements.
# Hint:
# Remember to use modulus % to determine if a number is divisible by 2. 
# Check if your function is working properly or not pasting below line in your code at the end:


def middle_element(lst):
     o1 = int(len(lst)/2)
     o2 = int(o1 - 1)
     if len(lst)%2 != 0:
         return lst[len(lst)/2]
     else:
            return (lst[o1] + lst[o2])/2

print(middle_element([5, 2, -10, -4, 4, 5])) #This should print -7.0
# **After completing the code, only share the Github link for your python code file. 


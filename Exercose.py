


import os
os.system('clear')

''' 
 Assign a different name to function and call it through the new name
Below is the function displayStudent(name, age). 
Assign a new name showStudent(name, age) to it and call through the new name
'''


def recursive(num):
    total = 0
    count = 0
    while count <= num:
        total = total + count
        count = count + 1
    return total

result = recursive(4)
print(result)
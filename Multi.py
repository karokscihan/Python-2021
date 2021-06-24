
import os
os.system('clear')

def shownumbers(limit):
    total = 0
    for each in range(0, limit + 1):        
        if each % 3 == 0 or each % 5 == 0:
            print("New number to add is " + str(each)+ "\n")
            total = total + each
    return total
        
    
        
print("\n Grand total is:" + str(shownumbers(20)))

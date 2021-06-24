
import os
os.system('clear')

def shownumbers(limit):
   for each in range(0, limit + 1):
       if each % 2 == 0:
           print(str(each) + " EVEN")
       else:
           print(str(each) + " ODD")

shownumbers(20)
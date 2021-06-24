### https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt ###

import os
os.system('clear')


def fact(num):
    total = 1
    for each in range(1, num+1):
        total = total * each
    return total
print(fact(8))


# Function for Speed Check

def shownumbers(limit):
    count = limit
    while count <= 0:
        if count % 2 == 0:
            print(str(count) + "EVEN")
            count =- 1
        else:
            print(str(count) + "ODD")

shownumbers(20)
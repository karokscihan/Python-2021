
# Function for Speed Check



def limitcheck(speed):
    demerit = 0
    while demerit < 12:
        speed = int(input("Enter your speed: "))
        if speed < 70:
            print("OK")
        else:    
            demerit = int(((speed - 75)/5) + 1)
            print("Demerit point: " + str(demerit))
        if demerit > 12:
            print("License suspended")

limitcheck(0)    

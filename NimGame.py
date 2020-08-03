
def nimGame(n): #no. of stones

    #base case 4
    if n % 4 == 0:
        return False
    else:
        return True



Number = input("enter the number of stones = ")
print (nimGame(Number))

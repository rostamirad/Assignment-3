x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))

divisorx = []
divisory = []

while True: 
    if x == y:
        print("BMM is: ", x)
        break

    elif x == 1 or y == 1:
        if x == 1:
            print("BMM is: ", x)
        else:
            print("BMM is: ", y)
            break
            
    elif x == 0 or y == 0:
        print("you cant choose 0") 
        break

    else:
        for ix in range (1, x+1):
            if x % ix == 0:
                divisorx.append(ix)
        for iy in range (1, y+1):
            if y % iy == 0:
                divisory.append(iy)
            if iy in divisorx:
                BMM = iy
    print("divisors of x are: ", divisorx," and divisors of y are: ", divisory)
    print("BMM is: ", BMM)
    break



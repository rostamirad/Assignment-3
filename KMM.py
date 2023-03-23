x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))

counterx = countery = 1

while True: 
    if x == y:
        print("KMM is: ", x)
        break
    elif x == 1 or y == 1:
        if x == 1:
            print("KMM is: ", y)
            break
        else:
            print("KMM is: ", x)
            break
    elif x == 0 or y == 0:
        print("KMM is:", 0) 
        break
    else:
        while True:
            multx = counterx * x
            multy = countery * y
            if multx == multy:
                print("KMM of your choosen number is: ", multx)
                break
            elif multx > multy:
                countery += 1
            else:
                counterx += 1
    break
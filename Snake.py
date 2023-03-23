n = int(input("plese enter your snake's length: "))

counter = 0

while counter < n:
    print("*", end ="")
    counter = counter + 1
    if counter < n:
        print("#", end = "")
        counter = counter + 1
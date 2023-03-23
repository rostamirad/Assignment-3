
n = int(input("please enter the length of the array you want:"))

Array= []

for i in range(n):
    x = int(input("please enter your number: _You can enter only n number_"))
    if x not in Array:
        Array.append(x)

        if len(Array) > 1: 
            if Array[i] > Array[i-1]:
                print("✅ correct!")
            else:  
                print("❌ The members of your array are not entered from smallest to largest")
                print("Try again!")
                break
    print(Array)
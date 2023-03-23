import random

n = int(input("plese enter the length of the array you want: "))

Array = []

for i in range(0,n):
    x = random.randint(0,100)
    if not x in Array:
        Array.append(x)
print(Array)    
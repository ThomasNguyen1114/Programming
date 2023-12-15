from random import *
oneCounter = 0
twoCounter = 0
threeCounter = 0
fourCounter = 0
fiveCounter = 0

print("Output: ")

for x in range (1000):
    from random import randint
    randomNumber = randrange(1,6)
    if randomNumber == 1:
        oneCounter += 1
    elif randomNumber == 2:
        twoCounter += 1
    elif randomNumber == 3:
        threeCounter += 1
    elif randomNumber == 4:
        fourCounter += 1
    else:
        fiveCounter += 1

    print(randomNumber, end="   ")
    if (x + 1) % 20 == 0:
        print("")

print(" ")
print("Totals: ")
print(" ")
print("        1 -", oneCounter)
print("        2 -", twoCounter)
print("        3 -", threeCounter)
print("        4 -", fourCounter)
print("        5 -", fiveCounter)
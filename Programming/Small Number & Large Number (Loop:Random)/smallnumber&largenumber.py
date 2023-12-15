from random import *
smallNumberTotal = 0
smallNumberCount = 0
largeNumberTotal = 0
largeNumberCount = 0
for x in range (100):
    from random import randint
    randomNumber = randrange(1,7)
    if randomNumber <= 3:
        smallNumberTotal += randomNumber
        smallNumberCount += 1
    else:
        largeNumberTotal += randomNumber
        largeNumberCount += 1

    print(randomNumber, end=" ")
    if (x + 1) % 10 == 0:
        print("")

print("")
print("Small Number Total: ", smallNumberTotal, sep="")
print("Small Number Count: ", smallNumberCount, sep="")
print("Large Number Total: ", largeNumberTotal, sep="")
print("Large Number Count: ", largeNumberCount, sep="")
average = 0
for x in range (3):
    testScore = testScore = float(input("Enter Test Score: "))
    while testScore < 0 or testScore > 100:
        print("Test Score Must Be Between 0 and 100! ")
        testScore = float(input("Enter Test Score: "))
    average += testScore/3
print("Average: ", round(average))
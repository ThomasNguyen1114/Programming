weight = int(input("Enter Weight (lbs): "))
height = float(input("Enter Height (in): "))
bodyMassMutiplier = 703
BMI = weight*(bodyMassMutiplier)/(height * height)
if BMI < 18.4:
    print("You Are Underweight! ")
elif BMI >= 18.4 and BMI <= 26:
    print("Your Weight Is Optimal! ")
else:
    print("You Are Overweight! ")
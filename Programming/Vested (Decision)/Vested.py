yearsWorked = int(input("Years Worked: "))
if yearsWorked >= 5:
    yearlySalary = float(input("Yearly Salary: "))
    if yearlySalary >= 50000:
        print("You Are Vested Since You Have Worked At Least 5 Years & Have A Salary Of 50,000 Or More ")
    elif yearlySalary < 50000:
        statusLevel = int(input("Status Level: "))
        if statusLevel >= 2:
            print("You Are Vested Since You Have Worked At Least 5 Years & Have A Status Level Of 2 Or Higher")
        elif statusLevel < 2:
            print("You Are Not Vested Since Your Yearly Salary Is Less Than 50,000 & Your Status Is Less Than 2 ")
else:
    print("You Are Not Vested Since You Have Not Worked At Least 5 Years ")

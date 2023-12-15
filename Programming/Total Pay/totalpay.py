regularHours = int(input("Enter Regular Hours: "))
overtimeHours = int(input("Enter Overtime Hours: "))
payRate = float(input("Enter Pay Rate: "))
regularPay = regularHours * payRate
overtimePay = overtimeHours * (payRate * 1.5)
print("Regular Pay: $" + format(regularPay, '.2f'))
print("Overtime Pay: $" + format(overtimePay, '.2f'))
totalPay = regularPay + overtimePay
print("Total Pay: $" + format(totalPay, '.2f'))
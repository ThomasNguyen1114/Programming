regularHours = int(input("Enter Regular Hours: "))
overtimeHours = int(input("Enter Overtime Hours: "))
payRate = float(input("Enter Pay Rate: "))
grossPay = (regularHours * payRate) + (overtimeHours * (payRate * 1.5))
print("Gross Pay: $", format(grossPay, '.2f'), sep="")
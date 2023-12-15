totalSales = float(input("Enter Total Sales: "))
if totalSales >= 10000:
    percentage = .07
elif totalSales >= 5000 and totalSales < 10000:
    percentage = .05
elif totalSales >= 1000 and totalSales < 5000:
    percentage = .03
elif totalSales >= 0 and totalSales < 1000:
    percentage = .02
commission = totalSales * percentage
print("Commission = $", format(commission, '.2f'), sep="")
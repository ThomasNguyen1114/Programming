milesToAddress = int(input("Miles To Address: "))
weight = int(input("Weight (Enter in lbs): "))
if milesToAddress <= 10:
    standardCharge = 4.95
    droneDiscount = 5
    if weight <= 3:
        weightCharge = 2
    elif weight <= 5:
        weightCharge = 5
    else:
        weightCharge = 10
        droneDiscount = 0
    totalShippingCharge = (standardCharge + weightCharge) - droneDiscount
elif milesToAddress <= 20:
    standardCharge = 7.95
    droneDiscount = 5
    if weight <= 3:
        weightCharge = 2
    elif weight <= 5:
        weightCharge = 5
    else:
        weightCharge = 10
        droneDiscount = 0
    totalShippingCharge = (standardCharge + weightCharge) - droneDiscount
else:
    standardCharge = 7.95
    droneDiscount = 0
    if weight <= 3:
        weightCharge = 2
    elif weight <= 5:
        weightCharge = 5
    else:
        weightCharge = 10
        droneDiscount = 0
    totalShippingCharge = (standardCharge + weightCharge) - droneDiscount

print(standardCharge)
print(weightCharge)
print(droneDiscount)
print(format(totalShippingCharge, '.2f'))

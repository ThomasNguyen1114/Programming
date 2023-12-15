dollarAmount = int(input("Enter Dollar Amount: "))
remainder = (dollarAmount)%20
twentyDollarBill = (dollarAmount)/20
print("20: " , int(twentyDollarBill))
dollarAmount = remainder
remainder = (dollarAmount)%10
tenDollarBill = (dollarAmount)/10
print("10: " , int(tenDollarBill))
dollarAmount = remainder
remainder = (dollarAmount)%5
fiveDollarBill = (dollarAmount)/5
print("5: " , int(fiveDollarBill))
dollarAmount = remainder
remainder = (dollarAmount)%1
oneDollarBill = (dollarAmount)/1
print("1: " , int(oneDollarBill))
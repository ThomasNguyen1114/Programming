total = 0
number = int(input("Enter Number (Must Be Between 0 and 50): "))
if number < 0 or number > 50:
    print("Invalid Entry (Number Must Be Between 0 and 50)")
    number = int(input("Enter Number (Enter 9999 To End!): "))
while number != 9999:
    total += number
    number = int(input("Enter Number (Enter 9999 To End!): "))
    if number == 9999:
        print("Total: ", int(total))
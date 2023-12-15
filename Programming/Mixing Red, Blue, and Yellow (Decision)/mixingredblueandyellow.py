firstColor = input("Enter First Color (Red, Blue, or Yellow): ")
if firstColor == "Red":
    secondColor = input("Enter Second Color: ")
    if firstColor == secondColor:
        print("Error: The two colors you entered are the same")
    elif secondColor == "Yellow":
        print(" Red & Yellow = Orange ")
    elif secondColor == "Blue":
        print("Red & Blue = Purple ")
    else:
        print("Error: The second color you entered is invalid! ")
elif firstColor == "Blue":
    secondColor = input("Enter Second Color: ")
    if firstColor == secondColor:
        print("Error: The two colors you entered are the same! ")
    elif secondColor == "Yellow":
        print(" Blue & Yellow = Green ")
    elif secondColor == "Red":
        print("Blue & Red = Purple ")
    else:
        print("Error: The second color you entered is invalid! ")
elif firstColor == "Yellow":
    secondColor = input("Enter Second Color: (Red, Blue, or Yellow): ")
    if firstColor == secondColor:
        print("Error: The two colors you entered are the same! ")
    elif secondColor == "Yellow":
        print("Yellow & Red = Orange ")
    elif secondColor == "Blue":
        print("Yellow & Blue = Green ")
    else:
        print("Error: The second color you entered is invalid! ")
else:
    print("Error: The first color you entered is invalid! ")

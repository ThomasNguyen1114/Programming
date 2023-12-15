name = input("Enter Name: ")
payment = float(input("Enter Payment: "))
yearOfPayment= int(input("Enter Payment Year (Enter As 4 Digits!): "))
monthOfPayment = int(input("Enter Month Of Payment (Enter Number!): "))
while monthOfPayment < 1 or monthOfPayment > 12:
    print("Invalid Entry (Enter Number That Corresponds With The Month!) ")
    monthOfPayment = int(input("Enter Month Of Payment (Enter Number!): "))
    studentBalance = 300
    studentNewBalance = 300 - payment
    dueDate = (-6 + monthOfPayment) + 12 * (-2021 + yearOfPayment)
    if studentNewBalance <= 0:
        print("Congratulations ",name , " you are free" \
            " from our continuous collection harassments.", sep="")
    else:
        if dueDate <= 2:
            print(name, " made a payment of ", format(payment, '.2f'),\
                ". Your payment was within the agreed time frame but"\
                " you stil owe ", format(studentNewBalance, '.2f'),\
                " so keep up the payments and we will"\
                " not come and pull you out of class. ", sep="")
        elif dueDate <= 4:
            print(name, " made a payment of ", format(payment, '.2f'),\
                ". Your payment was ", dueDate, " months late and you"\
                " still owe ", format(studentNewBalance, '.2f'), " so"\
                " we will come take your car or any other item of"\
                " value. ", sep="")
        elif dueDate <= 6:
            print(name, " made a payment of ", format(payment, '.2f'),\
                ". Your payment was ", dueDate, " months late and you"\
                " still owe ", format(studentNewBalance, '.2f'), " so"\
                " we will be taking away your debit card until you"\
                " pay your bill. ", sep="")
        else: 
            print(name, " made a payment of ", format(payment, '.2f'),\
                ". Your payment was ", dueDate, " months late and you"\
                " still owe ", format(studentNewBalance, '.2f'), " so"\
                " be ready for the warrant and court date. ", sep="")
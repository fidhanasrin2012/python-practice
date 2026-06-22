balance= 10000
pin = int (input("Enter the PIN:"))
if pin== 1234:
    print("Login Successfull")
    print("Your balance is:", balance)
    amount=int(input("Enter the amount to withdraw:"))
    if amount  <= balance:
        balance = balance - amount
        print("Withdrawal Successfull")
        print("Your remaining balance:" , balance)
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")
    
    
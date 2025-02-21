
while True:
    try:
        
        print("Welcome to mybank \n---------------------------------------------------")
        print("1:create acc\n2:credit amount\n3:debit amount\n4:show balance\n5:exit")
        choice=int(input("enter choice number:"))
        if choice==1:
            name = input("enter your name=")
            amount = float(input("enter amount to open acc="))
            if amount>=1000:
                print(f"{name}, congrats your acc created successfully and acc number is 5555")
                accnumber = 5555
            else:
                print("amount must be greater than or equal to 1000")
                
        elif choice==2:
            pass
        elif choice==3:
            pass
        
        elif choice==4:
            newaccnum = int(input("enter your a/c number to verify="))
            if newaccnum == accnumber:
                print("your current balance=", amount)
            else:
                print("invalid acc number. try again!")
                
                
        elif choice==5:
            print("thank you for using our services :)")
            break
        else:
            print("invalid choice no")
    except:
        print("invalid input")
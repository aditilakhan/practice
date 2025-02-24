#wap to monthnumber from user and show monthname and no of days

try:
    monthnum = int(input("enter month num:"))
    if monthnum == 1:
        print(f"{monthnum} is jan month and has 31 days")
    elif monthnum == 2:
        year = int(input("Enter year:"))
        if year % 4 == 0:
            print(f"{year} is leap and {monthnum} is feb month and has 29 days")
        else:
            print(f"{year} is not leap and {monthnum} is feb month and has 28 days")
    elif monthnum == 3:
        print(f"{monthnum} is march month and has 31 days")
    elif monthnum == 4:
        print(f"{monthnum} is april month and has 30 days")   
    elif monthnum == 5:
        print(f"{monthnum} is may month and has 31 days")           
    elif monthnum == 6:
        print(f"{monthnum} is june month and has 30 days")
    elif monthnum == 7:
        print(f"{monthnum} is july month and has 31 days")
    elif monthnum == 8:
        print(f"{monthnum} is aug month and has 31 days")
    elif monthnum == 9:
        print(f"{monthnum} is sept month and has 30 days")
    elif monthnum == 10:
        print(f"{monthnum} is oct month and has 31 days")
    elif monthnum == 11:
        print(f"{monthnum} is nov month and has 30 days")
    elif monthnum == 12:
        print(f"{monthnum} is dec month and has 31 days")
    else:
        print("Please enter month no between 1 to 12")
except:
    print("invalid input")
    
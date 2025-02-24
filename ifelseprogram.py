#wap to check entered no is +ve or -ve

n = int(input("enter no: "))
if n > 0:
    print(f"{n} is +ve no")
else:
    print(f"{n} is -ve no")
    
#wap to check entered no is even odd

n = int(input("enter no: "))
if n % 2 == 0:
    print(f"{n} is even no")
else:
    print(f"{n} is odd no")
    
    
#wap to show greatest no among any two no

a = int(input("enter a:"))
b = int(input("enter b:"))          
if a > b:
    print(f"{a} is greatest no")
else:
    print(f"{b} is greatest no")
    
#wap to check entered year is leap year or not

year = int(input("enter year:"))
if year % 4 == 0:   
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
    
#wap to show profit and loss as per entered costprice and selling price
cp = float(input("enter cost price:"))
sp = float(input("enter selling price:"))
if sp == cp:
    print("no profit no loss")
else:
   if sp > cp:
    profit = sp - cp
    print(f"congrats! you earned profit of {profit}Rs/-")
   else:
    loss = cp -sp
    print(f"Sorry! you had loss of {loss}Rs/-")
    


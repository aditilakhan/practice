#wap to check enter number is prime or not

n = int(input("enter n="))
flag = False
if n==1:
    print(f"{n} is not a prime number")
    
else:
    for i in range(2,n):
        if n%i == 0:
            flag = True
            break
        
        if flag == True:
            print(f"{n} is not a prime number")
        else:
            print(f"{n} is a prime number")


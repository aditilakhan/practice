n = int(input("enter any number:"))
sum = 1
for i in range(2, n):
    if n%1 == 0:
        sum = sum + i
    
    if sum == n:
        print(f"{n} no is perfect number")
    else:
        print(f"{n} no is not a perfect number")
    
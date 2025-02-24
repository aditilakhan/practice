for i in range(3):
    print("*")
    
    
for i in range(3):
    print("*", end="")
    
for i in range(3):
    print(3 * "*")
    
#star pattern
row = int(input("enter row count="))
column = int(input("enter column count="))
for i in range(row):
    for j in range(column):
        print("*", end=" ")
    print()

row = int(input("enter row count="))
column = int(input("enter column count="))
for i in range(row):
    for j in range(column):
        print(j, end=" ")
    print()

row = int(input("enter row count="))
column = int(input("enter column count="))
for i in range(row):
    for j in range(1,column+1) :
        print(j, end=" ")
    print()
    
row = int(input("enter row count="))
column = int(input("enter column count="))
for i in range(1,row+1):
    for j in range(1,column+1) :
        print(f"[{i},{j}]", end="\t")
    print()
    
row = int(input("enter row count="))
column = int(input("enter column count="))
for i in range(1,row+1):
    for j in range(1,column+1) :
        print(f"{i*j}", end="")
    print()


    
#wap to print numbers in  row-wise as per multiplication
# row = int(input("enter row count="))
# column = int(input("enter column count="))
# count = 1
# for i in range(3):
#     for j in range(5):
#         print(count,end="") 
#         count += 1
#     print()
    
#wap to print numbers in column-wise as multiplication
# row = int(input("enter row count="))
# column = int(input("enter column count="))
# count = 1
# for i in range(1,row+1):
#     count = i
#     for j in range(column):
#         print(count,end=" ")
#         count = count + 5
#     print()
    
#right decrement  
# row = int(input("enter row="))
# for i in range(row):
#     for j in range(i):
#         print(" ", end=" ")
        
#     for k in range(row - i):
#         print("😴", end=" ")
#     print()


# #hill incremental triangle
# row = int(input("enter row="))
# for i in range(1,row + 1):
#     for j in range(row - i):
#         print(" ", end=" ")
        
#     for k in range(i):
#         print("*  ", end=" ")
#     print()
    
#hill decrement triangle
# row = int(input("enter row="))
# for i in range(row):
#     for j in range(i):
#         print(" ", end="")
     
#     for k in range(row - i):
#         print("*", end=" ")
#     print()
        
    
#number incremental

# row = int(input("enter row="))
# count = 1
# for i in range(1,row + 1):
#     for j in range(row - i):
#         print(" ", end="")
        
#     for k in range(i):
#         print(count, end=" ")
#         count = count + 1            
#     print()
    
#number decremental

# row = int(input("enter row="))
# count = 1
# for i in range(row):
#     for j in range(i):
#         print(" ", end="")
        
#     for k in range(row - i):
#         print(count, end=" ")
#         count += 1          
#     print()
    
    
#diamond
row = int(input("enter row="))
for i in range(1,row):
    for j in range(row - i):
        print(" ", end="")
        
    for k in range(i):
        print("*", end=" ")         
    print()
    
for i in range(row):
    for j in range(i):
        print(" ", end="")
        
    for k in range(row - i):
        print("*", end=" ")         
    print()
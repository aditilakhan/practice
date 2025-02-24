# #wap to check no is zero, positive or negative
# try:
#     n = int(input("Enter a number: "))
#     if n == 0:
#        print(f"{n} is zero")
#     else:
#          if n > 0:
#              print(f"{n} is positive no")
#          else:
#              print(f"{n} is negative no")
# except:
#        print("invalid input")
# #wap to show square and cube of any integer no follow below cases
# # note: 
# # test case-1 if empty inputs or string then show invalid inputs
# # test case-2 if number is zero or less than also it will show no cant be zero

# try:
#     n = int(input("Enter any integer no: "))
#     if n!=0:
#         sq = n**2
#         cube = n**3
#         print(f"square{sq} and cube {cube}")
#     else:
#         print("no can't be zero")
# except:
#     print("invalid input!")    
    
# wap to find smallest no among any positive three integer no
try:
    a = int(input("enter a="))
    b = int(input("enter b="))
    c = int(input("enter c="))
    if a < b and a < c:
        print(f"{a} is smallest no")
    else:
        if b < c:
           print(f"{b} is smallest no")
        else:
            print(f"{c} is smallest no")
except:
      print("invalid inputs")  
        
        
    
    
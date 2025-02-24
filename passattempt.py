# wap to validate your pass by entering 'admin' as password
# but give only 3 attempt for wrong password and when it is correct it stop with 
# congrats msg

password = "admin"
i = 1
while i <= 3:
    password_input = input("Enter your password: ")
    if password_input == password:
        print("congrats msg")
    break
else:
    print("pass incorrect")
i += 1
   
    
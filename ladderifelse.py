# wap to show welcome message for user accn to entered username

username = input("enter username:")
if username == "admin":
    print("welcome admin! you have all permission")
elif username == "testuser":
    print("welcome testuser! you have all r/w permission")
elif username == "guest":
    print("welcome guest! you have read only permission")
elif username == "":
    print("Please enter correct username")
else:
    print("invalid username")

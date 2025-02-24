# mylist = ["red", "green", "blue", "white"]
# for i in mylist:
#     print(i)

# i = 0
# while i < len(mylist):
#     print(mylist[i], i)
#     i += 1
    
#wap to find enter elements and replace as per asked new element
mylist = ["red", "blue", "green", "white"]

print(mylist)
flag = False
element = input("enter element to find and replace=")
result = []
for i in mylist:
    if i == element:
        print(f"{element} found")
        newelement = input("enter new element to replace=")
        result = result + list(newelement)
        result.append(newelement)
        flag = True
    else:
        result = result + list(i)
        result.append(i)
if flag:
    print(f"New list={result}")
else:
    print(f"{element} not found")
    
    

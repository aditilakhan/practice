# #traverse

# colors = ("red", "green", "purple", "blue", "black")
# # for i in colors:
# #     print(i)
    

# # for i in reversed(colors):
# #     print(i,end=",")
    

# for i in colors[::-1]:
#     print(i)
    
# #while loop
# i = 0
# while i < len(colors):
#     print(colors[i])
#     i = i + 1
    
# #wap to show count of elements entered by user from below tuple
# colors  = ("red", "green", "purple", "blue", "black")
# print(colors)
# element = input("enter element=")
# count = 0
# flag = False
# for i in colors:
#     if i == element:
#         count = count + 1
#         flag = True
    
# if flag:
#     print(f"Count of {element}={count}")
# else:
#     print(f"Entered {element} not present")


# show index of entered elements

colors  = ("red", "green", "purple", "blue", "black")
print(colors)
element = input("enter element=")
indexnum = []
flag = False
for i in range(len(colors)):
    if colors[i] == element:
        indexnum.append(i)
        flag = True
    
if flag:
    print(f"index of {element}={indexnum}")
else:
    print(f"Entered {element} not present")

#wap to show find and replace for entered char as per entered string
str = input("enter string:").lower()
char = input("enter char to find and replace:").lower()
flag = False
result = ""
for i in str:
    if i == char:
        print("character found.")
        x = input("enter replace char=").lower()
        flag = True
        result = result + x
    else:
        result = result + i
        
if flag:
    print(f"replace string={result}")
else:
    print(f"entered'{char} not found")

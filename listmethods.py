#adding elements append(), insert()

# colors = []
# print(colors)

# colors.append("red")
# print(colors)

# colors.append("green")
# print(colors)

# colors.append(["blue","white"])
# print(colors)

# colors.append(("blue","white"))
# print(colors)

# colors.append({"blue", "white"})
# print(colors)

# x = ["pink" , "orange"]
# colors.append(x)
# print(colors)

# # for i in colors:
# #     print(i)

# colors.append("black", 0) #error index not allowed


#wap to create mylist add numbers as per count entered by user
mylist =[]
count = int(input("Enter the count of numbers: "))

for i in range(count):
    n = int(input(f"enter {i+1} number="))
    mylist.append(n)
    
print(mylist)


#length of mylist by using loop
# count = 0
# for i in mylist:
#     count += 1
#     print(f"length of mylist = {count}")

#homework q
#count of element 
#find replace element
#sum of all elements
#show even and odd number in seperate list

#sorting - asc desc by using loop 

# for i in range(len(mylist)):
#     for j in range(i+1):
#         if mylist[i] > mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# print("Descending order=", mylist)  

# for i in range(len(mylist)):
#     for j in range(i+1):
#         if mylist[i] < mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# print("Ascending order=", mylist)
# #
# find 2nd highest element using loop
# for i in range(len(mylist)):
#     for j in range(i+1):
#         if mylist[i] > mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
            
# print("Descending order=", mylist)
# print("2nd highest", mylist[1])

# show newmylist without duplication any element
newmylist = []
for i in mylist:
    if i not in newmylist:
        newmylist.append(i)
print(newmylist)
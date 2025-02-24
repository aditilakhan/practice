# # #adding elements insert()

# # mylist = []
# # mylist.insert(5, "red")
# # print(mylist)  

# # print(mylist[0])
# # mylist.insert(3, "green")
# # print(mylist)

# # mylist.insert(1, "blue")
# # print(mylist)

# # #insert at last
# # mylist.insert(-1,"white")
# # print(mylist)
# # mylist.insert(len(mylist), "grey")
# # print(mylist)

# # mylist.insert(len(mylist) // 2, "orange") #insert at middle 
# # print(mylist)

# # # wap to add elements into mylist as per count entered by user

# # mylist =[]
# # count = int(input("Enter the count of numbers: "))
# # for i in range(count):
# #     n = int(input(f"enter {i+1} number="))
# #     mylist.insert(i,n)
# # print(mylist)

#update
colors = []
print(colors)

# colors[0] = "red"
print(colors)

colors = ["red", "green", "blue"]
print(colors)
colors[0] = "black"
print(colors)
colors[3] = "pink"
print(colors)

# #wap display vowels and consonent and counts from entered name by user
# # name = input("enter name=")
# # v = []
# # c = [] 

# # for i in name:
# #     if i == "aeiouAEIOU":
# #        v.append(i)
# #     else:
# #         c.append(i)
# # print(f"vowels={v} and total vowels={len(v)}")
# # print(f"consonants={c} and total consonants={len(c)}")


# #remove

# # books = ["py", "cpp", "html", "js", "py", "java"]
# # print(books)
# # books.pop()
# # print(books)

# # books.pop(3)
# # print(books)

# # books.pop(31)
# # print(books)

# # mylist = []
# # mylist.pop()

# # books = ["py", "cpp", "html", "js", "py", "java"]
# # print(books)
# # books.remove("cpp")
# # print(books)
# # books.remove("py")
# # print(books)
# # books.remove("py")
# # print(books)
# # # books.remove("py")
# # # print(books)

# # del books[0]
# # print(books)

# # del books
# # print(books)

# # del books[10]
# # print(books)

# # del books
# # print(books)

# # books = ["py", "cpp", "html", "js", "py", "java"]
# # print(books)

# # #reverse(), sort(), extend(), copy(), clear(), count()

# # newbooks = books.reverse()
# # print(newbooks)       #none        

# # books.reverse()
# # print(books)



# #sort()
# # books.sort()
# # print(books)
# # # x = ["hello", True, 4.5, 44]
# # # x.sort() 
# # # print(x)
# z = [23,4,2.5,11]
# # z.sort(reverse=True)
# # print(z)

# #extend()
# m = [1,2,3]
# print(m)
# m.extend(z)
# print(m)

# student=[]
# for i in range(3):
#     name = input("enter name=")
#     grade = input("enter grade=")
#     # student.append([name,grade])
#     student.extend([name, grade])
# print(student)

books = ["py", "cpp", "html", "js", "py", "java"]
print(books, id(books))

#copy()
b = books
print(b, id(b))
bk = books.copy()
print(bk, id(bk))

n = [1,1,1]
print(n)
n = books.copy()
print(n, id(n))

#clear()
n.clear()
print(n)

#count()
print(books.count("py"))
print(books.count(""))
print(books.count("rust"))

#index()
print(books.index("py"))
print(books.index("py",3,5))


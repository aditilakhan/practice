# # #set methods

# # mylist = set()
# # print(mylist)

# # mylist.add("red")
# # print(mylist)
# # mylist.add("red")

# # print(mylist)
# # mylist.add(("green", "blue"))
# # print(mylist)

# x = ("black", 45, "white")
# # mylist.add(x)
# # print(mylist)

# # #wap to take numbers from user and show sum of them as per count entered by user
# # count = int(input("enter count for numbers:"))
# # sum = 0
# # myset = set()
# # for i in range(count):
# #     n = int(input(f"enter {i+1} number"))
# #     myset.add(n)
# #     sum += n
# # print(myset)
# # print(f"sum of above numbers:", sum)

# # #copy()

# # x = {1,2,3}
# # y = {3,4,5,6}
# # print(x)
# # print(y)
# # x = y.copy()
# # print(x)

# # #update()
# z = {"red", "blue"}
# z.update(x)
# print(z)

# z.update((45,56))
# print(z)

# z.update({8, 100, 200})
# print(z)

# z.update([99, 88])
# print(z)

# #wap to take student data as name, marks, grade into set for 3 students
# # students = set()
# # for i in range(3):
# #     name = input(f"enter {i+1} student name=")
# #     marks = int(input(f"enter {i+1} student total marks="))
# #     grade = input(f"enter {i+1} student grade=")
# #     # students.update((name, marks, grade))
# #     students.add((name, marks, grade))
# # print(students)
    
# #removing elements
# z.remove(88)
# print(z)
# z.remove(188)
# print(z)

# z.discard(188)
# print(z)
# z.discard(100)
# print(z)

# z.pop()
# print(z) 

# z.clear()
# print(z)

# del z
# print(z)

# a = {1,2,3,4}
# b = {1,2,3}
# c = {11,12}

# print(a.issuperset(b))
# print(a>b)
# print(b.issubset(a))
# print(a>b)

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))  

#frozen set()
s = {"red","green"}
print(s)
s.add("black")
print(s, type(s))
s = frozenset(s)
print(s, type(s))
s.add("white")
print(s)
# #set

# #empty set
# s = {}
# print(s, type(s))

# s = set()
# print(s, type(s))

# s1 = {34}
# print(s1, type(s1))

# s2 = {"Hello", True, 56j, None, 67.78}
# print(s2, type(s2))

# s3 = {"red", 45,45, "red", 78, 45}
# print(s3, type(s3))

# s4 = {(1,2), (1,2), (1,2), 56, 45}
# print(s4, type(s4))

# # s4 = {(1,2), [1,2], {1,2}, 56, 45}
# # print(s4, type(s4))

# #no index no slicing
# colors = {"red", "green", "blue", "white"}
# # print(colors[0])
# # print(colors[1:])
# newcolors = list(colors)
# print(newcolors)
# newcolors.append("black")
# colors = set(newcolors)
# print(colors)


#operators
# a = {1,2,3}
# b = {3,4, "java"}
# c = {5,6,7,9}
# d = {1,2,3,8,9,10}
# print(a)
# print(b)
# print(c)
# print(d)

# print(a+b)
# print(a+c)
# print(a*b)
# print(a*5)
# print(a-b)
# print(b-a)
# print(a-d)
# print(a == b)
# print(a is b)
# print(a in d)
# print(2 in d)

# print(a > d)
# print(d > a)

#set operation methods

x = {1,2,3,4}
y = {2,4,5,6}

print("x=", x)
print("y=", y)

print("union of x to y=", x.union(y))
print("union of y to x=", y.union(x))
print("union of x and y=", x|y)

print("intersection of x and y=", x.intersection(y))
print("intersection of y and x=", y.intersection(x))
print("intersection of x and y=", x&y)

print("difference of x to y=", x.difference(y))
print("difference of y to x=", y.difference(x))
print("difference of x to y=", x-y)

print("symmetric_difference of x to y=", x.symmetric_difference(y))
print("symmetric_difference of y to x=", y.symmetric_difference(x))
print("symmetric_difference of x to y=", x-y)
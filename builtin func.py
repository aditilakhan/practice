# #built in function

# a = 3
# print(a)
# print(bin(a))
# print(oct(a))
# print(hex(a))

# #help()
# # print(help("def"))
# print(help("ahggud"))

# print(pow(2,3))
# print(2**3)
# print(round(34.54262))
# print(round(58.254))
# print(round(58.254, 2))
# print(divmod(5,3))
# print(5//3, 5%3)

# #zip()

# names = ["rohan", "komal", "pooja"]
# grades = ["A", "O", "A+"]
# percentage = [89.45, 56.45]
# print(list(zip(names, grades)))
# print(list(zip(names, grades, percentage)))


# for i in names, grades:
#     # print(i)
#     print(i[0], end=" ")
    
# print(tuple(zip(names, grades, percentage)))
# print(set(zip(names, percentage)))
# print(dict(zip(names, grades)))

#unzip
# students = [("rohan","A"), ("komal", "O"), ("pooja", "A+")]
# print(students)
# print(list(zip(*students)))
# print(set(zip(*students)))
# print(tuple(zip(*students)))
# # print(dict(zip(*students)))

# students = [["rohan", "A"], ["komal", "O"]]
# print(dict(zip(*students)))

#slice()

colors = ["red", "green", "blue", "white", "grey", "orange"]
ans = slice(2,5)
print(colors[ans])
print(colors[2:5])
msg = "Welcome to python"
print(msg[ans])

#enumerate()
colors = ["red", "green", "white", "grey", "orange"]
print(colors)
print(list(enumerate(colors)))
print(list(enumerate(colors,3)))
print(tuple(enumerate(colors)))
print(set(enumerate(colors)))
print(dict(enumerate(colors)))

print(dict.fromkeys(colors, 0))
print(set(enumerate(colors)))

#iter
colors = ["red", "green", "pink"]
print(colors)
newdata = iter(colors)
print(newdata)
first = next(newdata)
print(first)
second = next(newdata)
print(second)
third = next(newdata)
print(third)
# fourth = next(newdata)
# print(fourth)
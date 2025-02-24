#tuple

# t = tuple()
# print(t, type(t))

# t1 = ()
# print(t1, type(t1))

# t2 = (34)
# print(t2, type(t2)) --- #int

# t3 = 45, "welcome",455
# print(t3, type(t3)) 

# tuple1 = (3, "python", True, 6j, None, 56.78, [1,23], ("red, 45"), {1:4})
# print(tuple1, type(tuple1))   --- #tuple

# tuple2 = tuple("hello")
# print(tuple2, type(tuple2))  #('h', 'e', 'l', 'l', 'o')

# t3 = tuple(34)  #TypeError: 'int' object is not iterable
# print(t3, type(t3))  

# t3 = tuple([34,35,36])
# print(t3, type(t3))

# accessing elements via index on tuple

# colors = ("red", "black", "blue", "white", "yellow")
# print(colors, len(colors))
# print(colors[0])
# print(colors[-1])
# print(colors[len(colors) // 2])

# # slicing 
# print(colors[::-1])
# print(colors[3:5])
# print(colors[-3:5])
# print(colors[3:-5])


#operators
# numbers = (3, 45, 2, 5)
# x = ("hello", 56, 4.53)
# print(numbers, id(numbers))
# print(x)

# print(numbers + x)
# print(numbers * 5)
# numbers += 100
# print(numbers)

# print(numbers + x)
# print(numbers * 5)
# numbers += x
# print(numbers, id(numbers))
# print(numbers > x)

# a = (1,2)
b = (4,5,1,3)
# print(a < b)
# print(a == b)
# z = (1,2)
# print(a == z)
# print(a is z)
# print(1 in z)

# functions
# print(b)
# print(len(b))
# print(min(b))
# print(max(b))
# print(sorted(b))
# print(sum(b))
# print("".join(reversed(str(b))))

m = ("hi", 45, 56.67, True, 76, "yo")
print(m)
print(m.count(45))
print(m.count(""))
print(m.count("yo"))
print(m.count(456))
# print(m.count(45,"hi"))

print(m.index(45))
print(m.index(""))
print(m.index("459"))
# dictionary: collection of different data types but written as key value pair enclosed within {} 
# no. index but keyindexing follows, unorder but follows key order and no slicing and no repeated keys but value can be repeated


d = {}
print(d, type(d))
d = dict()
print(d, type(d))

d = {1:1}
print(d, type(d))

d = {1:1, 1:6}
print(d, type(d))

d = {"name": "komal", "rollnum": 34, "grade": "A"}
print(d, type(d))

d = {"name": "roshan"}
print(d, type(d))

#without methods add, update, remove
books = {}
print(books)
books["title"] = "python"
print(books)

books["title"] = "java"
print(books)

books["author"] = "jj"
print(books)

books["price"] = 800
print(books)

books["publisher", "qty"] = "techmax", 7
print(books)

books = dict(isbn=1111, dop="12-09-2009")
print("new=",books)

print("--------------")

#delete/remove via keyname
del books["isbn"]
print(books)

# del books["title"]
# print(books)

#update 
colors = {1: "red", 2: "blue", 3:"green", 4:"white"}
print(colors)

colors[2] = "pink"
print(colors)

colors[9] = "orange"
print(colors)

colors[8] = "red"
print(colors)

#reading elements
print(colors[1])


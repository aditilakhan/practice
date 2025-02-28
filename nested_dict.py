# books = [
#     {"isbn": 1111, "title": "python", "author":"pp"}, 
#     {"isbn": 2222, "title": "java", "author":"js"},
# ]

# for i in books:
#     print(i)
    
# #find details of isbn 2222
# print(books[1])
# print("isbn=", books[1]["isbn"])
# print("title=", books[1].get("title"))
# print("author=", books[1].get("author"))

books = {
    1111: {"title": "python", "author": "pp"}, 
    2222: {"title": "js", "author": "js"},
}

print(books, type(books))
for i in books.items():
    print(i)
    
#find details of isbn 2222
print("isbn=2222")
print("title=", books[2222]["title"])
print("author=", books[2222].get("author"))
# #methods

# students = {}
# print(students)

# students.update({"name": "raj"})
# print(students)

# students.update({"name": "komal"})
# print(students)

# students.update({"grade":"A", "per":89.67, "degree":"bca"})
# print(students)

# students.update({"subjects":["py", "js", "cpp"]})
# print(students)

# students.update({"email":("k@gmail", "k1@gmail.com")})
# print(students)

# # students.update({(["city", "pincode"]:("mumbai"), 400098)})
# # print(students)

# students.update({("city", "pincode"):("mumbai", 400098)})
# print(students)

# #remove elements
# students.pop("per")
# print(students)

# # students.pop("percentage")
# # print(students)

# students.popitem()
# print(students)

# students.popitem()
# print(students)

# students.clear()
# print(students)

#values(), get(), keys(), items()
numbers = {1:100, 2:200, 3:300, 4:400}
print(numbers)
print(numbers.values())
print(numbers.keys())
print(numbers.items())
print(numbers.get(1))
print(numbers.get(100)) 
print(list(numbers.items()))
print(tuple(numbers.items()))
print(set(numbers.items()))


#copy()
numbers1 = numbers.copy()
print(numbers1) 

#fromkeys()
n = [1,2,3]
print(n)
n = dict.fromkeys(n,"itv")
print(n)

#set default()
movies = {"name": "abcd", "stars": 5}
print(movies)
x = movies.setdefault("duration", "2.10mins")
print(movies)
print(x)
movies.update({"duration":"3hrs"})
print(movies)
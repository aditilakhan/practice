#operators : it is aka symbol which perform sum operations in operands which can be one or many
# unary : only one operand +, -, !, 
# binary : more than operands >,<, in. +=

print(5 > 6 and 5 < 6) 
print(5 > 6 and 5 < 6 and 6 > 5)
print(5 > 6 or 5 < 6)
print(5 > 6 or 5 < 6 or 6 > 5)
print(not 5 > 6)

name = "python"
print("p" in name)
# n = 2323345878
# print (2 in n) # type error
# n = 2323345878
# print (2 in str(n))  # error
n = 232345878
print("2" in str(n))    # true
mylist = ["py", 23, "js"]
print(23 in mylist)
#built-in function for string

print(len("welcome"))
print(len("welcome python"))
# print(len(1243)) #error

print(len(str(1243))) #or while loop
print(ord("A"))       #65 ascii code
# print(ord("anu"))   # error
print(chr(97)) 
print(min("python"))
print(max("python"))
print(max("python34567Bca hi"))
# print(max(123456767)) #error
print(sorted("python"))
print(sorted("python")[::-1])
print(sorted("python"[::1]))
print(sorted("hello")[:1:])

#operations on string 
x = "python"
y = "java"
print(x+y)
# print(x-y)
# print(232 + "welcome") 
# print(x*y)
# print(x/y)
print(x * 5)
print(x * True)
print(x * False) #empty

print("10" * 10)
a = "10"
print(int(a) * 10)
print(x < y)
print(x > y) #checks first char ascii code
print(x == y)
print(x is y)
print(y is x)
print("p" in y)
print("p" in x)
msg = "hi hello"
print(" " in msg)
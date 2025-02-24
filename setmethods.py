#set methods

mylist = set()
print(mylist)

mylist.add("red")
print(mylist)
mylist.add("red")

print(mylist)
mylist.add(("green", "blue"))
print(mylist)

x = ("black", 45, "white")
mylist.add(x)
print(mylist)

#wap to take numbers from user and show sum of them as per count entered by user
count = int(input("enter count for numbers:"))
sum = 0
myset = set()
for i in range(count):
    n = int(input(f"enter {i+1} number"))
    myset.add(n)
    sum += n
print(myset)
print(f"sum of above numbers:", sum)

#copy()

x = {1,2,3}
y = {3,4,5,6}
print(x)
print(y)
x = y.copy()
print(x)

#update()
z = {"red", "blue"}
z.update(x)
print(z)

z.update((45,56))
print(z)
s ="welcome to python"
print(s,len(s))
print("")
print(s.count("o"))
print(s.count(""))
print(s.count("ome",5,14))
print(s.count("o",3,14))
print(s.count("om",5,14))
print(s.count("v",5,14))
print(s.find("o"))
print(s.find("o",5,14))
print(s.find("o"))
print(s.find(""))
print(s.find("x"))
print(s.index("o"))
print(s.index(""))
print(s.index("o",5,16))
# print(s.index("x"))

# print(s["o"])

print(s.join("x"))
print("x".join(s))
print(" ".join(s))
print(sorted(s))
print("".join(sorted(s)))

print("-------")
print(s.split())
x = "python"
print(x.split())


y = "red,green,blue,white,black"
print(y.split())
print(y.split(","))
print(y.split(",",3))

print(s.splitlines())
s1 = "hi\nhow are you?"
print(s1)
print(s1.split())
print(s1.splitlines())

print(s.zfill(13))
print(s.zfill(23))

print(s.strip())
x = "      mango          grapes        apple    "
print(x)
print(x.strip())

a = "welcome to python"
b = "abc1234"
c = ""
d = "py@123/"
e = "678"

print(a.upper())
print(b.lower())
print(a.lower())
print(a.isupper())
print(b.islower())
print(e.islower())

print(a)
print(a.isalnum())
print(a.isnumeric())
print(a.isalpha())
print(a.isdigit())

print(b)
print(b.isalnum())
print(b.isnumeric())
print(b.isalpha())
print(b.isdigit())


print(c)
print(c.isalnum())
print(c.isnumeric())
print(c.isalpha())
print(c.isdigit())

print(d)
print(d.isalnum())
print(d.isnumeric())
print(d.isalpha())
print(d.isdigit())

print(e)
print(e.isalnum())
print(e.isnumeric())
print(e.isalpha())
print(e.isdigit())


for i in "python":
    print(i)
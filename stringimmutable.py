s = "welcome"
print(s,id(s))
print(s[0])

# s[0] = "r"
print(s)

news = "r" + s[1:]
print(news)

print(s.replace("w","r"))
s = s.replace("w","r")
print(s, id(s))
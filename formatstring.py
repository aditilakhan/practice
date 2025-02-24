name = "abc"
place = "mumbai"
print("my name is", name,"and i am from",place)

ans = "my name is", name, "and i am from", place
print(ans)

ans1 = f"my name is {name} and i am from {place}"
print(ans1)


# %s is string format specifier
ans3 = "my name is %s and i am from %s" % (name, place)
print(ans3)

ans4 = "my name is %s and i am from %s and %s" % (name, place, "delhi")
print(ans4)

#format()
ans5 = "my name is {0} and i am from {1}".format(name, place)
print(ans5)

per = 98.78965423
ans6 = f"my name is {name} and i am from {place} and i got {per:0.2f} percentage"
print(ans6)


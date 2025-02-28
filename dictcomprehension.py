# #dict comprehension without block and generate result in sequence

# ans = {}
# for i in range(1,6):
#     ans.update({i:i *i})
# print(ans)

# ans = [i for i in range(1,6)]
# print(ans)

# ans = {i for i in range(1,6)}
# print(ans)

# ans = {i:i * i for i in range(1,6)}
# print(ans)

# #wap to print 5number table
# result = {i:i*5 for i in range(1,11)}
# print(result)

products = {"milk": 50, "coffee": 80, "bread": 28}

# convert all item price inr to us and show updated product data use dict comprehension
# with loop
ans = {}
for k, v in products.items():
    ans.update({k:v/87})

print(ans)

# comprehension 
print({k:v/87 for k,v in products.items()})

#show only those items whose price is greater than 30
print({k:v for k,v in products.items() if v>30})

#show only coffee details
print({k:v for k,v in products.items() if k=="coffee"})
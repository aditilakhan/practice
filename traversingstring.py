# traversing 

# s = "python"
# for i in s:
#     print(i)
    
# show along with index number

# s = "python is too easy"
# for i in s:
#     print(i, s.index(i)) 

# msg = "welcome to python world"
# for i in range(len(msg)):
#     print(msg[i],i)
    
# i = 0
# while i < len(msg):
#     print(msg[i], i)
#     i += 1
    
#wap to traverse every 2nd character of any string entered by user
# str = input("enter string:")
# for i in range(1,len(str),2):
#     print(str[i])
    
# wap to print no of occurances of enter 
# char from ay string by using loop

# str = input("enter string:")
# char = input("enter char:")
# count = 0
# flag = False
# for i in str:
#     if i == char:
#         count = count + 1
#         flag = True
#     else: 
#         flag = False
# if flag:
#     print("char is present in string", count)
# else:
#     print("char is not present in string")

# wap to find entered character index position by is using loop
# str = input("enter string:")
# char = input("enter char:")
# indexnum = []

# flag = False

# for i in range(len(str)):
#     if char == str[i]:
#         indexnum.append(i)
#         flag = True
        
# if flag:
#     print(f"index of {char}={indexnum}")
# else:
#     print(f"entered '{char}' not present in '{str}'") 
        
        
#wap to show reverse of string by without loop
# str = input("enter string=")
# print(str)
# print(str[::-1])

# wap to show reverse of string by using loop
# for i in str[::-1]:
#     print(i, end="")

# wap to show reverse string 
# for i in range(len(str)-1,-1, -1):
#     print(str[i], end="")
    
# s = ""
# for i in str:
#     s = i + s
#     print(s)


# str = input("enter string:")
# print(str)

#wap to show vowels and count from entered string

# str = input("enter string:")
# acount, ecount, icount, ocount, ucount = 0,0,0,0,0

# for i in str.lower():
#     if i == "a":
#         acount += 1
#     elif i == "e":
#         ecount += 1
#     elif i == "i":
#         icount += 1
#     elif i == "o":
#         ocount += 1
#     elif i == "u":
#         ucount += 1
        
# print(f"vowels count a={acount}\ne={ecount}\ni={icount}\no={ocount}\nu={ucount}")

#wap to show vowels and consonant seperately with total count from entered string
# str = input("enter string:").lower()
# v,c = 0,0 
# vowels = ""
# consonants = ""

# for i in str:
#     if i in "aeiou":
#         v += 1 
#         vowels = vowels + i
#     else:
#         c += 1
#         consonants = consonants + i 
# print(f"vowels present in{str}={vowels} and count={v}")
# print(f"consonants present in{str}={consonants} and count = {c}")

#wap to show find and replace for entered char as per entered string
str = input("enter string:").lower()
char = input("enter char to find and replace:").lower()
flag = False
result = ""
for i in str:
    if i == char:
        print("character found.")
        x = input("enter replace char=").lower()
        flag = True
        result = result + x
    else:
        result = result + i
        
if flag:
    print(f"replace string={result}")
else:
    print(f"entered'{char} not found")


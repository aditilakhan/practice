# #comprehension is replacement of traditional loop & also generate result in sequence

# # for i in range(1,6):
# #     print(i, end=" ")
    
# [print(i) for i in range(1,6)]

# print([i for i in range(1,6)])

# ans = [i for i in range(1,6)]
# print(ans) 

# even = [i for i in range(2,11,2)]
# print("even number=", even)

# odd = [i for i in range(1,11) if i%2!= 0]
# print("odd number=", odd)  

# #or 
# e = []
# o = []
# ans = [e.append(i) if i%2==0 else o.append(i) for i in range(1,11)]
# print("even numbers=", e)
# print("odd numbers=", o)

#WAP TO SHOW ENTERED STRING BY REMOVING VOWELS USE LIST COMPREHENSION
# s = input("Enter a string:")
# news= ""
# for i in s:
#     if i not in "aeiouAEIOU":
#         news = news + i
# print(news)

# ans = [i for i in s if i not in "aeiouAEIOU"]
# print("".join(ans))

#wap to print true for positive numbers and false for negative numbers
#but take 10 numbers from user and use list comprehension

numbers = [int(input(f"enter {i} number:")) for i in range(1,11)]
print(numbers)
ans = [True if i>0 else False for i in numbers]
print(ans)
count = 1
for i in range(1,7):
    for j in range(1,6):
        if i % 2 == 0:
             if j % 2 != 0:
                  print("*", end=" ")
             else:
                  print(count, end=" ")
                  count += 1
        else:
             if j % 2 != 0:
                  print(count, end=" ")
                  count += 1
             else:
                 print("*", end=" ")
    print()                 

        
        
        
    


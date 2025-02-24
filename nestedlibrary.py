bookdb = [["isbn", "title", "author", "price", "qty"]]
count = int(input("enter count for books="))
for i in range(count):
    isbn = int(input(f"enter {i+1} book isbn="))
    title = input(f"enter {isbn} book title=")
    author = input(f"enter {isbn} book author=")
    price = float(input(f"enter {isbn} book price="))
    qty = int(input(f"enter {isbn} book qty="))
    
    data = [isbn, title, author, price, qty]
    bookdb.append(data)
    
print("------available books-------")

for i in bookdb:
    for j in i:
        print(j, end=" ")
    print()
    
    
#do with while true 

print("---update books detail---")
chkisbn = int(input("enter book isbn number update record="))
flag = False
for i in bookdb:
    if i[0] == chkisbn:
        flag = True
        print("ISBN=", i[0])
        print("Title=", i[1])
        print("Author=", i[2])        
        print("Price=",i[3])
        print("Qty=", i[4])
        print("--update option as per asked below---")
        choice = int(input("enter 1:title\n2:author\n3:price\n4:qty\n5:cancel"))
        if choice == 1:
            newtitle = input(f"enter new title for isbn{i[0]}=")
            print("title updated successfully!")
            
        elif choice==2:
            newauthor = input(f"enter new author for isbn{i[0]}=")
            i[2] = newauthor
            print("author updated successfully")
            
        elif choice==3:
            newprice = float(input(f"enter new price for isbn {i[0]}"))
            i[3] = newprice
            print("price updated successfully!")
            
        elif choice==4:
            newqty = float(input(f"enter new qty for isbn {i[0]}"))
            i[4] = newqty
            print("qty updated successfully!")
            
            
        elif choice==5:
            print("operation cancelled!")
            break
        
        else:
            print("invalid choice number")
            
if flag == False:
    print("Book not found or check ISBN number again")
    
print("------available books-------")

for i in bookdb:
    for j in i:
        print(j, end="")
    print()
    
print("---delete books detail---")
chkisbn = int(input("enter book isbn number delete record="))
flag = False
for i in bookdb:
    if i[0] == chkisbn:
        flag = True
        print("ISBN=", i[0])
        print("Title=", i[1])
        print("Author=", i[2])        
        print("Price=",i[3])
        print("Qty=", i[4])    
        choice = input("are you want to delete record type yes/no=")
        if choice.lower() == "yes" or choice.lower() == "y":
            bookdb.remove(i)
            print("record deleted successfully")
        elif choice.lower() == "no" or choice.lower() == "n":
            print("record not deleted...")
        else:
            print("incorrect choice. try again")
            
if flag == False:
    print("Book not found or check ISBN number again")
    
print("------available books-------")

for i in bookdb:
    for j in i:
        print(j, end="")
    print()
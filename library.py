
booksdb = []
while True:
    try:
        
        print("------------Welcome to my library---------------")
        print("1:add books\n2:show books\n3:update books\n4:remove books\n5:search books\n6:exit")
        choice=int(input("enter choice number:"))
        if choice==1:
           count = int(input("enter count for book="))
           for i in range(count):
               title = input(f"enter {i+1} book title=").lower()
               booksdb.append(title)
           print("books added successfully!")   
            
        elif choice==2:
           if len(booksdb) > 0:
               print("avaliable books=", booksdb)
           else:
               print("books not available")
               
        elif choice==3:
            if len(booksdb) > 0:
                chktitle = input("enter book to update title=").lower()
                if chktitle in booksdb:
                    print(f"{chktitle} book found")
                    newtitle = input(f" enter new title for {chktitle}=").lower()
                    for i in range(len(booksdb)):
                        if chktitle==booksdb[i]:
                            booksdb[i]=newtitle
                        print("book title updated successfully!")
                else:
                    print(f"{chktitle} is not available or enter correct title")
            else:
                print("books db is empty so first add books then after do update.")
        
        elif choice==4:
            if len(booksdb) > 0:
                chktitle = input("enter book to delete title=").lower()
                if chktitle in booksdb:
                    print(f"{chktitle} book found")
                    # for i in range(len(booksdb)):
                    #     if chktitle==booksdb[i]:
                    #         del booksdb[i]
                            
                    for i in booksdb:
                        if chktitle == i:
                            booksdb.remove(i)
                        print("book title deleted successfully!")
                else:
                    print(f"{chktitle} is not available or enter correct title")
            else:
                print("books db is empty so first add books then after do update.")
                
        elif choice==5:
           pass
        
        elif choice==6:
             print("thank you for using our services")
             break
        else:
            print("inavlid choice number")
    except:
        print("invalid input")
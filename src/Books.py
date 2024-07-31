"Function Related to Books in Library Management System"
import mysql.connector as sql
import report



def AddBook():
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()
        
    #Adding New Book

        bookid=input("Enter the book id:")
        name=input("Enter the book name:")
        author=input("Enter the author:")
        genre=input("Enter the genre:")
        language=input("Enter the language:")
        
        query="insert into books values('{}','{}','{}','{}','{}','YES')".format(bookid,name,genre,author,language)
        cursor.execute(query)
        db.commit()
    except:
        print("Error")




def RemoveBook():
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()

        #Removing Book
        
        print("Please make sure the book is returned before deleting it !!")
        bookid=input("Enter the book id:")
        cursor.execute("select * from books where book_id='"+str(bookid)+"'")
        if cursor.fetchone()==[]:
            print("\nNo book by that name!!")

        cursor.execute("delete from library_transaction where book_id='"+bookid+"'")
        query="delete from books where book_id='{}'".format(bookid)
        cursor.execute(query)
        db.commit()
    except:
        print("Error:Unable to connect to database")
    
 

def SearchBook():
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
    
    #Searching for a book
        cursor=db.cursor()
        print("\nSearch by:\n\n\t1.Book Name\n\t2.Author\n\t3.Genre\n\t4.Book Id\n\t5.All Books")

        c=int(input("\n\tEnter your choice:"))
        
        if c==1:
            name=input("Enter the book name you want to search:")
            query="select * from books where book_name like '%{}%'".format(name)
        elif c==2:
            name=input("Enter the author name you want to search:")
            query="select * from books where author like '%{}%'".format(name)
        elif c==3:
            name=input("Enter the genre you want to search:")
            query="select * from books where genre like '%{}%'".format(name)
        elif c==4:
            bid=input("Enter the book id you want to search:")
            query="select * from books where book_id like '%{}%'".format(bid)
        elif c==5:
            query="select * from books"
        else:
            print("\nInvalid choice!!\n")
            return  None
        cursor.execute(query)
        data=cursor.fetchall()
        if data==[]:
            print("\nNo results !!")
        else:
            print("\n\n"+"-"*80)
            print("BookId|Name\t\t   |Genre     |Author\t\t   |Language  |Available|")
            print("-"*80)
            for i in data:
                print(i[0]+" "*(6-len(i[0])),i[1]+" "*(20-len(i[1])),i[2]+" "*(10-len(i[2])),i[3]+" "*(20-len(i[3])),i[4]+" "*(10-len(i[4])),i[5]+" "*(9-len(i[5]))+"|",sep="|")
            print("-"*80)
    except ValueError:
            print("Enter a integer value !!")
    except:
        print("Error:Unable to connect to database")
    




def UpdateBook():
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()

        #Updating Books
        
        book_id=input("Enter the book id:")
        cursor.execute("select * from books where book_id='"+book_id+"'")
        
        if cursor.fetchone()==None:
            print("Book doesnt exist")
            return None
            
        name=input("Enter the updated book name:")
        author=input("Enter the updated author:")
        genre=input("Enter the genre:")
        language=input("Enter the language:")
        
        query="update books set book_name='{}',genre='{}',author='{}',language='{}' where book_id='{}'".format(name,genre,author,language,book_id)
        cursor.execute(query)
        db.commit()
    except:
        print("Something went wrong ??")
    


def ReturnBook(uid):
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()
        
        print("\nPlease make sure to enter the correct book id")
        book_id=input("Enter the book_id")
        cursor.execute("select * from books where book_id='"+str(book_id)+"'")
        data=cursor.fetchone()
        if data ==None:
            print("No Book By That ID")
            return None
        elif data[0]=='YES':
            print("Unable to return book (Book not Lent) !!")
        else:
            date_of_return=str(input("Enter date of returning(yyyy-mm-dd):"))
            cursor.execute("update library_transaction set date_of_return='"+str(date_of_return)+"' where user_id='"+str(uid)+"' and date_of_return is null")
            cursor.execute("update books set available='YES' where book_id='"+book_id+"'")
            db.commit()
    except ValueError:
        print("\nError:Data inputed is incorrect !!")
    except:
        print("Something went wrong")


def LendBook(uid):    
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()
        print("Please only lend a book after returning previous books")

        book_id=str(input("Enter the book id:"))
        cursor.execute("select available from books where book_id='"+str(book_id)+"'")
        data=cursor.fetchone()
        if data==None:
            print("No such Books")
            return None
        elif data[0]=='NO':
            print("This Book Hasnt Been Returned Yet")
        else:
            date=str(input("Enter date of lending(yyyy-mm-dd):"))
            query="insert into library_transaction values('{}','{}','{}',NULL)".format(uid,book_id,date)
            cursor.execute(query)
            cursor.execute("update books set available='NO' where book_id='"+str(book_id)+"'")
            db.commit()
    except ValueError:
        print("Error:Data entered is incorrect !!")
    except:
            print("Error:Something went wrong??")

SearchBook()

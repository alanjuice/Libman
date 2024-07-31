

#a simple line
def line():
   print("~"*100)


   
#MEMBER
def member(data):
    print("\n\n\t\tWelcome!!!",data[0][1])
    while True:
        line()
        print("\n\n\t1.Lend a Book\n\t2.Return a Book\n\t3.Search a book\n\t4.Logout")
        try:
            c=int(input("\nEnter the choice:"))
        except ValueError:
            print("\nEnter a integer value !!\n")
            continue
        if c==1:
            Books.LendBook(data[0][0])
        elif c==2:
            Books.ReturnBook(data[0][0])
        elif c==3:
            Books.SearchBook()
        elif c==4:
            print("Goodbye !!")
            break
        else:
                print("Invalid Choice!!\n")
#ADMIN                
def admin():
    while True:
        line()
        print("\t\tADMIN\n\n\t1.Members\n\t2.Books\n\t3.Reports\n\t4.Go Back\n")
        try:
            ch=int(input("Enter the choice:"))
        except ValueError:
            print("\nError:Enter a integer value !")
            continue
        if ch==1:
            while True:
                line()
                print("\n\n\t\tMEMBERS\n\n\t1.Add a member\n\t2.Delete a Member\n\t3.Update a Member\n\t4.Go Back\n")
                try:
                    ch=int(input("Enter the choice:"))
                except ValueError:
                    print("\nError:Enter an integer value !!")
                    continue
                if ch==1:
                    Members.AddMember()
                elif ch==2:
                    Members.RemoveMember()
                elif ch==3:
                    Members.UpdateMember()
                elif ch==4:
                    break
                else:
                    print("\nError:Invalid Choice!")
        elif ch==2:
            while True:
                line()
                print("\n\n\t\tBOOKS\n\n\t1.Add a new book\n\t2.Delete a book\n\t3.Update a book\n\t4.Search a book\n\t5.Go Back\n")
                try:
                    ch=int(input("Enter the choice:"))
                except ValueError:
                    print("\nError:Enter an integer value !!")
                    continue
                if ch==1:
                    Books.AddBook()
                elif ch==2:
                    Books.RemoveBook()
                elif ch==3:
                    Books.UpdateBook()
                elif ch==4:
                    Books.SearchBook()
                elif ch==5:
                    break
                else:
                    print("Invalid Choice!")
        elif ch==3:
            while True:
                line()
                print("*****Data added on this session wont be reflected in the file*******")
                print("\n\n\t\tGenerate a csv report on:")
                print("\n\t1.Full Library Transcations\n\t2.Members Information\n\t3.Books Report\n\t4.Go Back")
                try:
                  ch=int(input("\nEnter your choice:"))
                except ValueError:
                    print("\nError:Enter an integer Value !!")
                    continue
                if ch==1:
                    cursor.execute("select * from library_transaction")
                    data=cursor.fetchall()
                    report.reportcsv(["user_id","book_id","date_of_lend","date_of_return"],data,"library_transaction")
                elif ch==2:
                    cursor.execute("select * from members")
                    data=cursor.fetchall()
                    report.reportcsv(["user_id","name","phone_no","address","dob","password"],data,"members")
                elif ch==3:
                    cursor.execute("select * from books")
                    data=cursor.fetchall()
                    report.reportcsv(["book_id","name","genre","author","language","available"],data,"books")
                elif ch==4:
                    break
                else:
                    print("\nError:Invalid Choice!!")
        elif ch==4:
            break
        else:
            print("\nError:Invalid Choice!!")

#VERFYING PASSWORD AND USER_ID
def Login():
    line()
    uid=input("\nEnter your id:")
    psw=input("Enter the password:")
    data = Members.PassCheck(uid,psw)
    if data==[]:
        print("\nError:Wrong Password or User Id\n")
    else:
        if uid.upper()=="ADMIN":
            admin()
        else:
            member(data)

#Mysql connection
import mysql.connector as sql
db=sql.connect(passwd="root",user="root",host="localhost")
db.autocommit=True
cursor=db.cursor()

#USING DATABASE
cursor.execute("create database if not exists library")
cursor.execute("use library")

#Importing Modules
import Members
import Books
import sys
import report


#CREATING REQUIRED TABLES
cursor.execute("create table if not exists members(user_id char(6) primary key,name char(20),phone_no char(10),address char(30),dob date,password char(10))")
cursor.execute("create table if not exists books(book_id char(6) primary key,book_name char(20),genre char(10),author char(20),language char(10),available char(3))")
cursor.execute("create table if not exists library_transaction(user_id char(10),foreign key(user_id) references members(user_id),book_id char(6),foreign key(book_id) references books(book_id),date_of_lend date,date_of_return date)") 

#Checking for Admin Account
cursor.execute("select * from members where user_id='ADMIN'")
if cursor.fetchone()==None:
    line()
    Members.AddMember("Admin")



#Main Menu
while True:
    line()
    print("\n\n\t\tLIBRARY MANAGMENT SYSTEM\n")
    print("\n\t1.Login\n\t2.Register\n\t3.Exit\n")
    try:
        ch=int(input("\nEnter your choice:"))
    except ValueError:
      print("\nEnter a integer value !!\n")
      continue
    cursor.execute("select * from members")
    print(cursor.fetchall())
    if ch==1:
        Login()
    elif ch==2:
        Members.AddMember()
    elif ch==3:
        print("\n\tBye !!")
        sys.exit()
    else:
        print("Invalid choice !!")
    

import mysql.connector as sql



def AddMember(typ=None):
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()
    #Adding a Member
        if typ=="Admin":
            passw=input("Enter a password for ADMIN:")
            cursor.execute("insert into members values('ADMIN',NULL,NULL,NULL,NULL,'"+str(passw)+"')")
        else:
            uid=input("Enter the user id:")
            name=input("Enter your name(limit:20):")
            no=int(input("Enter your mobile no:"))
            address=input("Enter your address(limit:30):")
            dob=input("Enter date of birth(YYYY-MM-DD):")
            password=input("Enter a password(limit:10):")
            
            query="insert into members values('{}','{}',{},'{}','{}','{}')".format(uid,name,no,address,dob,password)
            cursor.execute(query)
        db.commit()
    except:
        print("\nError:Data have been entered incorrectly")


def RemoveMember():
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()
        
        #Removing a Member
        
        print("\nPlease make sure that books have been returned before deleting the account")
        uid=input("Enter the user id:")
        cursor.execute("select * from members where user_id='"+uid+"'")
        if cursor.fetchone()==None:
            print("\nAccount doesn't exist")
            return None
        if uid.upper()=="ADMIN":
            print("\nError:ADMIN cant Be REMOVED\n")
            return None
        cursor.execute("delete from library_transaction where user_id='"+str(uid)+"'")
        query="delete from members where user_id='{}'".format(uid)
        cursor.execute(query)
        db.commit()
        print("\nAccount Removed Successfully !\n")
        
    except:
        print("Something went Wrong!")
        return None



#Used to update details of members(except user_id)
def UpdateMember():
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()
        
    #Updating a Existing Member
        uid=input("Enter the user id")
        cursor.execute("select * from members where user_id='"+uid+"'")
        if cursor.fetchone()==None:
            print("\nAccount doesn't exist:")
            return None
        name=input("Enter your name(updated):")
        no=int(input("Enter your updated mobile no:"))
        address=input("Enter your updated address:")
        dob=input("Enter correct date of birth(YYYY-MM-DD)")
        password=input("Enter a new password:")
    
        query="update members set name='{}',phone_no={},address='{}',dob='{}',password='{}' where user_id='{}'".format(name,no,address,dob,password,uid)
        cursor.execute(query)
        db.commit()
        print("Updation successfull !!")
    except ValueError:
        print("\nError:Data inputed is incorrect !!")
    except:
        print("\nSomething Went Wrong !")


#Used for Verifying User_Id and Password
def PassCheck(uid,psw):
    try:
        db=sql.connect(passwd="root",user="root",host="localhost",database="library")
        cursor=db.cursor()
    
        query="select * from members where user_id='{}' and password='{}'".format(uid,psw)
        cursor.execute(query)
        data=cursor.fetchall()
        return data
    except:
        print("Error:Couldn't connect to database") 
    



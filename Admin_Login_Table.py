import mysql.connector as mc
from mysql.connector import errorcode

def login():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        while True:
            user=input("Enter your username : ")
            cur.execute('select username from admin_login;')
            Data=cur.fetchall()
            user_exist=False
            for i in Data:
                if user==i[0]:
                    user_exist=True
                    break
            if user_exist == True:
                while True:
                    password=int(input("Enter your password : "))
                    cur.execute("select password from admin_login where username='{}';".format(user))
                    Data=cur.fetchone()
                    if password==Data[0]:
                        print("\nLogin Successful")
                        print("Permission to use our software granted\n")
                        cur.execute("select type from admin_login where username='{}';".format(user))
                        global Type
                        Type=cur.fetchone()[0]
                        break
                    else:
                        print("Inavalid Password. Please enter again\n")
                break
            else:
                print("User does not exist. Please try again\n")
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
    
def new_user():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        global Type
        if Type=='user':
            print("You don't have authorisation to add new user\n")
        else:
            print("This is the portal to add a new user\n")
            while True:
                user=input('Enter new username : ')
                cur.execute('select username from admin_login;')
                Data=cur.fetchall()
                user_exist=False
                for i in Data:
                    if user==i[0]:
                        user_exist=True
                        break
                if user_exist == True:
                    print("Username already exists. Enter different username\n")
                else:
                    t=0
                    password=98566666 #random number
                    while len(str(password))!=6:
                        if t==1:
                            print("\nEnter only 6 digit Password\n")
                        t=1
                        password=int(input("Enter Password (only 6 digits) : "))
                    Type1=input("Enter user type (admin/user) : ")
                    Query="insert into admin_login values('{}',{},'{}')"
                    cur.execute(Query.format(user,password,Type1))
                    cur.execute("commit")
                    print("\nNew user registered successfully\n")
                    del t
                    break
        cnx.close() 
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def del_user():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        global Type
        if Type=='user':
            print("You don't have authorisation to add new user\n")
        else:
            print("This is the portal to delete user\n")
            while True:
                user=input('Enter username : ')
                cur.execute('select username from admin_login;')
                Data=cur.fetchall()
                user_exist=False
                for i in Data:
                    if user==i[0]:
                        user_exist=True
                        break
                if user_exist == True:
                    WARNING=input(("Are you sure you want to delete this user? (Y/N) : "))
                    if WARNING.upper()=='Y':
                        cur.execute("delete from admin_login where username='{}'".format(user))
                        cur.execute('commit')
                        print('User deleted successfully\n')
                    else:
                        print('User not deleted\n')
                    break
                else:
                    print("Username does not exist. Enter different username\n")
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


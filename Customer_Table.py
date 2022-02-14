import mysql.connector as mc
from mysql.connector import errorcode
import random

def New_Acc():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print('\nPlease Enter the following details to register your account\n')
        Account_No=random.randint(1000000000,9999999999)
        Name=input("Enter name : ")
        Balance=float(input("Enter the amount you would like to deposit : "))
        while True:
            Sex=input("Enter sex (M for male/F for female/O for others) : ")
            if len(Sex)==1 and Sex.upper() in 'MFO':
                break
            else:
                print('Please enter sex in required format\n')
    #process to generate customer id
        First_Name=Name.split()[0]
        Customer_Id=First_Name[:4]
        for i in range(4-len(First_Name)):
            Customer_Id=Customer_Id+'0'
        Customer_Id=Customer_Id+Sex+str(random.randint(100,999))
    #customer id generated
        DOB=input("Enter date of birth (YYYY-MM-DD) : ")
        while True:
            Phone_No=int(input("Enter mobile number : "))
            if len(str(Phone_No))==10:
                break
            else:
                print("Please enter 10 digits!!!\n")
        Email_Id=input("Enter email id : ")
        Street_Add=input("Enter street address : ")
        Locality=input("Enter locality : ")
        City=input("Enter city : ")
        State=input("Enter state : ")
        Pincode=int(input("Enter pincode : "))
        Country=input("Enter country : ")
        Nom=input("Enter nominee : ")
        Nom_rel=input("Enter nominee relation : ")
        Occupation=input("Enter occupation : ")
        Account_Type=input("Enter account type : ")
        Query="insert into customer values ({},'{}','{}',{},'{}','{}',{},'{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}')"
        cur.execute(Query.format(Account_No,Name,Customer_Id,Balance,Sex,DOB,Phone_No,
                             Email_Id,Street_Add,Locality,City,State,Pincode,Country,
                             Nom,Nom_rel,Occupation,Account_Type))
        cur.execute('Commit')
        print("\nAccount registered successfully")
        print("Your Account Number is :",Account_No)
        print("Your Customer I'd is :",Customer_Id,'\n')
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()



def Update_Acc():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print("\nThis is the portal to updatde account details")
        print('''1)Contact Details
2)Address
3)Nominee Details
4)Occupation\n''')
        while True:
            Account_No=int(input('Enter your account number : '))
            cur.execute('select Account_No from Customer;')
            Data=cur.fetchall()
            Acc_exist=False
            for i in Data:
                if Account_No==i[0]:
                    Acc_exist=True
                    break
            if Acc_exist == True:
                cur.execute('select Name from Customer where Account_No={}'.format(Account_No))
                print('Account is registered with name : ',cur.fetchone()[0])
                C=int(input("Enter your choice : "))
                if C==1:
                    while True:
                        Phone_No=int(input("Enter mobile number : "))
                        if len(str(Phone_No))==10:
                            break
                        else:
                            print("Please enter 10 digits!!!\n")
                    Email_Id=input("Enter email id : ")
                    Query="update customer \
set Phone_No={}, Email_Id='{}' \
where Account_No={}"
                    cur.execute(Query.format(Phone_No,Email_Id,Account_No))
                    cur.execute('commit')
                    print("Details Updated")
                    break
                elif C==2:
                    Street_Add=input("Enter street address : ")
                    Locality=input("Enter locality : ")
                    City=input("Enter city : ")
                    State=input("Enter state : ")
                    Pincode=int(input("Enter pincode : "))
                    Country=input("Enter country : ")
                    Query="update customer \
set Street_Address='{}', Locality='{}', City='{}', State='{}', Pincode={}, Country='{}'\
where Account_No={}"
                    cur.execute(Query.format(Street_Add,Locality,City,State,Pincode,Country,Account_No))
                    cur.execute('commit')
                    print("Details Updated")
                    break
                elif C==3:
                    Nom=input("Enter nominee : ")
                    Nom_rel=input("Enter nominee relation : ")
                    Query="update customer \
set Nominee='{}', Nominee_Relation='{}' \
where Account_No={}"
                    cur.execute(Query.format(Nom,Nom_rel,Account_No))
                    cur.execute('commit')
                    print("Details Updated")
                    break
                elif C==4:
                    Occupation=input('Enter Your Occupation : ')
                    Query="update customer \
set Occupation='{}' \
where Account_No={}"
                    cur.execute(Query.format(Occupation,Account_No))
                    cur.execute('commit')
                    print("Details Updated")
                    break
                else:
                    print('Invalid Choice\n')
            else:
                print('Account does not exist\n')
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def Check_Balance():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        while True:
            Account_No=int(input('\nEnter your account number : '))
            cur.execute('select Account_No from Customer;')
            Data=cur.fetchall()
            Acc_exist=False
            for i in Data:
                if Account_No==i[0]:
                    Acc_exist=True
                    break
            if Acc_exist == True:
                Query="select Balance from customer where Account_No={}"
                cur.execute(Query.format(Account_No))
                Balance=cur.fetchone()
                print('Your account balance is : ',Balance[0],'\n')
                break
            else:
                print('Account does not exist')
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()



def Delete_Account():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print('\nThis is the portal to delete your account\n')
        while True:
            Account_No=int(input('Enter Account Number to be deleted : '))
            cur.execute('select Account_No from Customer;')
            Data=cur.fetchall()
            Acc_exist=False
            for i in Data:
                if Account_No==i[0]:
                    Acc_exist=True
                    break
            if Acc_exist == True:
                cur.execute('select Name from Customer where Account_No={}'.format(Account_No))
                print('Account is registered with name : ',cur.fetchone()[0])
                WARNING=input(("Are you sure you want to delete this account? (Y/N) : "))
                if WARNING.upper()=='Y':
                    cur.execute('delete from customer where account_no={}'.format(Account_No))
                    cur.execute('commit')
                    print('Account deleted successfully\n')
                else:
                    print('Account not deleted\n')
                break
            else:
                print('Account does not exist\n')
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()



def Display_Acc_Details():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print('\nThis is the portal to display all account details\n')
        while True:
            Account_No=int(input('Enter your account number : '))
            cur.execute('select Account_No from Customer;')
            Data=cur.fetchall()
            Acc_exist=False
            for i in Data:
                if Account_No==i[0]:
                    Acc_exist=True
                    break
            if Acc_exist == True:
                cur.execute('select * from customer where account_no={}'.format(Account_No))
                (Account_No,Name,Customer_Id,Balance,Sex,DOB,Phone_No,Email_Id,Street_Add,Locality,City,State,Pincode,Country,Nom,Nom_rel,Occupation,Account_Type) = cur.fetchone()
                print('\nAccount number \t\t:\t\t',Account_No)
                print('Name \t\t\t:\t\t',Name)
                print('Customer id \t\t:\t\t',Customer_Id)
                print('Balance \t\t:\t\t',Balance)
                print('Sex \t\t\t:\t\t',Sex)
                print('Date Of Birth \t\t:\t\t',DOB)
                print('Phone Number \t\t:\t\t',Phone_No)
                print('Email id \t\t:\t\t',Email_Id)
                print('Street Address \t\t:\t\t',Street_Add)
                print('Locality \t\t:\t\t',Locality)
                print('City \t\t\t:\t\t',City)
                print('State \t\t\t:\t\t',State)
                print('Pincode \t\t:\t\t',Pincode)
                print('Country \t\t:\t\t',Country)
                print('Nominee Name \t\t:\t\t',Nom)
                print('Nominee relation \t:\t\t',Nom_rel)
                print('Occupation \t\t:\t\t',Occupation)
                print('Account type \t\t:\t\t',Account_Type)
                print('********\n')
                break
            else:
                print('Account does not exist\n')
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
        







        
    
                
        
    
        
    
        
        
            
            
            
    

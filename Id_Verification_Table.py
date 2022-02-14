import mysql.connector as mc
from mysql.connector import errorcode
import string
from datetime import date


def New_Kyc():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print('\nPlease Enter the following details for KYC verification\n')
        print("\nSelect Government ID of your choice")
        print('''1)Aadhar
2)Pan
3)Driving lisence
4)Passport
5)Voter ID\n''')
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
                cur.execute('select Account_No from id_verification;')
                Data=cur.fetchall()
                Kyc_exist=False
                for i in Data:
                    if Account_No==i[0]:
                        Kyc_exist=True
                        break
                if Kyc_exist==False:
                    gov_id_no='2536457689780978676547685' #random number
                    t=0
                    C=int(input("Enter your choice : "))
                    if C==1:
                        while len(gov_id_no)!=16 or not gov_id_no.isnumeric():
                            if t==1:
                                print("\nId Number does not match the gerneral format\nPlease try again\n")
                            t=1
                            gov_id_no=input("Enter Aadhar Number : ")
                        Query="insert into id_verification values({},'{}','{}','{}')"
                        cur.execute(Query.format(Account_No,'AADHAR',gov_id_no,str(date.today())))
                        cur.execute("Commit")
                        print("\nKYC completed successfully!!!\n")
                        break
                    elif C==2:
                        while len(gov_id_no)!=10 or not gov_id_no[:5].isalpha() or not gov_id_no[5:9].isnumeric() or not gov_id_no[-1] in string.ascii_letters:
                            if t==1:
                                print("\nId Number does not match the gerneral format\nPlease try again\n")
                            t=1
                            gov_id_no=input("Enter Pan Number : ")
                        Query="insert into id_verification values({},'{}','{}','{}')"
                        cur.execute(Query.format(Account_No,'PAN',gov_id_no,str(date.today())))
                        cur.execute("Commit")
                        print("\nKYC completed successfully!!!\n")
                        break
                    elif C==3:
                        while len(gov_id_no)!=15 or not gov_id_no[:2].isalpha() or not gov_id_no[2:].isnumeric():
                            if t==1:
                                print("\nId Number does not match the gerneral format\nPlease try again\n")
                            t=1
                            gov_id_no=input("Enter Driving lisence Number : ")
                        Query="insert into id_verification values({},'{}','{}','{}')"
                        cur.execute(Query.format(Account_No,'DRIVING LISENCE',gov_id_no,str(date.today())))
                        cur.execute("Commit")
                        print("\nKYC completed successfully!!!\n")
                        break
                    elif C==4:
                        while len(gov_id_no)!=8 or not gov_id_no[0] in string.ascii_letters or not gov_id_no[1:].isnumeric():
                            if t==1:
                                print("\nId Number does not match the gerneral format\nPlease try again\n")
                            t=1
                            gov_id_no=input("Enter Passport Number : ")
                        Query="insert into id_verification values({},'{}','{}','{}')"
                        cur.execute(Query.format(Account_No,'PASSPORT',gov_id_no,str(date.today())))
                        cur.execute("Commit")
                        print("\nKYC completed successfully!!!\n")
                        break
                    elif C==5:
                        while len(gov_id_no)!=10 or not gov_id_no[:3].isalpha() or not gov_id_no[3:].isnumeric():
                            if t==1:
                                print("\nId Number does not match the gerneral format\nPlease try again\n")
                            t=1
                            gov_id_no=input("Enter Passport Number : ")
                        Query="insert into id_verification values({},'{}','{}','{}')"
                        cur.execute(Query.format(Account_No,'VOTER ID',gov_id_no,str(date.today())))
                        cur.execute("Commit")
                        print("\nKYC completed successfully!!!\n")
                        break
                    else:
                        print('Invalid Choice\n')
                    del t
                else:
                    print("Account is already KYC verified\n")
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

def Kyc_status():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
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
                cur.execute('select Account_No from id_verification;')
                Data=cur.fetchall()
                Kyc_exist=False
                for i in Data:
                    if Account_No==i[0]:
                        Kyc_exist=True
                        break
                if Kyc_exist==False:
                    print("Account is not KYC verified\n")
                    break
                else:
                    print("Account is KYC verified\n")
                    Query="Select * from id_verification where account_no={}"
                    cur.execute(Query.format(Account_No))
                    Data=cur.fetchone()
                    print("Account Number \t:\t ",Data[0])
                    print("Gov. ID Name \t:\t ",Data[1])
                    print("Gov. ID Number \t:\t ",Data[2])
                    print("Date of KYC \t:\t ",Data[3])
                    print("*****************\n")
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


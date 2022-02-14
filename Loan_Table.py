import mysql.connector as mc
from mysql.connector import errorcode
import string
import random

def New_Loan():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print("\nThis is the portal for a new loan\n")
        print("Interest rate is 5% per annum\n")
        print('Please Enter the following details to apply for a loan\n')
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
                S=15
                Loan_id=''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                Loan_type=input("Enter type of loan : ")
                Loan_amt=int(input("Enter Loan Amount required : "))
                Loan_duration=int(input("Enter Loan Duraton (in years) : "))
                income_cert_no=int(input("Enter Income Certificate Number (for verification) : "))
                Loan_collateral=input("Enter Collateral against loan : ")
                rate_month=5/(100*12)
                EMI=round(Loan_amt*rate_month*((1+rate_month)**(Loan_duration*12)/((1+rate_month)**(Loan_duration*12)-1)),2)
                Query="insert into loan values ('{}',{},'{}',{},{},{},{},'{}')"
                cur.execute(Query.format(Loan_id,Account_No,Loan_type,Loan_amt,EMI,Loan_duration,income_cert_no,Loan_collateral))
                cur.execute('Commit')
                print("\nLoan registered successfully")
                print("Loan I'd is :",Loan_id,'\n')
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

def loan_details():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print("\nThis is the portal to print your loan details")
        while True:
            Account_No=int(input("\nPlease enter the account number : "))
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
                cur.execute('select Account_No from loan;')
                Data=cur.fetchall()
                Loan_exist=False
                for i in Data:
                    if Account_No==i[0]:
                        Loan_exist=True
                        break
                if Loan_exist == True:
                    Query="select * from loan where Account_No={}"
                    cur.execute(Query.format(Account_No))
                    Data=cur.fetchall()
                    K=1
                    for(Loan_id,Account_No,Loan_type,Loan_amt,EMI,Loan_duration,income_cert_no,Loan_collateral) in Data:
                        print("\nDetails of Loan number",K)
                        print("Loan Id \t\t:\t", Loan_id)
                        print("Account number \t\t:\t", Account_No)
                        print("Loan Type \t\t:\t", Loan_type)
                        print("Loan Amount \t\t:\t", Loan_amt)
                        print("EMI \t\t\t:\t", EMI)
                        print("Loan Duration (years)\t:\t", Loan_duration)
                        print("Income Cert No \t\t:\t", income_cert_no)
                        print("Loan Collateral \t:\t",Loan_collateral)
                        K+=1
                    print("\nNo more loan")
                    print("*************\n")
                else:
                    print("You haven't taken any loan\n")
                break
            else:
                print("Account does not exist\n")
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()




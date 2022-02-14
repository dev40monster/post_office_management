import mysql.connector as mc
from mysql.connector import errorcode
import string
import random
from datetime import date

def Transaction():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print("\nThis is the portal to deposit or withdraw money from account")
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
                C=int(input("Enter 1 for deposit and 2 for withdrwal : "))
                if C==1:
                    Amount=float(input("Enter the amount you want to deposit : "))
                    S=17
                    Transaction_id=''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                    Query="insert into transaction (Transaction_id,Account_No,Money_credited,Date) values ('{}',{},{},'{}')"
                    cur.execute(Query.format(Transaction_id,Account_No,Amount,str(date.today())))
                    cur.execute("update customer set Balance=Balance+{} where Account_No={}".format(Amount,Account_No))
                    cur.execute("Commit")
                    print("Amount Credited\n")
                    break
                elif C==2:
                    Amount=float(input("Enter the amount you want to withdraw : "))
                    S=17
                    Transaction_id=''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                    Query="insert into transaction (Transaction_id,Account_No,Money_debited,Date) values ('{}',{},{},'{}')"
                    cur.execute(Query.format(Transaction_id,Account_No,Amount,str(date.today())))
                    cur.execute("update customer set Balance=Balance-{} where Account_No={}".format(Amount,Account_No))
                    cur.execute("Commit")
                    print("Amount Debited\n")
                    break
                else:
                    print("Inavlid Choice!!!\n")
                    break
            else:
                print("Account does not exist!!!\n")
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def Account_Statement():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print("\nThis is the portal to get account statement")
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
                Query="select * from transaction where Account_No={}"
                cur.execute(Query.format(Account_No))
                print("Transaction Id\t\t|\t Account No\t|\tMoney Credited\t|\tMoney Debited\t|\tDate")
                Details=cur.fetchall()
                for (Transaction_id,Account_No,Credit,Debit,Date) in Details:
                    print(Transaction_id,'\t|\t',Account_No,'\t|\t',Credit,'\t\t|\t',Debit,'\t\t|\t',Date)
                cur.execute("select Balance from Customer where Account_No={}".format(Account_No))
                print("Balance in Account :",cur.fetchone()[0])
                print("Complete!!!\n")
                break
            else:
                print("Account does not exist")
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def Transfer_Amount():
    try:
        cnx=mc.connect(host='localhost',
                       user='root',
                       passwd='yes',
                       database='post_office')
        cur=cnx.cursor()
        print("\nThis is the portal to transfer money from account\n")
        while True:
            Account_No1=int(input("\nPlease enter the account number from which you have to transfer money : "))
            cur.execute('select Account_No from Customer;')
            Data=cur.fetchall()
            Acc_exist=False
            for i in Data:
                if Account_No1==i[0]:
                    Acc_exist=True
                    break
            if Acc_exist == True:
                cur.execute('select Name from Customer where Account_No={}'.format(Account_No1))
                print('Account is registered with name : ',cur.fetchone()[0])
                while True:
                    Account_No2=int(input("Enter account number to which you want to transfer money : "))
                    cur.execute('select Account_No from Customer;')
                    Data=cur.fetchall()
                    Acc_exist=False
                    for i in Data:
                        if Account_No2==i[0]:
                            Acc_exist=True
                            break
                    if Acc_exist == True:
                        cur.execute('select Name from Customer where Account_No={}'.format(Account_No2))
                        print('Account is registered with name : ',cur.fetchone()[0])
                        Amount=float(input("Enter amount you want to transfer : "))
                        S=17
                        Transaction_id=''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
                        Query="insert into transaction (Transaction_id,Account_No,Money_debited,Date) values ('{}',{},{},'{}')"
                        cur.execute(Query.format(Transaction_id,Account_No1,Amount,str(date.today())))
                        cur.execute("update customer set Balance=Balance-{} where Account_No={}".format(Amount,Account_No1))
                        Query="insert into transaction (Transaction_id,Account_No,Money_credited,Date) values ('{}',{},{},'{}')"
                        cur.execute(Query.format(Transaction_id,Account_No2,Amount,str(date.today())))
                        cur.execute("update customer set Balance=Balance+{} where Account_No={}".format(Amount,Account_No2))
                        cur.execute("Commit")
                        print("\nTransaction Complete!!!\n")
                        break
                    else:
                        print("Account in which you want to transfer money does not exist\n")
                break
            else:
                print("Account from which you want to transfer money does not exist")
        cnx.close()
    except mc.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
        
            
                
            
            
            
    
    
    
            
            
    
    

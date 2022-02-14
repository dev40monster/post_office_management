import Admin_Login_Table,Customer_Table, Transaction_Table, Loan_Table, Id_Verification_Table


print("\n\t\t****************************************************\n")
print("Welcome to A&D Post Office Bank!\n")
print("Please login to continue with the program\n")
Admin_Login_Table.login()
while True:
    print("\nTo which section you would like to proceed to?")
    print('''
1)Admin settings
2)Accounts
3)Transaction
4)ID Verification/KYC
5)Loan
6)Exit''')
    C=int(input("Please enter your choice : "))
    if C==1:
        print("\nWelcome to the admin portal!")
        K='a' #initialise K
        while K!='':
            print('''\n\t\t*****MENU*****
1)Add new user
2)Delete existing user
3)Back to main menu\n''')
            Ch=int(input("Please enter your choice : "))
            if Ch==1:
                Admin_Login_Table.new_user()
                K=input("Press any key to continue : ")
            elif Ch==2:
                Admin_Login_Table.del_user()
                K=input("Press any key to continue : ")
            elif Ch==3:
                K=''
            else:
                print("Invalid choice\n")
        
    elif C==2:
        print("\nWelcome to the accounts portal!")
        K='a' #initialise K
        while K!='':
            print('''\n\t\t*****MENU*****
1)Open a new account
2)Update account details
3)Check Balance
4)Delete existing account
5)Display account details
6)Back to main menu\n''')
            Ch=int(input("Please enter your choice : "))
            if Ch==1:
                Customer_Table.New_Acc()
                K=input("Press any key to continue : ")
            elif Ch==2:
                Customer_Table.Update_Acc()
                K=input("Press any key to continue : ")
            elif Ch==3:
                Customer_Table.Check_Balance()
                K=input("Press any key to continue : ")
            elif Ch==4:
                Customer_Table.Delete_Account()
                K=input("Press any key to continue : ")
            elif Ch==5:
                Customer_Table.Display_Acc_Details()
                K=input("Press any key to continue : ")
            elif Ch==6:
                K=''
            else:
                print("Invalid choice\n")
    elif C==3:
        print("\nWelcome to the transactions portal!")
        K='a' #initialise K
        while K!='':
            print('''\n\t\t*****MENU*****
1)Deposit or withdraw amount
2)Account Statement
3)Transfer amount
4)Back to main menu\n''')
            Ch=int(input("Please enter your choice : "))
            if Ch==1:
                Transaction_Table.Transaction()
                K=input("Press any key to continue : ")
            elif Ch==2:
                Transaction_Table.Account_Statement()
                K=input("Press any key to continue : ")
            elif Ch==3:
                Transaction_Table.Transfer_Amount()
                K=input("Press any key to continue : ")
            elif Ch==4:
                K=''
            else:
                print("Invalid choice\n")
    elif C==4:
        print("\nWelcome to the ID Verification/KYC portal!")
        K='a' #initialise K
        while K!='':
            print('''\n\t\t*****MENU*****
1)New KYC
2)Check KYC Status
3)Back to main menu\n''')
            Ch=int(input("Please enter your choice : "))
            if Ch==1:
                Id_Verification_Table.New_Kyc()
                K=input("Press any key to continue : ")
            elif Ch==2:
                Id_Verification_Table.Kyc_status()
                K=input("Press any key to continue : ")
            elif Ch==3:
                K=''
            else:
                print("Invalid choice\n")
    elif C==5:
        print("\nWelcome to the loans portal!")
        K='a' #initialise K
        while K!='':
            print('''\n\t\t*****MENU*****
1)Get new loan
2)Loan Details
3)Back to main menu\n''')
            Ch=int(input("Please enter your choice : "))
            if Ch==1:
                Loan_Table.New_Loan()
                K=input("Press any key to continue : ")
            elif Ch==2:
                Loan_Table.loan_details()
                K=input("Press any key to continue : ")
            elif Ch==3:
                K=''
            else:
                print("Invalid choice\n")
    elif C==6:
        break
    else:
        print("Invalid Choice\n")
print("\n\t\t*****\tThanks for using the software.\t*****")
print("\t\t*****\t\tHave a nice day.\t*****")
print("\n\t\t****************************************************\n")
        
        
                
                
                
            



                        
                        
                    


            
    
    

        


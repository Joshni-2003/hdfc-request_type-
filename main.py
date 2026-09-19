
from authentication import sign_up,login
from customer_menu import withdraw,deposit,check_balance,request



print("1. Signup")
print("2. Login")
print("3. Exit")
choose=int(input("Enter a option:"))
if choose==1:
    sign_up()
elif choose==2:
    abc=login()
    # print(abc)
    user_id,user_name,user_password,user_role=abc
    # print(user_role)
    if user_role=="customer":
        print("-----customer menu----")
        print("1. withdraw")
        print("2. deposit")
        print("3. check_balance")
        print("4.request(atm/loan/checkbook)")
        choose=int(input("enter a option here:"))
        if choose==1:
            withdraw(user_id)
        if choose==2:
            deposit(user_id)
        if choose==3:
            check_balance(user_id)
        if choose==4:
            request(user_id)
        
        


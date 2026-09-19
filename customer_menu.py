from db import get_connection
connection=get_connection()
cur=connection.cursor()
def withdraw(user_iddd):
    amnt=float(input("enter a amount:"))
    cur.execute("update account set account_balance=account_balance-%s where user_id=%s",(amnt,user_iddd))
    connection.commit()
    print("amount withdrawn successfully")
def deposit(user_iddd):
    amnt=int(input("enter a amount:"))
    cur.execute("update account set account_balance=account_balance+%s where user_id=%s",(amnt,user_iddd))
    cur.execute("select * from account where user_id=%s",(user_iddd,))
    person=cur.fetchone()
    acc_id,user_id,acc_type,acc_balance=person
    connection.commit()
    print(f"{amnt} credited to your account successfully and total balance:",acc_balance)
def check_balance(user_iddd):
    cur.execute("select * from account where user_id=%s",(user_iddd,))
    person=cur.fetchone()
    acc_id,user_id,acc_type,acc_bal=person
    connection.commit()
    print(f"your main balance is {acc_bal}")
def request(user_iddd):
    print("1.loan")
    print("2. atm")
    print("3. checkbook")
    ch=int(input("enter your option:"))
    if ch==1:
        req_type="loan"
        amt=float(input("enter loan quoting amount:"))
    elif ch==2:
        req_type="atm_card"
        amt=0
    elif ch==3:
        req_type="checkbook"
        amt=0
    else:
        print("invalid request")
        return
    cur.execute("insert into requests(user_id,request_type,req_amount)values(%s,%s,%s)",(user_iddd,req_type,amt))
    connection.commit()
    print("request raised successfully")

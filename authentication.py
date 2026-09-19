from db import get_connection 
connection=get_connection()
cur=connection.cursor()
def sign_up():
    
    u_name=input("Enter a user name:")
    u_pswd=input("Enter a password:")
    u_role=input("Enter a role(admin/customer):")
    cur.execute("insert into users(user_name,user_password,user_role)values(%s,%s,%s)",(u_name,u_pswd,u_role))
    connection.commit()
    print(f"{u_name} registered as {u_role} successfully")

    cur.execute("select * from users where user_name=%s",(u_name,))
    data=cur.fetchone()
    print(data)

   
    acc_type=input("Enter the type of account(savings/current):")
   
    cur.execute("insert into account(user_id,account_type,account_balance)values(%s,%s,%s)",(data[0],acc_type,15000))
    
    print(f"account created to {u_name} successfully")
    connection.commit()
    connection.close()
    
def login():
    us_name=input("Enter a user name:")
    us_pswd=input("Enter a user password:")
    cur.execute("select * from users where user_name=%s and user_password=%s",(us_name,us_pswd))
    data=cur.fetchone()
    # print(data)
    if not data:
        print("no credentials found")
    else:
        # print(data)
        # print("loggined successfully")
        return data




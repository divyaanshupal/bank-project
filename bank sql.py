import random
import mysql.connector as mr
def menu():
    print('''                  <<***MONEY BANK OF INDIA***>>             ''')
    print("                  [WITH You - all  the ways]           ")
    print("welcome we can help you by:-")
    print(" 1>> create a account \n 2>> Login into your Account \n 3>> update a account ")
    p=input('Please enter your MYSQL DATABASE Password -')
    n=input('enter your choice-').strip()
    if n=='1':
        create(p)
    if n=='2':
        login(p)
    

def database(p):
    db=mr.connect(user='root',
                 host='localhost',
                 password=p)
    cur=db.cursor()
    try:
        cur.execute('use bank_trial')
    except:
        cur.execute('create database bank_trial')
        cur.execute('use bank_trial')
    try:
        cur.execute('desc bank_data')
    except:
        cur.execute('create table bank_data(Name varchar(25), Phone_Number varchar(10) , Nominee_name varchar(25) , Acc_number int , Password int) ')
        
        
                 
def create(p): 
    print('For creating your account please give all deatls sir ....please enter correct details')
    print("                    <<<REGISTRATION FORM>>>              ")
    a=input('Enter Your Complete Name-')
    b=(input('enter your coplete phone number-'))
    c=input('please enter a nominee name-')
    print('Thank you sir for giving your details and precious time your account is created and we welcome you in our BOB Family')
    d=random.randint(123456789,987654321)
    e=random.randint(123456,654321)
    print('Your Account number =',d)
    print('Your Login Pass=',e)
    print('Please take this seriously and save them as this is the only key to access to your account in the future')
    try:
        store(a,b,c,d,e)
    except:
        database(p)
        store(a,b,c,d,e,p)
def store(a,b,c,d,e,p):
    db=mr.connect(user='root',
                  host='localhost',
                  password=p,
                  database='bank_trial')
    cur=db.cursor()
    cur.execute("insert into bank_data values('{}','{}','{}',{},{})".format(a,b,c,d,e))
    db.commit()

def login(p):
    acc=int(input('Enter your Account number-'))
    passw=int(input('enter the password please-'))
    try:
        db=mr.connect(user='root',
                      host='localhost',
                      password=p,
                      database='bank_trial')
        cur=db.cursor()
        cur.execute("select * from bank_data where Acc_number={} and Password={}".format(acc,passw))
        for i in cur:
            print(i)
        return True
    except:
        return False
        
        

menu()
                  
    

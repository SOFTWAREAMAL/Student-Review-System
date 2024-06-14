"STUDENT REVIEW SYSTEM"
c={}
d={}
wr_dict={}
al_list=[]
store_review_dict = {}
terminate_dict={}
def signup():
    siun=input("create your usesrname:")
    siupw=input("create your password:")
    if siun in c:
        print("username is already used")
    elif siun in terminate_dict:
        print("you are terminated by admin\n you must pay fine rs.500 for signin")
    else:
        c[siun]=siupw
        print("you are signup sucessfully")
        print(c)
        
def login():
    lun=input("Enter your user name:")
    lupw=input("Entre your password:")
    if lun in al_list:
        print("username already exist")
    elif lun in c and c[lun]==lupw:
        print("login successful")
        al_list.append(lun)
        print(al_list)
    elif lun in terminate_dict:
        print("you are terminated by admin\n you must pay fine rs.500 for signin")
    else:
        print("invalid login username or password")
        
def logout():
    lo_id=input("Enter your username:")
    lo_pw=input("Enter your password")
    if lo_id in c and c[lo_id]==lo_pw:
        print("you are successfully logout")
    
def admin_login():
    alu=input("Enter admin username:")
    alp=input("Enter admin password:")
    d[alu]=alp
    print("admin login successful")

def check_admin_login():
    while True:
        cdu=input("Enter admin username:")
        cdl=input("Enter admin password:")
        if cdu in d:
            if d[cdu] == cdl:
                print("admin login verified")
                break
            else:
                print("invalid admin password")    
       
def admin_logout():
    alou=input("Enter admin username:")
    alop=input("Enter adamin password:")
    if alou in d and d[alou]==alop:
        print("admin logout successfully")
    else:
        print("invalid username or password")
        
def write_review():
    wr=input("Username:")
    if wr in al_list:
        w=input("write_review:")
        store_review_dict[wr]=w
        print(store_review_dict)
         
    else:
        print("invaid username or password:")
        
def read_review():
    check_admin_login()
    #o/p:1
    rr=input("Enter login username:")
    if rr in al_list:
        for i in store_review_dict:
            print("username:",i,"& review is:",'\"', store_review_dict[i] ,'\"')
    else:
         print("invalid username are password")
         #o/p:2
         #print("username:",rr,"& review is:", store_review_dict.get(rr))
             
def delete_review():
    check_admin_login()
    dr=input("Enter username for delete review:")
    if dr in al_list:
         print('\"login username is verified\"')         
    else:
         print("invalid username or password")
         
    if dr in c:
        print("Before:",store_review_dict)
        store_review_dict.pop(dr)
        print("After:",store_review_dict)        
    else:
        print("check the login username")
        
def terminate_user():
    check_admin_login()
    tr=input("Enter the terminate user name:")
    if tr in al_list:
        if tr in c:
            al_list.remove(tr)
            x=c.pop(tr)
            terminate_dict.setdefault(tr,x)
            print("user signin terminate by admin")
            print("sign in users list:",al_list)
            print("terminate_dict:",terminate_dict)
        else:
            print("check the login username")
    else:
        print("invalid username or password")
            
def login_list():
    check_admin_login()
    print("sign in users list:")
    for i in c:
        print(i)
        
def fine_amount():
    fa_id=input("Enter terminated signup name:")
    fa_pw=input("Enter the password:")
    if fa_id in terminate_dict and fa_pw == terminate_dict[fa_id]:
        f_amount = int(input("Enter fine amount rs:"))
        if f_amount >= 500:
            al_list.append(fa_id)
            c.setdefault(fa_id,fa_pw)
            print("Amount paid \nyou are elgibile to login")
        else:
            print("invalid terminate name")
            
while True:
    print("\n1.signup","\n2.login","\n3.logout","\n4.admin_login","\n5.check_admin_login","\n6.admin_logout","\n7.write_rewiew","\n8.read_review",
          "\n9.delete_review","\n10.terminate_user","\n11.login_list","\n12.fine_amount","\n13.Exit")

    a=int(input("Enter your choice:"))

    if a==1:
        signup()
    elif a==2:
        login()
    elif a==3:
        logout()
        
    elif a==4:
        admin_login()
    elif a==5:
        check_admin_login()
    elif a==6:
        admin_logout()
        
    elif a==7:
        write_review()
    elif a==8:
        read_review()
    elif a==9:
        delete_review()
    elif a==10:
        terminate_user()
    elif a==11:
        login_list()
    elif a==12:
        fine_amount()
    elif a==13:
        print('\"Thankyou\"')
        break
    
    else:
        print("invalid process")

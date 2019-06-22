from time import sleep
from pygame import mixer
from gtts import gTTS 
import os
from getpass import getpass
import json as js
mixer.init()
acnumber=1236

def welcome():
    mytext = 'Welcome to My First project which is based on Banking System!'
    print(mytext)
    #language = 'en' 
    #myobj = gTTS(text=mytext, lang=language, slow=False) 
    #myobj.save("welcome.mp3") 
    #os.system("welcome.mp3")

    mixer.music.load("welcome.mp3")
    mixer.music.play()
    sleep(4)
    Main()
    return

def Main(): 
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    ch="choose an option from the following:"
    #language = 'en' 
    #myobj = gTTS(text=ch, lang=language, slow=False) 
    #myobj.save("choose.mp3") 
    #os.system("choose.mp3")
    print(ch)
    mixer.music.load("choose.mp3")
    mixer.music.play()
    op='''1)deposit\n2)withdrawl\n3)cheak balance\n4)Make a new account\n5)Edit you personal details\n6)Manager login\n7)Apply for a loan\n8)exit'''
    print(op)
    choice=int(input("entert the choioce in single digit number"))
    if choice==1:
        deposit()
    elif choice==2:
        withdrawl()
    elif choice==3:
        balanceeq()
    elif choice==4:
        new_account()
    elif choice==5:
        edit_info()
    elif choice==6:
        manager_login()
    elif choice==7:
        loan()
    elif choice==8:
        print("closing the program",end="")
        mixer.music.load("close.mp3")
        mixer.music.play()
        for i in range(1,8):
            sleep(0.3)
            #clear screen 3 dots
            if i%3==0:
                os.system('cls')
                sleep(0.3)
            print(".",end="")
        return
    else:
        print("you had't choose from these options")
        mixer.music.load("nochoice.mp3")
        mixer.music.play()
    coe=input("enter continue if you want to continue otherwise enter anything to exit:").lower().strip()
    mixer.music.load("continue.mp3")
    mixer.music.play()
    if coe=="continue":
        Main()
    else:
        return


def deposit():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    cd="you want to deposit money"
    language = 'en' 
    #myobj = gTTS(text=cd, lang=language, slow=False) 
    #myobj.save("cd.mp3") 
    #os.system("cd.mp3")
    mixer.music.load("cd.mp3")
    mixer.music.play()
    sleep(2.5)

    ac=account_number()
    data=database()
    
    if str(ac) not in data.keys():
        print("your account number is not registered ")
        mixer.music.load("notreg.mp3")
        mixer.music.play()
        print("choose an option:")
        print("1)for deposit money in another account choose this")
        print("2)for making a new account please choose Make a new account option in Main bar after selecting this")
        ch1=int(input())
        if ch1==1:
            deposit()
        if ch1==2:
            Main()
        else:
            print("not a correct choice")
            Main()
        return           #do noting after get back from function calling
    
    
    d="enter the amount and deposit"
    print(d,end=" ")
    #language = 'en' 
    #myobj = gTTS(text=d, lang=language, slow=False) 
    #myobj.save("depo.mp3") 
    #os.system("depo.mp3")
    mixer.init()
    mixer.music.load("depo.mp3")
    mixer.music.play()
    da=int(input())
    data[str(ac)][0]+=da
    updatedata(data)
    nb=new_balance(data,ac)
    print(f"your new balance is {nb}")
    backup()
    return

def account_number():
    a="please enter your account number:"
    print(a,end=' ')
    
    
    #language = 'en' 
    #myobj = gTTS(text=a, lang=language, slow=False) 
    #myobj.save("acno.mp3") 
    #os.system("acno.mp3")
    mixer.init()
    mixer.music.load("acno.mp3")
    mixer.music.play()
    #try:
    ac=int(input())
    #except:
        #return
    return ac


def database():
    dp = open("deposit.db","r+")
    data=js.load(dp)
    print(data)
    dp.close()
    return data

def new_balance(data,ac):
    return data[str(ac)][0]

def updatedata(data):
    dp = open("deposit.db","w")
    data=js.dump(data,dp)
    print(data)
    dp.close()

def username():
    un="enter your user name :"
    print(un,end=" ")
    #language = 'en' 
    #myobj = gTTS(text=un, lang=language, slow=False) 
    #myobj.save("un.mp3") 
    #os.system("un.mp3")
    mixer.music.load("un.mp3")
    mixer.music.play()
    user_name=input()
    return(user_name)

def password():
    pss="enter your password"
    #language = 'en' 
    #myobj = gTTS(text=pss, lang=language, slow=False) 
    #myobj.save("pss.mp3") 
    #os.system("pss.mp3")
    mixer.music.load("pss.mp3")
    mixer.music.play()
    p=getpass(pss)
    return p

def backup():
    fp = open('deposit.db',"r")
    data=js.load(fp)
    fp.close()
    fp = open('backup.db',"w")
    js.dump(data,fp)
    fp.close()

def account_reactivate():
    ac=account_number()
    od=open('deposit.db',"r")
    olddata=js.load(od)
    od.close()
    fp = open('backup.db',"r")
    data1=js.load(fp)
    olddata[str(ac)]=data1[str(ac)]
    print(olddata)
    fp1 = open('deposit.db',"w")
    js.dump(olddata,fp1)
    fp1.close()
    fp.close()


def cheakuserandpass(u,p,ac,data,c):
    if u != data[str(ac)][1][0] or p != data[str(ac)][1][1]:
        print("your user name or password is incorrect")
        print("choose an option:")
        mixer.music.load("choose.mp3")
        mixer.music.play()
        print("1)for withdrawl money from another account choose this")
        print("2)for try re-entering username and password:")
        ch1=int(input())
        if ch1==1:
            withdrawl()
        if ch1==2:
            if c==2:
                dp = open("deposit.db","w")
                data[str(ac)]="account deactivated, please contact your bank"
                data=js.dump(data,dp)
                print(data)
                dp.close()
                print("you have tried 3 times in a row")
                print("your account is deactivated")
                print("please contact your bank to re-activate your account")
                return False
            else:
                u=username()
                p=password()
                c+=1
                a=cheakuserandpass(u,p,ac,data,c)
        else:
            print("not a correct choice")
            Main()
            return
            
    else:
        return True
    if a==True:
        return True



def withdrawl():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    cw="you want to withdrawl money"
    #language = 'en' 
    #myobj = gTTS(text=cw, lang=language, slow=False) 
    #myobj.save("cw.mp3") 
    #os.system("cw.mp3")
    mixer.music.load("cw.mp3")
    mixer.music.play()
    sleep(2.5)
    
    wamt="enter the amount you want to withdrawl "
    print(wamt,end=" ")
    mixer.music.load("wamt.mp3")
    mixer.music.play()
    witamt=int(input())
    
    data=database()
    
    ac=account_number()
    
    if str(ac) not in data.keys():
        print("your account number is not registered ")
        mixer.music.load("notreg.mp3")
        mixer.music.play()
        sleep(2.5)
        print("choose an option:")
        mixer.music.load("choose.mp3")
        mixer.music.play()
        sleep(2.5)
        print("1)for withdrawl money from another account choose this")
        print("2)for making a new account please choose Make a new account option in Main bar after selecting this")
        ch1=int(input())
        if ch1==1:
            withdrawl()
        if ch1==2:
            Main()
        else:
            print("not a correct choice")
            Main()
        return        #do noting after get back from function calling
    
    un=username()
    p=password()
    
    c=0
    cup=cheakuserandpass(un,p,ac,data,c)
    '''if u != data[str(ac)][1][0] or p != data[str(ac)][1][1]
        print("your user name or password is incorrect")
        print("choose an option:")
        print("1)for withdrawl money from another account choose this")
        print("2)for making a new account please choose Make a new account option in Main bar after selecting this")
        print("3)for try re-entering username and password:")
        ch1=int(input())
        if ch1==1:
            withdrawl()
        if ch1==2:
            main()
        if ch1==3:
            if c==4:
                dp = open("deposit.db","w")
                data[str(ac)]="account deactivated, please contact your bank"
                data=js.dump(data,dp)
                print(data)
                dp.close()
                print("you have tried 3 times in a row")
                print("your account is deactivated")
                print("please contact your bank to re-activate your account")
                return
            else:
                u=username()
                p=password()
                c+=1
    
    '''
    if cup==True:
        if data[str(ac)][0]<witamt:
            print("not enough balance")
        else:
            data[str(ac)][0]-=witamt
            print(f"{witamt} amount deducted")
            print(f"Balance left->{data[str(ac)][0]}")
            updatedata(data)
    else:
        return
    backup()
    return


def balanceeq():
    ac=account_number()
    data=database()
    if str(ac) not in data.keys():
        print("your account number is not registered ")
        mixer.music.load("notreg.mp3")
        mixer.music.play()
        sleep(2.5)
        print("choose an option:")
        mixer.music.load("choose.mp3")
        mixer.music.play()
        print("1)for balance enquiry of another account choose this")
        print("2)for making a new account please choose Make a new account option in Main bar after selecting this")
        ch1=int(input())
        if ch1==1:
            balanceeq()
        if ch1==2:
            main()
        return 
    bal=new_balance(data,ac)
    print(f"remaining balance of account number {ac} is {bal}")




def new_account():
    global acnumber
    firstname=input("enter your first name:")
    lastname=input("enter your last name:")
    mob=addmobile()
    address=addaddress()
    un=addusername()
    pw=password()
    data=database()
    data[str(acnumber)]=[0,[un,pw]]
    unc=open("deposit.db",'w')
    js.dump(data,unc)
    unc.close()
    print(data)
    backup()
    unc=open("perde.db",'r')
    data1=js.load(unc)
    unc.close()
    print(data1)
    data1[str(acnumber)]=[firstname,lastname,mob,address]
    unc=open("perde.db",'w')
    js.dump(data1,unc)
    unc.close()
    print(data1)
    acnumber=acnumber+1
    backupofdetails()



def addmobile():
    #try:
    mob=int(input("enter your mobile number: "))
    #except:
        #print("mobile number must be in numbers")
        #Main()
        #return
    return mob


def addaddress():
    address=input("enter your permanent address: ")
    return address


def addusername():
    un=input("enter your user name:")
    unc=open("deposit.db",'r')
    data=js.load(unc)
    unc.close()
    for i in data.values():
        if un in i[1][0]:
            print("username already exists, please enter different username")
            un=addusername()
    return un


def backupofdetails():
    fp = open('perde.db',"r")
    data=js.load(fp)
    fp.close()
    fp = open('backupofdetails.db',"w")
    js.dump(data,fp)
    fp.close()



def edit_info():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    print("enter your account number:")
    ac=str(account_number())
    data=database()
    if ac in data.keys():
        print("enter your user name and password:")
        un=username()
        pw=password()
        if un==data[ac][1][0]:
            if pw==data[ac][1][1]:
                print("choose what you want to edit: ")
                print("1)address/n2)password/n3)mobile number")
                ch=int(input())
                if ch==1:
                    address=addaddress()
                    unc=open("perde.db",'r')
                    data1=js.load(unc)
                    unc.close()
                    print(data1)
                    data1[str(ac)][3]=address
                    unc=open("perde.db",'w')
                    js.dump(data1,unc)
                    unc.close()
                    print(data1)
                    backupofdetails()
                elif ch==3:
                    nmn=addmobile()
                    unc=open("perde.db",'r')
                    data1=js.load(unc)
                    unc.close()
                    print(data1)
                    data1[str(ac)][2]=nmn
                    unc=open("perde.db",'w')
                    js.dump(data1,unc)
                    unc.close()
                    print(data1)
                    backupofdetails()
                else:
                    npw=password()
                    unc=open("deposit.db",'r')
                    data1=js.load(unc)
                    unc.close()
                    print(data1)
                    data1[str(ac)][1][1]=npw
                    unc=open("deposit.db",'w')
                    js.dump(data1,unc)
                    unc.close()
                    print(data1)
                    backup()
                    
            else:
                print("incorrect usename or password")
                print("choose what you want to do now: ")
                print("1)edit another account details/nelse)go to main")
                ch1=int(input())
                if ch1==1:
                    edit_info()
                return
        else:
            print("incorrect user name or password")
            print("choose what you want to do now: ")
            print("1)edit another account details/nelse)go to main")
            ch1=int(input())
            if ch1==1:
                edit_info()
            return
    else:
        print("incorrect account number")
        print("choose what you want to do now: ")
        print("1)edit another account details/nelse)go to main")
        ch1=int(input())
        if ch1==1:
            edit_info()
    return



def manager_login():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    un=username()
    pw=password()
    data=mdatabase()
    data1=database()
    unc=open("perde.db","r")
    data2=js.load(unc)
    unc.close()
    if un in data.keys():
        if pw in data.values():
            ac=account_number()
            getdetails(data1,data2,ac)
    return


def mdatabase():
    dp = open("manager.db","r+")
    data=js.load(dp)
    print(data)
    dp.close()
    return data



def getdetails(data1,data2,ac):
    print(f"personal details of this account holder are:")
    print(f"1)First name->{data2[str(ac)][0]}/n2)last name->{data2[str(ac)][1]}/n3)mob. no.->{data2[str(ac)][2]}/n4)address->{data2[str(ac)][3]}/n1)Balance->{data1[str(ac)][0]}/n")
    print("choose an option from the following:")
    print("1)get someone else details/nelse)go to main")
    a=int(input())
    if a==1:
        ac=account_number()
        getdetails(data1,data2,ac)
    return


def loan():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    ac=account_number()
    data=database()
    la=0
    if str(ac) in data.keys():
        data=database()
        print("choose your profession:")
        print("1)government employee/n2)private sector/n3)student/n4)unemployed/n5)bussiness")
        ch=int(input())
        if ch==3 or ch==4:
            print("you can't apply for a loan")
        elif ch==1:
            s=salary()
            if s<50000:
                print("you can't apply for a loan")
                return
            elif s<100000:
                print("you can get maximum loan of 2,00,000")
                la=200000
            elif s<500000:
                print("you can get maximum loan of 4,00,000")
                la=400000
            else:
                print("you can get maximum loan of 10,00,000")
                la=1000000
            loanapp(la,ac)
                    
        elif ch==2:
            s=salary()
            if s<50000:
                print("you can't apply for a loan")
                return
            elif s<100000:
                print("you can get maximum loan of 1,00,000")
                la=100000
            elif s<500000:
                print("you can get maximum loan of 3,00,000")
                la=300000
            else:
                print("you can get maximum loan of 7,00,000")
                la=700000
            loanapp(la,ac)
        elif ch==5:
            s=salary()
            if s<40000:
                print("you can't apply for a loan")
                return
            elif s<100000:
                print("you can get maximum loan of 50,000")
                la=50000
            elif s<300000:
                print("you can get maximum loan of 1,20,000")
                la=120000
            else:
                print("you can get maximum loan of 5,00,000")
                la=500000
            loanapp(la,ac)
        else:
            print("you haven't choose from given options")
    return



def salary():
    s=int(input("enter your monthly income:"))
    return s



def loanamt():
    l=int(input("enter the amount you want as a loan"))
    return l



def loanapp(la,ac):
    q=int(input("do you have payslip/n1)yes/n2)no"))
    q1=int(input("do you have ITR/n1)yes/n2)no"))
    q2=int(input("do you have GST no./n1)yes/n2)no"))
    if q==1 or q1==1 or q2==1:
        loanamtch(la,ac)
    else:
        print("you can't apply for a loan")
        return
    return



def loanamtch(la,ac):
    gst=int(input("enter gst number: "))
    lamt=loanamt()
    if lamt>la:
        print("you can't apply for a loan")
        print("choose an option from the following:")
        print("1)change loan amount/nelse)go to main")
        l=int(input())
        if l==1:
            loanamtch()
    else:
        print("loan approved")
        saveloandata(lamt,ac,gst)
    return



def saveloandata(lamt,ac,gst):
    unc=open("loandata.db","r")
    data=js.load(unc)
    unc.close()
    data[str(ac)]=[lamt,gst]
    unc=open("loandata.db","w")
    js.dump(data,unc)
    unc.close()




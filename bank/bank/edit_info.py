def edit_info():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    print("enter your account number:")
    ac=str(bank.account_number.account_number())
    data=bank.database.database()
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
                    address=bank.addaddress.addaddress()
                    unc=open("perde.db",'r')
                    data1=js.load(unc)
                    unc.close()
                    print(data1)
                    data1[str(ac)][3]=address
                    unc=open("perde.db",'w')
                    js.dump(data1,unc)
                    unc.close()
                    print(data1)
                    bank.backupofdetails.backupofdetails()
                elif ch==3:
                    nmn=bank.addmobile.addmobile()
                    unc=open("perde.db",'r')
                    data1=js.load(unc)
                    unc.close()
                    print(data1)
                    data1[str(ac)][2]=nmn
                    unc=open("perde.db",'w')
                    js.dump(data1,unc)
                    unc.close()
                    print(data1)
                    bank.backupofdetails.backupofdetails()
                else:
                    npw=bank.password.password()
                    unc=open("deposit.db",'r')
                    data1=js.load(unc)
                    unc.close()
                    print(data1)
                    data1[str(ac)][1][1]=npw
                    unc=open("deposit.db",'w')
                    js.dump(data1,unc)
                    unc.close()
                    print(data1)
                    bank.backup.backup()
                    
            else:
                print("incorrect usename or password")
                print("choose what you want to do now: ")
                print("1)edit another account details/nelse)go to main")
                ch1=int(input())
                if ch1==1:
                    bank.edit_info.edit_info()
                return
        else:
            print("incorrect user name or password")
            print("choose what you want to do now: ")
            print("1)edit another account details/nelse)go to main")
            ch1=int(input())
            if ch1==1:
                bank.edit_info.edit_info()
            return
    else:
        print("incorrect account number")
        print("choose what you want to do now: ")
        print("1)edit another account details/nelse)go to main")
        ch1=int(input())
        if ch1==1:
            bank.edit_info.edit_info()
    return


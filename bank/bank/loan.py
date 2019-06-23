def loan():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    ac=bank.account_number.account_number()
    data=bank.database.database()
    la=0
    if str(ac) in data.keys():
        data=bank.database.database()
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
            bank.loanapp.loanapp(la,ac)
                    
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
            bank.loanapp.loanapp(la,ac)
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
            bank.loanapp.loanapp(la,ac)
        else:
            print("you haven't choose from given options")
    return
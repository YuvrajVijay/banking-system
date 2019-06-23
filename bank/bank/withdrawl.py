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
    
    data=bank.database.database()
    
    ac=bank.account_number.account_number()
    
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
            bank.withdrawl.withdrawl()
        if ch1==2:
            bank.Main.Main()
        else:
            print("not a correct choice")
            bank.Main.Main()
        return        #do noting after get back from function calling
    
    un=bank.username.username()
    p=bank.password.password()
    
    c=0
    cup=bank.cheakuserandpass.cheakuserandpass(un,p,ac,data,c)
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
            bank.updatedata.updatedata(data)
    else:
        return
    bank.backup.backup()
    return
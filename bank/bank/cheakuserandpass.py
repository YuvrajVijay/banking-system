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
            bank.withdrawl.withdrawl()
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
                u=bank.username.username()
                p=bank.password.password()
                c+=1
                a=bank.cheakuserandpass.cheakuserandpass(u,p,ac,data,c)
        else:
            print("not a correct choice")
            bank.Main.Main()
            return
            
    else:
        return True
    if a==True:
        return True
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

    ac=bank.account_number.account_number()
    data=bank.database.database()
    
    if str(ac) not in data.keys():
        print("your account number is not registered ")
        mixer.music.load("notreg.mp3")
        mixer.music.play()
        print("choose an option:")
        print("1)for deposit money in another account choose this")
        print("2)for making a new account please choose Make a new account option in Main bar after selecting this")
        ch1=int(input())
        if ch1==1:
            bank.deposit.deposit()
        if ch1==2:
            bank.Main.Main()
        else:
            print("not a correct choice")
            bank.Main.Main()
        return           #do nothing after get back from function calling
    
    
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
    bank.updatedata.updatedata(data)
    nb=bank.new_balance.new_balance(data,ac)
    print(f"your new balance is {nb}")
    bank.backup.backup()
    return
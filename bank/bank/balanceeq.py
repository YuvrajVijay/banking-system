def balanceeq():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    ac=bank.account_number.account_number()
    data=bank.database.database()
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
            bank.balanceeq.balanceeq()
        if ch1==2:
            bank.Main.Main()
        return 
    bal=bank.new_balance.new_balance(data,ac)
    print(f"remaining balance of account number {ac} is {bal}")
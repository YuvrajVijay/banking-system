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
        bank.deposit.deposit()
    elif choice==2:
        bank.withdrawl.withdrawl()
    elif choice==3:
        bank.balanceeq.balanceeq()
    elif choice==4:
        bank.new_account.new_account()
    elif choice==5:
        bank.edit_info.edit_info()
    elif choice==6:
        bank.manager_login.manager_login()
    elif choice==7:
        bank.loan.loan()
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
        bank.Main.Main()
    else:
        return

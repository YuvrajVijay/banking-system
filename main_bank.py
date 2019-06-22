from time import sleep
from pygame import mixer
from gtts import gTTS 
import os
from getpass import getpass
import json as js
mixer.init()
def Main(): 
    ch="choose an option from the following:"
    #language = 'en' 
    #myobj = gTTS(text=ch, lang=language, slow=False) 
    #myobj.save("choose.mp3") 
    #os.system("choose.mp3")
    print(ch)
    mixer.init()
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
        cheak_balance()
    elif choice==4:
        deposit()
    elif choice==5:
        deposit()
    elif choice==6:
        deposit()
    elif choice==7:
        deposit()
    elif choice==8:
        print("closing the program",end="")
        sleep(2)
            for i in range(1,8):
                sleep(0.5)
                #clear screen 3 dots
                if i%3==0:
                    os.system('cls')
                    sleep(0.7)
                    print(".",end="")
            return
    else:
        print("you had't choose from these options")
    coe=input("enter continue if you want to continue otherwise enter anything to exit:").lower().strip()
    if coe=="continue":
        welcome()
    else:
        return
Main()

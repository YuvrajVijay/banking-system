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
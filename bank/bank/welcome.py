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
    bank.Main.Main()
    return

welcome()

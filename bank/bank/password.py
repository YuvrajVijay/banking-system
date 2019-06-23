def password():
    pss="enter your password"
    #language = 'en' 
    #myobj = gTTS(text=pss, lang=language, slow=False) 
    #myobj.save("pss.mp3") 
    #os.system("pss.mp3")
    mixer.music.load("pss.mp3")
    mixer.music.play()
    p=getpass(pss)
    return p
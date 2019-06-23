def username():
    un="enter your user name :"
    print(un,end=" ")
    #language = 'en' 
    #myobj = gTTS(text=un, lang=language, slow=False) 
    #myobj.save("un.mp3") 
    #os.system("un.mp3")
    mixer.music.load("un.mp3")
    mixer.music.play()
    user_name=input()
    return(user_name)
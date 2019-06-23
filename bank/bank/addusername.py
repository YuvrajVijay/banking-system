def addusername():
    un=input("enter your user name:")
    unc=open("deposit.db",'r')
    data=js.load(unc)
    unc.close()
    for i in data.values():
        if un in i[1][0]:
            print("username already exists, please enter different username")
            un=bank.addusername.addusername()
    return un
def manager_login():
    os.system('cls')
    print("loading",end="")
    for i in range(8):
        sleep(0.5)
        print(".",end="")
    os.system('cls')
    un=bank.username.username()
    pw=bank.password.password()
    data=bank.mdatabase.mdatabase()
    data1=bank.database.database()
    unc=open("perde.db","r")
    data2=js.load(unc)
    unc.close()
    if un in data.keys():
        if pw in data.values():
            ac=bank.account_number.account_number()
            bank.getdetails.getdetails(data1,data2,ac)
    return
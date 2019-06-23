def new_account():
    global acnumber
    firstname=input("enter your first name:")
    lastname=input("enter your last name:")
    mob=bank.addmobile.addmobile()
    address=bank.addaddress.addaddress()
    un=bank.addusername.addusername()
    pw=bank.password.password()
    data=bank.database.database()
    data[str(acnumber)]=[0,[un,pw]]
    unc=open("deposit.db",'w')
    js.dump(data,unc)
    unc.close()
    print(data)
    bank.backup.backup()
    unc=open("perde.db",'r')
    data1=js.load(unc)
    unc.close()
    print(data1)
    data1[str(acnumber)]=[firstname,lastname,mob,address]
    unc=open("perde.db",'w')
    js.dump(data1,unc)
    unc.close()
    print(data1)
    acnumber=acnumber+1
    bank.backupofdetails.backupofdetails()
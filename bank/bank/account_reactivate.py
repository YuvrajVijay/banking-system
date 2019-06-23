def account_reactivate():
    ac=bank.account_number.account_number()
    od=open('deposit.db',"r")
    olddata=js.load(od)
    od.close()
    fp = open('backup.db',"r")
    data1=js.load(fp)
    olddata[str(ac)]=data1[str(ac)]
    print(olddata)
    fp1 = open('deposit.db',"w")
    js.dump(olddata,fp1)
    fp1.close()
    fp.close()
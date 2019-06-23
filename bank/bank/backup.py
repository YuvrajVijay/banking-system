def backup():
    fp = open('deposit.db',"r")
    data=js.load(fp)
    fp.close()
    fp = open('backup.db',"w")
    js.dump(data,fp)
    fp.close()
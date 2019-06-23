def backupofdetails():
    fp = open('perde.db',"r")
    data=js.load(fp)
    fp.close()
    fp = open('backupofdetails.db',"w")
    js.dump(data,fp)
    fp.close()
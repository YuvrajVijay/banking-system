def saveloandata(lamt,ac,gst):
    unc=open("loandata.db","r")
    data=js.load(unc)
    unc.close()
    data[str(ac)]=[lamt,gst]
    unc=open("loandata.db","w")
    js.dump(data,unc)
    unc.close()

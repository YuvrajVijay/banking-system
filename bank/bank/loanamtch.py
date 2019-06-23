def loanamtch(la,ac):
    gst=int(input("enter gst number: "))
    lamt=bank.loanamt.loanamt()
    if lamt>la:
        print("you can't apply for a loan")
        print("choose an option from the following:")
        print("1)change loan amount/nelse)go to main")
        l=int(input())
        if l==1:
            bank.loanamtch.loanamtch()
    else:
        print("loan approved")
        bank.saveloandata.saveloandata(lamt,ac,gst)
    return
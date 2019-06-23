def loanapp(la,ac):
    q=int(input("do you have payslip/n1)yes/n2)no"))
    q1=int(input("do you have ITR/n1)yes/n2)no"))
    q2=int(input("do you have GST no./n1)yes/n2)no"))
    if q==1 or q1==1 or q2==1:
        bank.loanamtch.loanamtch(la,ac)
    else:
        print("you can't apply for a loan")
        return
    return
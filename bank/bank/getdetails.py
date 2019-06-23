def getdetails(data1,data2,ac):
    print(f"personal details of this account holder are:")
    print(f"1)First name->{data2[str(ac)][0]}/n2)last name->{data2[str(ac)][1]}/n3)mob. no.->{data2[str(ac)][2]}/n4)address->{data2[str(ac)][3]}/n1)Balance->{data1[str(ac)][0]}/n")
    print("choose an option from the following:")
    print("1)get someone else details/nelse)go to main")
    a=int(input())
    if a==1:
        ac=bank.account_number.account_number()
        bank.getdetails.getdetails(data1,data2,ac)
    return
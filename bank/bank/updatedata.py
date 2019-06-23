def updatedata(data):
    dp = open("deposit.db","w")
    data=js.dump(data,dp)
    print(data)
    dp.close()
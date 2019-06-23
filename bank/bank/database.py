def database():
    dp = open("deposit.db","r+")
    data=js.load(dp)
    print(data)
    dp.close()
    return data
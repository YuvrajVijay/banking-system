def mdatabase():
    dp = open("manager.db","r+")
    data=js.load(dp)
    print(data)
    dp.close()
    return data
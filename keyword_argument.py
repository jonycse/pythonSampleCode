def addValue(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print "Key",key,"value",value
        total += value
    return total


print addValue(item1=2, item2=3 ,item3=5, item4=7)
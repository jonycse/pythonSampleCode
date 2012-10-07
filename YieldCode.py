def myFun(n):
    for i in range(0,n):
        yield i


it=myFun(5)

for i in it:
    print i
'''
Problem set: https://www.spoj.com/problems/CANDY/
Status: Accepted
'''

n=input()
while n != -1:
    a=[]
    s =0
    for i in range(0,n):
        d=input()
        s  += d
        a.append(d)
    avg = int(s/n)
    if avg*n != s:
        print -1
    else:
        r=0
        for i in range(0,n):
            if a[i]<avg:
                r += (avg - a[i])
        print r
    n = input()



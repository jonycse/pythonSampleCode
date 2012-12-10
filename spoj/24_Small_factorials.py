'''
Problem set: https://www.spoj.pl/problems/FCTRL2/
Status: Accepted
'''

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n = input()
while n>0:
    n=n-1
    k=input()
    print fact(k)


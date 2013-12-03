'''
Problem set: https://www.spoj.com/problems/FCTRL/
Status: TLE
'''

def zero(number,factor):
    if number==5:
        return 1
    rt =0;
    deno =factor
    while deno<number:
        rt += int(number/deno)
        deno *= factor
    return rt;

def solution(k):
    return min(zero(k,2), zero(k,5))

n = input()
while n>0:
    n=n-1
    k=input()
    print solution(k)

'''
Problem set: https://www.spoj.com/problems/CANTON/
Status: Accepted
'''

import math

def solution(n):
    t = float(math.sqrt(1+8*(n-1)))
    k = int((t+1)/2)
    a = int((k*(k-1))/2)
    b = n - a
    if k%2==0:
        return b,(k+1)-b
    return (k+1)-b, b

case = input()
while case>0:
    n=input()
    case = case -1
    a, b = solution(n)
    print "TERM %d IS %d/%d" % (n,a,b)

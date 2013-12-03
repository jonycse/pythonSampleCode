'''
https://www.spoj.com/problems/ARMY/
status: TLE
'''
import sys

data = sys.stdin
case=int(data.readline())
#print l
#case=input()
while case>0:
    data.readline()
    case -= 1
    n, m =[int(x) for x in data.readline().split()]
    an =[int(x) for x in data.readline().split()]
    am =[int(x) for x in data.readline().split()]

    #n, m = [int(x) for x in raw_input().split()]
    #an = [int(x) for x in raw_input().split()]
    #am = [int(x) for x in raw_input().split()]

    #an.sort();
    #am.sort();
    an = sorted(an)
    am = sorted(am)
    #print an
    #print am

    i, j = 0, 0
    while i<n and j<m:
        if an[i]>=am[j]:
            j+=1
        else:
            i+=1
    if i>=n and j<m:
        print "MechaGodzilla"
    elif j>=m and i<n:
        print "Godzilla"
    else:
        print "uncertain"





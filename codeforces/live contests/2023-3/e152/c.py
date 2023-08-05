import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
st position, number of 0's AFTER a 1
count how many extra 0's are fixated from a
position
if 1, no sub, else sub number of chained 0's
use bin ar to get num of 0's


010, 1 3 and 2 3 queries should be same
"""
def create_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = s[prevrow][i]+s[prevrow][i+dist//2]
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s

def exact_query(l: int, h: int, ar: list):
    #find sum of range
    length = h-l+1
    s = str(bin(length))[2:]
    two = len(s)
    pt = l
    ans = 0 
    for i in range(two):
        if s[i] == "1":
            ans += ar[two-i-1][pt]
            pt += 2**(two-i-1)
    return ans



for i in range(readint()):
    n,m = readints()
    s = input()
    ar = list()
    for snth in range(n):
        ar.append(int(s[snth]))
    br = [0]*n
    c = 999999999999999
    for k in range(n):
        if ar[-k-1] == 1: c = n-k-1
        br[-k-1] = c
    cr = create_sparse(ar)
    d = {}
    
    for j in range(m):
        a,b = readints()
        a = br[a-1]
        b -= 1
        if a >= b: d[0] = 1
        else:
            f = b-a+1-exact_query(a,b,cr)
            if f == 0: d[0] = 1
            else: d[(a,f)] = 1
    #print(br)
    #print(cr)
    print(len(d.keys()))
    #print(d.keys())
    

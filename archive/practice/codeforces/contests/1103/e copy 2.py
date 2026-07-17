import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
for a given subarray, there has to be two other subarrays that
could work

sliding windows can be possible
determine if a subarray is good by min/max check and unique val count

binary searching is NOT possible

O(n^3 log n) on technicality, this definitely is faster than implied

brute force every valid subarray, store in some sort of dict by (length,min val)
and track lowest/highest possible starting positions

run this whole shitshow but with intentionally only searching storing specific subarray lengths
one at a time
"""

def f(n,ar,x,minseg,maxseg):
    wtf = list()
    lowdict = {} # now stores (low,high) in a tuple format

    count = 0 # number of unique
    seg = [0]*(n+1)
    for i in range(x-1):
        if sega[ar[i]] == 0: count += 1
        sega[ar[i]] += 1
    
    for i in range(n):
        d = set()
        minv,maxv = 9999,-9999
        for j in range(i,min(n,i+n//2+1)):
            if ar[j] in d: # dup found
                break
            d.add(ar[j])
            minv = min(minv,ar[j])
            maxv = max(maxv,ar[j])
            if maxv-minv == j-i:
                key = (j-i+1)*6050+minv
                if lowdict.get(key) == None:
                    lowdict[key] = i*6051
                    wtf.append(key)
                else:
                    lowdict[key] -= lowdict[key]%6050
                    lowdict[key] += i
    ans = 0
    wtf.sort()
    wtf.reverse()
    for k in wtf:
        v = lowdict[k]
        vl,vh = v//6050,v%6050
        a,b = k//6050,k%6050
        if b > a and lowdict.get(k-a) != None:
            z = lowdict[k-a]
            zl,zh = z//6050,z%6050
            if vh-zl >= a or zh-vl >= a:
                ans = a
                break
        if (a+a+b-1) <= n and lowdict.get(k+a) != None:
            z = lowdict[k+a]
            zl,zh = z//6050,z%6050
            if vh-zl >= a or zh-vl >= a:
                ans = a
                break
    anslist.append(ans)


 
anslist = list()
for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    for why in range(n//2,-1,-1):
        if f(n,ar,why):
            ans = why
            break
    anslist.append(why)

    
sys.stdout.write("\n".join(map(str,anslist)))
        
        
            

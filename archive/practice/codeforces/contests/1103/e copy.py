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
"""

anslist = list()
hv = 7234587
for _ in range(readint()):
    n = readint()
    ar = readar()
    wtf = list()
    lowdict = {} # now stores (low,high) in a tuple format
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
                key = ((j-i+1)*6050+minv)^hv
                if lowdict.get(key) == None:
                    lowdict[key] = i*6051
                    wtf.append(key)
                else:
                    lowdict[key] -= lowdict[key]%6050
                    lowdict[key] += i
    ans = 0
    for kk in wtf:
        
        v = lowdict[kk]
        vl,vh = v//6050,v%6050
        k = kk ^ hv
        a,b = k//6050,k%6050
        ta,tb = (k-a)^hv,(k+a)^hv
        if b > a and lowdict.get(ta) != None:
            z = lowdict[ta]
            zl,zh = z//6050,z%6050
            if vh-zl >= a or zh-vl >= a:
                ans = max(ans,a)
        if (a+a+b-1) <= n and lowdict.get(tb) != None:
            z = lowdict[tb]
            zl,zh = z//6050,z%6050
            if vh-zl >= a or zh-vl >= a:
                ans = max(ans,a)
    anslist.append(ans)
    
sys.stdout.write("\n".join(map(str,anslist)))
        
        
            

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
has to be AT LEAST P
limit of P is 5, anything past that is not needed
6**5 needed states -> 7776

in base p+1 notation, lowest bit is first val
2nd lowest is second val, etc

F is some next level stuff, might be involving a seg tree?
"""
n,k,p = readints()
sc = (p+1)**k
dp = [999999999999999]*sc
dp[0] = 0
#print(sc)
def inc(v,k,p,ar):
    #print("v",v)
    br = list()
    reindex = 0
    for i in range(k):
        nv = min((v%(p+1))+ar[i+1],p)
        v //= (p+1)
        reindex += nv*((p+1)**i)
    #print(reindex)
    return reindex
    

for i in range(n):
    ar = readar()
    newdp = [999999999999999]*sc
    for j in range(sc):
        if dp[j] != 999999999999999:
            newdp[j] = min(newdp[j],dp[j]) #no change
            ri = inc(j,k,p,ar)
            newdp[ri] = min(newdp[ri],dp[j]+ar[0]) #use dev plan
    dp = newdp
if dp[-1] == 999999999999999: print(-1)
else: print(dp[-1])
    

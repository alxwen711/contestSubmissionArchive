import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
binary searching for optimal value in the dp???

segment racing with values?


given set of segments each with values,
find a set that produces the maximum total sum

implementation here is wrong in assuming the segments cannot overlap
segments just can't cover other centers.

probably needs two dp array setups to tackle each condition
multiple possible options?
"""

def create_seg(n):
    seg = list()
    tmp = [0]*n
    seg.append(tmp)
    while len(seg[-1]) != 1:
        tmp = [0]*(len(seg[-1])//2)
        seg.append(tmp)
    return seg

def update(seg,index,x):
    i = index
    seg[0][i] = x
    for j in range(1,len(seg)):
        i //= 2
        try:
            seg[j][i] = max(seg[j-1][i*2],seg[j-1][i*2+1])
        except:
            break

def query(seg,li,ri):
    l,r = li,ri
    ans = 0
    for i in range(len(seg)):
        if l > r: return ans
        if l % 2 == 1:
            ans = max(ans,seg[i][l])
            l += 1
        if r % 2 == 0:
            ans = max(ans,seg[i][r])
            r -= 1
    return ans
        

for _ in range(readint()):
    n = readint()
    ar = readar()
    dp = create_seg(n+1)
    segments = list()
    for i in range(len(ar)):
        segments.append((min(n,i+ar[i]+1),max(0,i-ar[i]),ar[i])) # end point, start point, value
    segments.sort()
    for s in segments:
        prior = query(dp,0,s[1]-1) # total possible score from before segment
        val = prior+s[2]
        target = s[0]
        updateval = max(val,query(dp,0,target-1))
        if dp[0][target] < updateval:
            update(dp,target,updateval)
    ans = max(dp[0])
    bans = 0
    for u in range(n):
        bans = max(bans,dp[0][u])
        ans = max(ans,bans+ar[u])
    tmpans = ans
    ar.reverse()    
    dp = create_seg(n+1)
    segments = list()
    for i in range(len(ar)):
        segments.append((min(n,i+ar[i]+1),max(0,i-ar[i]),ar[i])) # end point, start point, value
    segments.sort()
    for s in segments:
        prior = query(dp,0,s[1]-1) # total possible score from before segment
        val = prior+s[2]
        target = s[0]
        updateval = max(val,query(dp,0,target-1))
        if dp[0][target] < updateval:
            update(dp,target,updateval)
    ans = max(dp[0])
    bans = 0
    for u in range(n):
        bans = max(bans,dp[0][u])
        ans = max(ans,bans+ar[u])
    print(max(ans,tmpans))

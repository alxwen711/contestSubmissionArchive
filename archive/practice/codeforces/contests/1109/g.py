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
    ans = -9
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
    dp = create_seg(n)
    finish = 0
    for i in range(n):
        if i != 0:
            # consider the do nothing option
            if dp[0][i-1] > dp[0][i]:
                update(dp,i,dp[0][i-1])
        # try taking the value
        baseval = ar[i]
        if i > baseval:
            baseval += query(dp,0,i-baseval-1)
        endpoint = min(n,i+ar[i]+1)
        #if endpoint == n:
        finish = max(finish,ar[i]+query(dp,0,i))
        if endpoint != n:
            if baseval > dp[0][endpoint]:
                update(dp,endpoint,baseval)
        print(dp,finish)
    print(max(max(dp[0]),finish))


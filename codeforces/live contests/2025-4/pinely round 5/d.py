import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
no subsequence of x, x+1 can exist
some sort of dp by order of the values

lemma: if value x is used at pos p, then
any x at a pos over p must be used in the optimal solution?

1112333333332121

8 6 4 2 4 1 2 8 is currently wrong

for each x+1 segment, only the first x+1 chosen needs to be tracked
then for each first x+1, find the best tailing x+1 depending on dp[x]
"""


for _ in range(readint()):
    n = readint()
    ar = readar()
    d = list()
    for _ in range(n+1):
        tmp = list()
        d.append(tmp)
    for i in range(n):
        d[ar[i]].append(i)
    index = [-1]
    dp = [0]
    mv = [0]
    best = 0
    #print(d)
    for i in range(1,n+1):
        d[i].insert(-1,0) # 0 case
        nindex = list()
        ndp = list()
        ptr = 0
        for j in range(len(d[i])):
            inc = j
            while d[i][j] < index[ptr]:
                ptr += 1
            nindex.append(d[i][j])
            ndp.append(inc+mv[ptr])
        best = max(best,mv[0])
        ndp[-1] = best
        index = nindex
        dp = ndp
        # recompute mv
        mv = [0]*len(dp)
        mv[-1] = best
        for k in range(len(dp)-2,-1,-1):
            mv[k] = max(mv[k+1],dp[k])
        print(i,index,dp,mv)
    print(n-max(dp))
        

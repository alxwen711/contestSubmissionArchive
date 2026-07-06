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

compute the dp values first assuming only one value is placed
"""


for _ in range(readint()):
    n = readint()
    ar = readar()
    d = list()
    for _ in range(n+1):
        tmp = []
        d.append(tmp)
    for i in range(n):
        d[ar[i]].append(i)
    index = [n]
    dp = [0]
    best = 0
    #print(d)
    for i in range(1,n+1):
        nindex = []
        ndp = []
        #d[i].append(n) # 0 case
        ptr = 0
        for j in range(len(d[i])):
            while d[i][j] > index[ptr]:
                ptr += 1
            nindex.append(d[i][j]) # pseudo end position
            ndp.append(max(dp[ptr],dp[-1])+1)

        # add the full ignore case
        nindex.append(n)
        ndp.append(max(dp))    
        
        # backwards propogate
        best = dp[-1]
        for k in range(len(ndp)-2,-1,-1):
            best = max(best+1,ndp[k])
            ndp[k] = best

        

        dp = ndp
        index = nindex
        #print(i,index,dp)
    print(n-max(dp))
    
        

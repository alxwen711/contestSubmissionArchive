import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
track each state in tuples
"""

n,l = readints()
words = list()
for _ in range(n):
    s = readin()
    grid = list()
    for _ in range(len(s)):
        grid.append([0]*26)
    for i in range(len(s)):
        for j in range(26):
            if ord(s[i])-97 == j: grid[i][j] = i+1
            else: # construct?
                word = s[:i]+chr(j+97)
                for k in range(i,-1,-1):
                    if word[i+1-k:i+1] == s[:k]:
                        grid[i][j] = k
                        break
    words.append(grid)
dp = {}
dp[0] = 1
m = 998244353

for _ in range(l):
    ndp = {}
    for d in dp.keys():
        v = d
        decode = list()
        for _ in range(n):
            decode.append(v % 11)
            v //= 11
        decode.reverse()
        for p in range(26):
            v = 0
            for c in range(n):
                v *= 11
                if decode[c] != len(words[c]):
                    v += words[c][decode[c]][p]
                else: v += decode[c]
            if ndp.get(v) == None: ndp[v] = 0
            ndp[v] = (ndp[v]+dp[d]) % m
    dp = ndp
    #print(dp)
target = 0
for ii in range(len(words)):
    target *= 11
    target += len(words[ii])
if dp.get(target) == None: print(0)
else: print(dp[target])


                    

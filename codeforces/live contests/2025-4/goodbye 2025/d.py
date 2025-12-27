import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
a_i = h_i

there must be at least 1 fatality

everyone can go out assuming highest hp isn't absurdly high
minimize fatalities by having highest continually sending lowest to highest

at most n//2 can live

if n-1, do full cycle
if n, send lowest to highest until low enough, then cycle to end, then sd
else, then try doing pair sacks until 1 save needed, then full cycle residue
"""

for _ in range(readint()):
    n,m = readints()
    ar = readar() # all distinct
    br = list()
    for i in range(n):
        br.append((ar[i],i+1))
    br.sort()
    if m > n//2: print(-1)
    elif m == 0: # must full clear
        if n == 2: # don't bother with rest
            print(-1)
            continue
        xv = br[-1][0]
        ans = list()
        flag = False
        ptr = -1
        for i in range(n-2):
            if not flag:
                if xv-br[-2][0] <= br[i][0]:
                    flag = True
                    ptr = i
                else:
                    xv -= br[i][0]
                    ans.append((br[i][1],br[-1][1]))
            else:
                ans.append((br[i][1],br[i+1][1]))
        ans.append((br[-2][1],br[-1][1]))
        if flag:
            ans.append((br[-1][1],br[ptr][1]))
            print(len(ans))
            for snth in ans:
                print(snth[0],snth[1])
        else: print(-1)
    else: # use pairup system until only 1 left, then full cycle
        ans = list()
        for i in range(m-1):
            ans.append((br[2*i+1][1],br[2*i][1]))
        for j in range(2*m-2,n-1):
            ans.append((br[j+1][1],br[j][1]))
        print(len(ans))
        for snth in ans:
            print(snth[0],snth[1])

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ar is the final time sitting array
time 0 -> a_i = 0
otherwise -> a_i <= number of sitting down previous time AND someone besides

process in order of time, determine minimal and maximal totals

maximum -> number that were sitting down at previous time
minimum -> normally people sitting time t-2 plus 1
if neighbour(s) sitting at t-1, could be 0
if literally no neighbours, impossible

"""

mod = 676767677


def solve(n,m,ar):
    br = list()
    for _ in range(m):
        tmp = list()
        br.append(tmp)
    for i in range(n):
        br[ar[i]].append(i)
    tc = [0]*m
    ans = 1

    # 0 case
    tc[0] = len(br[0])
    h = [9999999999999]*n
    for b in br[0]:
        h[b] = 0

    for k in range(1,m):
        tc[k] = tc[k-1]
        ma = tc[k-1]
        for l in br[k]:
            tc[k] += 1
            hh = 9999999999999
            if l != 0: hh = min(hh,h[l-1])
            if l != n-1: hh = min(hh,h[l+1])
            if hh == 9999999999999: return 0
            elif hh == k-1:
                ans = (ans*ma) % mod # 0 is not allowed
            else:
                
                mi = tc[k-2]+1
                if k == 1: mi = 1
                #print(mi,ma)
                ans = (ans*(ma-mi+1)) % mod
        for l in br[k]:
            h[l] = k
        #print(ans,h)
    return ans
            
for _ in range(readint()):
    n,m = readints()
    ar = readar()
    print(solve(n,m,ar))

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# 111*11 = 1221, anything 1221 or higher will auto pass

dp = [0]*1221
dp[0] = 1
for j in range(1,1221):
    flag = False
    if j >= 11:
        if dp[j-11] == 1: flag = True
    if j >= 111:
        if dp[j-111] == 1: flag = True
    if flag: dp[j] = 1
    
for i in range(readint()):
    n = readint()
    if n >= 1221: print("YES")
    else: print("YES" if dp[n] == 1 else "NO")

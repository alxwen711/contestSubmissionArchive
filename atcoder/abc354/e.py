import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
too many possible games to true brute force
all states can be tracked 2**18 < 1 mil
if each pair is emulated, at most 40 mil scenarios
"""

def f(n,ar,dp,i,two):
    x = i
    one = 0
    while x != 0:
        one += x % 2
        x //= 2
    if (n-one) % 2 == 1: return -1 # literally impossible
    turns = (n-one)//2
    player = turns % 2 # 0 for T, 1 for A
    if turns == n//2: return player ^ 1 # not enough cards
    # search for winning position
    for a in range(n-1):
        for b in range(a+1,n):
            if (i & two[a]) and (i & two[b]) and (ar[a][0] == ar[b][0] or ar[a][1] == ar[b][1]):
                if dp[i-two[a]-two[b]] == player: return player
    return player ^ 1

n = readint()
two = [1]
for _ in range(n):
    two.append(two[-1]*2)
ar = list()
for _ in range(n):
    a,b = readints()
    ar.append((a,b))
dp = [-1]*(2**n)
for i in range(2**n):
    dp[i] = f(n,ar,dp,i,two)
if dp[-1] == 0: print("Takahashi")
else: print("Aoki")

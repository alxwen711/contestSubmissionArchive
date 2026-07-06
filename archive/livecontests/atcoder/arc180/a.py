import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
some sort of dp? dup cases are possible
  B  B  A  B  A  B  A  A  B  A  B  A  A  A  A  B  A
above has chain lengths 1,6,5,1,1,3

BAB -> 2
BABA -> 2
BABAB -> 3

ABA -> 2
ABAB -> 2
ABABA -> 3 ABABA,ABA,A
"""


n = readint()
s = readin()
ans = 1
m = 1000000007
chain = 1
prev = s[0]
for i in range(1,n):
    if prev == s[i]:
        ans *= (chain+1)//2
        ans = ans % m
        chain = 1
    else: chain += 1
    prev = s[i]
ans *= (chain+1)//2
ans = ans % m
print(ans)        

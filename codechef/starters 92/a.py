import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
k = 3, every 3 stones have 1 of each colour?
then after this it must follow the pattern
"""
for i in range(readint()):
    n,k = readints()
    ans = 1
    x = k
    for j in range(n):
        ans = (ans*x) % 1000000007
        x -= 1
        if x == 0: break
    print(ans)
    
    

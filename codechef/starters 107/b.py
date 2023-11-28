import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
goal is to make x % k and (n-x) % k as close in value as possible
x could be n//2 (in cases where n <= 2k)

"""

for _ in range(readint()):
    n,k = readints()
    choices = [n//2-2,n//2-1,n//2,n//2+1,n//2+2,
               (n+k)//2-2,(n+k)//2-1,(n+k)//2,(n+k)//2+1,(n+k)//2+2]
    ans = -1
    score = -100
    for x in choices: #can only test up to N
        x = x % k
        if x <= n:
            s = (x % k) * ((n-x) % k)
            if s > score:
                score = s
                ans = x
    print(ans)

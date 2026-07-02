import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
add 1 or div by x (with round down)
feels like most cases should involve dividing by x first
"""


for _ in range(readint()):
    a,b,x = readints()
    ans = abs(a-b)
    v = 0
    while a != 0 or b != 0:
        if a > b:
            a //= x
        else:
            b //= x
        v += 1
        ans = min(ans,abs(a-b)+v)
    print(ans)

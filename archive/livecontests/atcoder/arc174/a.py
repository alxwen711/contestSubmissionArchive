import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 -> nothing
0 or negative -> most negative result
2+ -> most positive result
"""

n,c = readints()
ar = readar()
t = sum(ar)
if c > 1:
    b = 0
    ans = 0
    for i in ar:
        b = max(b+i,i)
        ans = max(b,ans)
    t += (ans*(c-1))
elif c < 1:
    b = 0
    ans = 0
    for i in ar:
        b = min(b+i,i)
        ans = min(b,ans)
    t += (ans*(c-1))
print(t)

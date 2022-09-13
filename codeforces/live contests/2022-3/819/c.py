import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
()()() -> 1
(()()) -> 2
not max depth
not 0 count
1 + # of moves to reach ()()()...
"""

for i in range(readint()):
    n = readint()
    s = input()
    ans = n+1
    for j in range(n*2-1):
        if s[j] == "(" and s[j+1] == ")": ans -= 1
    print(ans)

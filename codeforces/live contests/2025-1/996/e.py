import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
once a stack has been searched, optimal to move later to that stack
shortest stack does not always work

keep track of number of dummies

is there a dp way of choosing the optimal searching order?
(probably because greedy on largest cap/shortest init stack fails)
"""

for _ in range(readint()):
    n = readint()
    stacks = list()
    for _ in range(n):
        a,b = readints()
        heappush(stacks,(-b,a))
    space = 0
    ans = 0
    while len(stacks) != 0:
        x = heappop(stacks)
        ans += x[1]
        space -= x[1]
        if space < 0: ans -= space
        if len(stacks) == 0 and space < 0:
            ans = -1
            break
        space -= x[0]
    print(ans)

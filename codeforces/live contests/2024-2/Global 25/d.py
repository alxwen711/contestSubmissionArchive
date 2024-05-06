import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if alice has 24 coins:
1
2
3
4
5
6
7
8
9
10 -> 15 1
11 -> 14 1
12 -> 2
13 -> no?
14 -> no?
15 -> no?
16 -> no?
17 -> no?
18 -> no?
19 -> no?
20 -> no?
21 -> no?
22 -> no?
23 -> no?
24 -> 1
"""

def solve(n,k):
    if n == k:
        print("YES")
        print(1)
        print(1)
    elif n < k:
        print("NO")
        return
    elif (n+1)//2 >= k:
        print("YES")
        print(2)
        print(n-k+1,1)
    else:
        print("NO")
        return

for _ in range(readint()):
    n,k = readints()
    solve(n,k)

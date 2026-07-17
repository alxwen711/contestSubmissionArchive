import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
brute force several possible cases
"""

def f(s,n):
    h = [1]*n
    for k in range(n):
        if s[k] == "L":
            for a in range(k+1,n):
                h[a] += 1
        else:
            for b in range(k):
                h[b] += 1
    return h


n = 2

s = [""]
for _ in range(n):
    ns = list()
    for i in s:
        ns.append(i+"L")
        ns.append(i+"R")
    s = ns
ar = list()
for i in s:
    ar.append((f(i,n),i))
ar.sort()
for i in ar:
    print(i)
    

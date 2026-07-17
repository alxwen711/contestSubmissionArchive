import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the answer always includes the entire string
n is at most 5000, technically could just brute force here
"""

for _ in range(readint()):
    s = readin()
    n = len(s)
    l = -1
    for i in range(n):
        if s[i] == "0":
            l = n-i # optimal will be this length
            break
    if l == -1: print(1,n,1,1) # all 1
    else:
        base = int(s,base=2)
        index = -1
        best = -1
        for j in range(n-l+1):
            if s[j] == "1":
                v = int(s[j:j+l],base=2)
                h = base ^ v
                if h > best:
                    index = j
                    best = h
        print(1,n,index+1,index+l)    

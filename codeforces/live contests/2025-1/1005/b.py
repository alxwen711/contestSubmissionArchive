import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
232323456232323 -> 15-5
232323232323 -> 12-2

keep anything that shows up twice

eliminate the longest continuous chain of unique values
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    h = [-1]*(n+1)
    for i in range(n):
        if h[ar[i]] == -1: h[ar[i]] = i
        else: h[ar[i]] = -2
    br = list()
    for j in range(n+1):
        if h[j] >= 0: br.append(h[j])
    if len(br) == 0: print(0)
    else:
        hel = [0]*(n+1)
        for b in br:
            hel[b] = 1
        chain = 0
        start = -1
        ans = 0
        base = -1
        for k in range(n+1):
            if hel[k] == 1:
                if chain == 0: start = k
                chain += 1
            else:
                if chain > ans:
                    ans = chain
                    base = start
                chain = 0
        if chain > ans:
            ans = chain
            base = start
        print(base+1,base+ans)
        




                

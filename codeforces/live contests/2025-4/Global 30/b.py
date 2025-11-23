import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
two even vals -> even
two odd vals -> even?
assume that for some number of values, a pair must exist with non 0 chance?
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    odd,even = list(),list()
    for i in ar:
        if i % 2 == 0: even.append(i)
        else: odd.append(i)
    if len(even) >= 2: print(even[0],even[1])
    elif len(ar) <= 200:
        # try brute force
        flag = False
        for i in range(n-1):
            for j in range(i+1,n):
                if (ar[j] % ar[i]) % 2 == 0:
                    flag = True
                    print(ar[i],ar[j])
                    break
            if flag: break
        if not flag: print(-1)
    else:
        # assume a solution must exist for some reason
        flag = False
        for i in range(n-1):
            if (ar[i+1] % ar[i]) % 2 == 0:
                flag = True
                print(ar[i],ar[i+1])
                break
        if not flag: print(-1)

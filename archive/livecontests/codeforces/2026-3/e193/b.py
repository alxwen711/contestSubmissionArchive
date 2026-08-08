import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
try to choose a chain of 4 in which a a b b is the pattern (+2)
if not then aabc or cabb (+1) or xaay
else no swap would work
deal with length 3 case separately
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(2 if ar[0] != ar[1] else 1)
        continue
    if n == 3:
        if ar[0] == ar[1] and ar[1] == ar[2]: print(1)
        else: print(3)
        continue
    flag = True
    for i in range(n-3):
        if ar[i] == ar[i+1] and ar[i+2] == ar[i+3] and ar[i+1] != ar[i+2]:
            ar[i+1],ar[i+2] = ar[i+2],ar[i+1]
            flag = False
            break
    if flag:
        f2 = True
        for i in range(n-3):
            if ar[i] == ar[i+1] and ar[i+1] != ar[i+3] and ar[i+1] != ar[i+2]:
                ar[i+1],ar[i+2] = ar[i+2],ar[i+1]
                f2 = False
                break
            elif ar[i+2] == ar[i+3] and ar[i+1] != ar[i+3] and ar[i] != ar[i+2]:
                ar[i+1],ar[i+2] = ar[i+2],ar[i+1]
                f2 = False
                break
        # run specific cases at the edges that are not considered
        if f2:
            if ar[1] == ar[2] and ar[0] != ar[1]:
                ar[0],ar[1] = ar[1],ar[0]
            elif ar[-3] == ar[-2] and ar[-1] != ar[-2]:
                ar[-1],ar[-2] = ar[-2],ar[-1]
            
             
    ans = 0
    prev = -29873
    for j in ar:
        if j != prev: ans += 1
        prev = j
    print(ans)

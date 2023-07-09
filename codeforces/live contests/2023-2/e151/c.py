import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
greedy select the last possible option
"""

def solve(s,n,mi,ma):
    minar = [0]*n
    maxar = [0]*n
    for i in range(n):
        minar[i] = int(mi[i])
        maxar[i] = int(ma[i])
    nn = len(s)
    ar = list()
    for j in range(nn):
        ar.append(int(s[j]))
    index = -1
    h = [0]*10
    r = 0
    for k in range(nn):
        if r == 0:
            index += 1
            if index == n: return "NO" #used all password digits
            r = maxar[index]-minar[index]+1
            for l in range(minar[index],maxar[index]+1):
                h[l] = 1
        x = ar[k]
        if h[x] == 1:
            h[x] = 0
            r -= 1
    if r == 0: index += 1
    if index == n: return "NO"
    return "YES"

for i in range(readint()):
    s = input()
    n = readint()
    mi = input()
    ma = input()
    print(solve(s,n,mi,ma))

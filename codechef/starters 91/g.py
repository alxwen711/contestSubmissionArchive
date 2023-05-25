import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def f(cr,j,n):
    best = max(j,n-j-1)
    index = 0
    v = j
    t = -100
    while index != n:
        if t < cr[index][0]: t = cr[index][0] + 1
        if cr[index][1] < j: v -= 1
        elif cr[index][1] > j: v += 1
        index += 1
        if v > best: best = v
    return best
        

for i in range(readint()):
    n = readint()
    ar = readar()
    inv = [0]*n
    ans = 0
    cr = list()
    for x in range(len(ar)):
        cr.append((ar[x],x))
    cr.sort()
    for a in range(n):
        for b in range(a+1,n):
            if ar[a] > ar[b]:
                ans += 1
                inv[a] += 1
                inv[b] += 1
    br = list()
    for j in range(n):
        br.append(ans-inv[j]+f(cr,j,n))
    #print(*inv)
    print(*br)

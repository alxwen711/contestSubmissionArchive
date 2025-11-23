import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
add 0/1 each time (also return an actual program)
entering min/max, exiting min/max
keep track of the min height req?
can we process this backwards

1 4
0 3 -> 2 3
1 3 -> 1 2
0 2 -> 0 0 (always 0 0)


0 0
0 2
1 2
2 3
1 4


0 3
-1 3 -> 2 2
1 2 -> 1 1 (cannot start on 0)
1 1 -> 0 0 (impossible)
"""

def solve(n,ar,ranges):
    mi = [ranges[-1][0]]
    ma = [ranges[-1][1]]
    ranges.reverse()
    ranges.append((0,0))
    ar.reverse()
    for i in range(n):
        if ar[i] != -1:
            mi.append(max(mi[-1]-ar[i],ranges[i+1][0]))
            ma.append(min(ma[-1]-ar[i],ranges[i+1][1]))
        else:
            mi.append(max(mi[-1]-1,ranges[i+1][0]))
            ma.append(min(ma[-1],ranges[i+1][1]))
        if mi[-1] > ma[-1]:
            print(-1)
            return
    sc = 0
    entries = list()
    ranges.reverse()
    mi.reverse()
    ma.reverse()
    ar.reverse()
    #print(mi,ma)
    for i in range(n):
        if ar[i] == -1: entries.append(i)
        elif ar[i] == 1: sc += 1
        diff = max(0,mi[i+1]-sc)
        for _ in range(diff):
            try:
                x = entries.pop()
                ar[x] = 1
                sc += 1
            except:
                print(-1)
                return
    for snth in range(n):
        if ar[snth] == -1: ar[snth] = 0
    print(*ar)

for _ in range(readint()):
    n = readint()
    ar = readar()
    ranges = list()
    for _ in range(n):
        l,r = readints()
        ranges.append((l,r))
    solve(n,ar,ranges)

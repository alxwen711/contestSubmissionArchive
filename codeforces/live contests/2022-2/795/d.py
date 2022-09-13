import sys
#if no consecutive positive, then group negatives, sum 3
#1,-7,5,-2,2,-2,3?
#if sum drops below 0, restart sum
def solve(n,ar):
    br = list()
    neg = 0
    flag = False
    for a in range(n):
        x = ar[a]
        if x < 0:
            neg += x
        elif x > 0:
            if neg < 0:
                br.append(neg)
                neg = 0
            elif flag: return "NO"
            else: flag = True
            br.append(x)
    if neg < 0: br.append(neg)
    if br[0] < 0: br.pop(0)
    if br[-1] < 0: br.pop(-1)
    if len(br) < 3: return "YES"
    restart = True
    s = 0
    m = -999999999999999999
    for b in range(len(br)):
        x = br[b]
        if restart:
            restart = False
            s = 0
            m = -99999999999999
        s += x
        if x > m: m = x
        if s > m: return "NO"
        elif x == m: s = m
    return "YES"

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    print(solve(n,ar))

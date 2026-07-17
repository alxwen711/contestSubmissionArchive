import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
add 2nd smallest from each while tracking min across all
add lowest val, sub min 2nd smallest
"""
for i in range(readint()):
    n = readint()
    #ar = list()
    sl = 9999999999999
    l = 9999999999999
    ans = 0
    for j in range(n):
        m = readint()
        tmp = readar()
        #ar.append(tmp)
        tmp.sort()
        x = tmp[1]
        ans += x
        sl = min(sl,x)
        l = min(l,tmp[0])
    ans -= sl
    ans += l
    print(ans)

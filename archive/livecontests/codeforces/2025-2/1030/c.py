import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
compute the fastest line to having more bits added

1000101010110
-> find least significant 1 bits, add into incrementing list
"""
for _ in range(readint()):
    n,k = readints()
    ar = readar()
    bc = [0]*100
    ans = 0
    for i in ar:
        for j in range(100):
            if i % 2 == 0:
                bc[j] += 1
            else: ans += 1
            i //= 2
    for s in range(100):
        if k >= (2**s)*bc[s]:
            ans += bc[s]
            k -= (2**s)*bc[s]
        else:
            ans += (k//(2**s))
            break
    print(ans)

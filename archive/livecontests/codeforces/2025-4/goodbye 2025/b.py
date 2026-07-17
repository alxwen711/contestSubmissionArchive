import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
any char that does not follow this -> change to s?
"""

for _ in range(readint()):
    r = readin()
    n = len(r)
    ar = list()
    for snth in r:
        ar.append(snth)
    prev = -9999999
    ans = 0
    for i in range(n):
        if ar[i] == "s": prev = i
        else:
            index = 2*i-prev
            if index >= n:
                ans += 1
                prev = i # assume this is a s
                ar[prev] = "s"
            elif r[index] == "u":
                ans += 1
                ar[index] = "s"
    print(ans)

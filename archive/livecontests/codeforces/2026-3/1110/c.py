import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
4th case fails due to 8 bit not being changable
(only bits up to n can be changed)
the mex can only increase
last mex will always be n
greedily try to shove as many bits as possible;
if not enough spaces, then this is impossible
"""

for _ in range(readint()):
    n,k = readints()
    target = n ^ k
    bits = list()
    v = 1
    while target != 0:
        if target % 2 == 1:
            bits.append(v)
        target //= 2
        v *= 2
    bits.reverse()
    prev = n
    if len(bits) == 0:
        print("YES")
        ans = [n-i-1 for i in range(n)]
        print(*ans)
    elif bits[0] >= n:
        print("NO")
    else: # greedily get minimal setup
        prev = n
        chain = list()
        c = 0
        for l in bits:
            if c+l >= prev:
                prev = c
                chain.append(c)
                c = 0
            c += l
        chain.append(c)
        chain.append(0)
        if len(chain) > n: print("NO")
        else:
            print("YES")
            chain.reverse()
            h = [1]*n
            for cc in chain:
                h[cc] = 0
            ans = list()
            for snth in range(n):
                if h[snth] == 1: ans.append(snth)
            for u in chain:
                ans.append(u)
            print(*ans)
        

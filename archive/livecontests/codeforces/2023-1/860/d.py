import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
absolute sum of any subarray in permutation must be less than max-min
"""
def solve(n,ar,ll,hl):
    a,b = 0,n-1
    s = 0
    ans = list()
    neg = True
    f = 0
    while b-a >= 0:
        if neg:
            t = s+ar[a]
        else:
            t = s+ar[b]
        if t < ll or t > hl:
            f += 1
            neg = neg ^ True
        else:
            f = 0
            s = t
            if neg:
                ans.append(ar[a])
                a += 1
            else:
                ans.append(ar[b])
                b -= 1
        if f == 2: return -1
    return ans

for i in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    if ar[0] == 0: print("No")
    else:
        ans = solve(n,ar,ar[0],ar[-1]-1)
        if ans != -1:
            print("Yes")
            print(*ans)
        else:
            ans = solve(n,ar,ar[0]+1,ar[-1]-1)
            if ans != -1:
                print("Yes")
                print(*ans)
            else: print("No")

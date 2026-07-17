import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    br = list(map(int,sys.stdin.readline().split()))
    cr = list(map(int,sys.stdin.readline().split()))
    h = [0]*(n+1)
    lc = 0
    a = {}
    for k in range(n):
        a[ar[k]] = k
    for j in range(n):
        x = ar[j]
        if h[x] == 0 and ar[j] != br[j]:
            #det loop
            lc += 1
            pt = j
            while h[ar[pt]] == 0:
                h[ar[pt]] = lc
                pt = a[br[pt]]
    loops = [1]*lc
    for m in range(n):
        if cr[m] != 0:
            if h[ar[m]] != 0: loops[h[ar[m]]-1] = 0
    ans = 1
    for f in range(sum(loops)):
        ans *= 2
        ans = ans % 1000000007 
    print(ans)
    

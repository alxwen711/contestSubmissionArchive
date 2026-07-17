import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# track all possible values by their frequency

n = readint()
ar = readar()
d = [0]*200000
#d = {}
d[ar[1]+100000] = 1
br = list()
br.append(ar[1]+100000)
m = 998244353
for i in range(n-2):
    nv = ar[i+2]
    #nt = {}
    #br = list(d.keys())
    nt = [0]*200000
    cr = list()
    for j in range(len(br)):
        x = br[j]-100000
        if x == 0: #adjust to mod and encode after
            a = nv+100000
            if nt[a] == 0: cr.append(a)
            nt[a] = (nt[a]+d[100000]) % m
        else:
            a = nv+x+100000
            b = nv-x+100000
            if nt[a] == 0: cr.append(a)
            nt[a] = (nt[a]+d[br[j]]) % m
            if nt[b] == 0: cr.append(b)
            nt[b] = (nt[b]+d[br[j]]) % m
    d = nt
    br = cr
ans = 0
for k in range(len(br)):
    ans += d[br[k]]
print(ans % m)

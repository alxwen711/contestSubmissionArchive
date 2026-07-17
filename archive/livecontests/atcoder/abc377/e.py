import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
3 4 2 1
2 1 4 3
1 2 3 4
1 2 3 4

cylicals probably break after 30+ manual transmissions
but then it gets kinda fricky since it's not a pure cylical
"""
n,k = readints()
ar = readar()
ans = [0]*n

for snth in range(min(k,1000)):
    br = list()
    for ss in range(n):
        br.append(ar[ar[ss]-1])
    ar = br
k = k-1000
if k < 0: k = 0
if k != 0:
    for i in range(n):
        if ans[i] == 0: # compute cycle
            vals = list()
            indices = list()
            index = i
            d = {}
            while d.get(index) == None:
                indices.append(index)
                vals.append(ar[index])
                d[index] = 1
                index = ar[index]-1
                
            print(vals,indices)
            m = len(vals)
            for j in range(m):
                ans[indices[(j-k) % m]] = vals[j]

    print(*ans)
else:
    print(*ar)

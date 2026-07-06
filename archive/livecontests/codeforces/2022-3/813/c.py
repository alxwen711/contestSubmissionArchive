import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def freq_dict(ar, pos = False) -> dict:
    d = {}
    if ar == None: return d
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None:
            if pos: d[x] = list()
            else: d[x] = 0
        if pos: d[x].append(i)
        else: d[x] += 1
    return d


for i in range(readint()):
    n = readint()
    ar = readar()
    d = freq_dict(ar,True)
    #check that back is sorted and no gaps
    st = 10000000000
    endpt = n
    for j in range(n):
        x = ar[endpt-1]
        if x == st: endpt -= 1
        elif x > st: break
        else:
            dl = d[x]
            if dl[-1]-dl[0] == len(dl)-1:
                endpt -= 1
                st = x
            else: break
    h = [0]*(n+1)
    for k in range(endpt):
        if h[ar[k]] == 0: h[ar[k]] = 1
    print(sum(h))
    

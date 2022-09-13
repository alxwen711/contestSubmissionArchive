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
        if pos: d[x].append(i+1)
        else: d[x] += 1
    return d

for i in range(readint()):
    x = input()
    y = freq_dict(x,True)
    cost = abs(ord(x[-1])-ord(x[0]))
    ar = list()
    st = ord(x[0])
    end = ord(x[-1])
    inc = 1
    if st > end: inc = -1
    while True:
        if y.get(chr(st)) != None:
            a = y[chr(st)]
            for s in range(len(a)):
                ar.append(a[s])
        if st == end: break
        st += inc
    print(cost,len(ar))
    print(*ar)
    

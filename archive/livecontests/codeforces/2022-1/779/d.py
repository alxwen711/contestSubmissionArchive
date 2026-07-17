import sys
for i in range(int(sys.stdin.readline())):
    s,e = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    base = [0]*20
    res = [0]*20
    #calculate base
    for j in range(20):
        b = 2**j
        if e < j: break
        cycle = (e+1)//(2*b)
        base[j] += (b*cycle)
        f = (e+1) - (2*b*cycle)
        if f > b: base[j] += (f-b)
    s -= 1
    if s > 0:
        for n in range(20):
            b = 2**n
            if s < n: break
            cycle = (s+1)//(2*b)
            base[n] -= (b*cycle)
            f = (s+1) - (2*b*cycle)
            if f > b: base[n] -= (f-b)

    
    for k in range(20):
        cont = False
        for l in range(e-s):
            if ar[l] != 0:
                cont = True
                res[k] += (ar[l]%2)
                ar[l] = ar[l]//2
        if not cont: break
        
    ans = 0
    for m in range(20):
        if base[m] != res[m]: ans += 2**m
    print(ans)

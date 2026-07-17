import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,s1,s2 = readints()
    ar = readar()
    br = list()
    for j in range(n):
        br.append((ar[j],j+1))
    br.sort()
    br.reverse()
    ansa = list()
    ansb = list()
    ansa.append(0)
    ansb.append(0)
    a,b = s1,s2
    for k in range(n):
        x = br[k]
        if a > b:
            ansb.append(x[1])
            b += s2
        else:
            ansa.append(x[1])
            a += s1
    ansa[0] = len(ansa)-1
    ansb[0] = len(ansb)-1
    print(*ansa)
    print(*ansb)
    

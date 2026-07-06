import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def find(h,x):
    a = -1
    b = -1
    for i in range(len(h)):
        if h[i] == x:
            if a == -1: a = i
            else:
                b = i
                return a,b

def solve(n):
    if n == 2:
        print("! 1 2 2 1")
        flush()
        x = readint()
        return x
    #can create a line setup with (1+n), n queries
    print("+",n+1)
    flush()
    readint()
    print("+",n)
    flush()
    readint()
    line = list()
    for i in range((n+1)//2):
        line.append(n-i)
        line.append(i+1)
    if n % 2 == 1: line.pop()
    h = [0]*n
    for j in range(1,n):
        print("?",1,j+1)
        flush()
        x = readint()
        h[j] = x
    #print(h)
    m = max(h)
    ans = [0]*n
    ans[0] = line[n-m-1]
    #print(ans)
    dup = n-m-1
    if n % 2 == 1 and dup == n//2:
        #exact midpoint setup, fix special case
        re,ri = find(h,m)
        ans[ri] = line[0]
        ans[re] = line[-1]
        for snth in range(1,m):
            ia,ib = dup-snth,dup+snth
            a,b = find(h,snth)
            print("?",a+1,re+1)
            flush()
            x = readint()
            if n-1-dup+snth == x:
                ans[a] = line[ia]
                ans[b] = line[ib]
            else:
                ans[a] = line[ib]
                ans[b] = line[ia]

    else:
        re = -1
        for k in range(n):
            if h[k] > dup:
                ans[k] = line[dup+h[k]]
                if h[k] == m: re = k+1
        #print(ans)
        for l in range(1,dup+1):
            a,b = find(h,l)
            ia,ib = dup-l,dup+l
            print("?",a+1,re)
            flush()
            x = readint()
            if n-1-dup+l == x:
                ans[a] = line[ia]
                ans[b] = line[ib]
            else:
                ans[a] = line[ib]
                ans[b] = line[ia]
    #print(ans)
    #determine mirror setup
    d = {}
    for ii in range(len(line)):
        d[line[ii]] = line[-ii-1]
    rans = list()
    for v in range(n):
        rans.append(d[ans[v]])
    ans = ans + rans
    print("! ",end="")
    print(*ans)
    flush()
    x = readint()
    return x
    
    


for i in range(readint()):
    n = readint()
    x = solve(n)
    flush()
    if x == -2: break 

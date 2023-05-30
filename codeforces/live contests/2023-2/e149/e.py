import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
#arbritary order method?
def solve(n,ar):
    p = 2 ** n
    mod = 998244353
    fact = [1]*p
    for k in range(1,p):
        fact[k] = (fact[k-1]*k) % mod
    cr = list()
    cr.append(ar)
    for i in range(n):
        br = list()
        w = p//2
        for j in range(w):
            a,b = ar[2*j],ar[2*j+1]
            if a != -1 and b != -1:
                if min(a,b) > w or max(a,b) <= w: return 0
                br.append(min(a,b))
            elif a == -1 and b == -1:
                br.append(-1)
            elif max(a,b) > w:
                br.append(-1)
            else:
                br.append(max(a,b))
        cr.append(br)
        ar = br
        p //= 2

    ans = 1
    cr[-1][0] = 1
    p = 1
    for jj in range(n):
        #prev = cr[-jj-1]
        #dr = cr[-jj-2]
        # fill in winners,scan for losers
        loss = [1]*(p*2+3)
        for k in range(p):
            a,b,c = cr[-jj-2][2*k],cr[-jj-2][2*k+1],cr[-jj-1][k]
            if a != c and b != c:
                if a == -1 and b == -1:
                    ans = (ans*2) % mod
                    cr[-jj-2][2*k] = c
                elif a == -1:
                    cr[-jj-2][2*k] = c
                else:
                    cr[-jj-2][2*k+1] = c
            loss[a] = 0
            loss[b] = 0
        # loss range is p+1 to p*2
        #print(p+1,p*2)
        #print(loss)
        #print(cr[-jj-2])
        index = p+1
        lc = 0
        for m in range(p):
            while loss[index] == 0:
                index += 1
            a,b = cr[-jj-2][2*m],cr[-jj-2][2*m+1]
            if a == -1:
                lc += 1
                cr[-jj-2][2*m] = index
                loss[index] = 0
            if b == -1:
                lc += 1
                cr[-jj-2][2*m+1] = index
                loss[index] = 0
        ans = (ans*fact[lc]) % mod
        p *= 2
    #print(cr)
    return ans

n = readint()
ar = readar()
print(solve(n,ar))

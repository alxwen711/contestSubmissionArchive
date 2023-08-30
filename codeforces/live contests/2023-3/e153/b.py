import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    m,k,a,b = readints()
    if b != 0:
       # print(b,m//b)
        m -= (min(b,m//k)*k) #use normal k coins
    m -= min(m,a) #use normal 1 coins
    #print(m)
    ans = m//k+m%k
    if (m+a)//k > m//k: ans = min(ans,m//k+1)
    print(ans)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    a,b = readints()
    x,y = readints()
    xq,yq = readints()
    ar = {}
    br = {}
    ar[(x+a,y+b)] = 1
    ar[(x+a,y-b)] = 1
    ar[(x-a,y+b)] = 1
    ar[(x-a,y-b)] = 1
    ar[(x+b,y+a)] = 1
    ar[(x+b,y-a)] = 1
    ar[(x-b,y+a)] = 1
    ar[(x-b,y-a)] = 1
    br[(xq+a,yq+b)] = 1
    br[(xq+a,yq-b)] = 1
    br[(xq-a,yq+b)] = 1
    br[(xq-a,yq-b)] = 1
    br[(xq+b,yq+a)] = 1
    br[(xq+b,yq-a)] = 1
    br[(xq-b,yq+a)] = 1
    br[(xq-b,yq-a)] = 1
    ans = 0
    for i in ar.keys():
        if br.get(i) == 1: ans += 1
    print(ans)
    

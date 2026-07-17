import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    a,b,x,y = readints()
    if a == b: print(0)
    elif a > b: # can only do xor if possible
        if b % 2 == 0 and a-1 == b: print(y)
        else: print(-1)
    else:
        ans = 0
        for t in range(a,b):
            if t % 2 == 0: ans += min(x,y)
            else: ans += x
        print(ans)
        

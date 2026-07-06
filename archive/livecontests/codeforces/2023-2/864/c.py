import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,m):
    print("?",1,1)
    flush()
    a = readint()
    print("?",n,1)
    flush()
    b = readint()
    #[av,ah,bv,bh]
    lines = [[(1,1+a),(1+a,1+a)],[(1+a,1),(1+a,1+a)],[(n-b,1+b),(n,1+b)],[(n-b,1),(n-b,1+b)]]
    if (a+b) == n-1: #horizontal intersection
        print("?",1+a,1)
        flush()
        c = readint()
        print("!",1+a,1+c)
        flush()
        return
    elif a == b: #vertical intersection
        print("?",1,1+a)
        flush()
        c = readint()
        print("!",1+c,1+a)
        flush()
    else: #singular intersection av/bh or ah/bv
        if b < a: #ah,bv
            print("!",1+a,1+b)
            flush()
        else: #av,bh
            print("!",n-b,1+a)
            flush()
        return
        

for i in range(readint()):
    n,m = readints()
    solve(n,m)

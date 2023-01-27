import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n):
    #at most 30 bits (n is at most 29)
    zero = n
    ans = 0
    inc = 1
    for u in range(n):
        snth = "- "+str(inc)
        print(snth,flush=True)
        v = readint()
        x = v-zero
        if x == -1: #shift one
            ans += inc
            inc <<= 1
        else: #shift multiple
            #zero = v
            inc <<= (x+1)
            ans += inc
        zero = v
    ans = "! "+str(ans)
    print(ans,flush=True)
                


for i in range(readint()):
    n = readint()
    if n == -1: break
    solve(n)

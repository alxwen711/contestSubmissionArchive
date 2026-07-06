import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

# pretty sure x and x+1 gcd is always 1

for i in range(readint()):
    l,r = readints()
    if r <= 3: print(-1)
    elif l != r:
        if r % 2 == 0: print(r//2,r//2)
        else: print((r-1)//2,(r-1)//2)
    else:
        a = 2
        flag = False
        while a*a <= l:
            if l % a == 0:
                print(a,l-a)
                flag = True
                break
            a += 1
        if not flag: print(-1)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,q = readints()
for i in range(q):
    a,b = readints()
    if a ^ b != n:
        if n == 3 and max(a,b) == 3:
            print(a^b,2)
            print(a,b)
        elif a == n:
            x = 1
            while x < n and (x^b == n or x == b):
                x += 1
            print(n,str(4))
            print(a,x,x^b,b)
        elif b == n:
            x = 1
            while x < n and (x^a == n or x == a):
                x += 1
            print(n,str(4))
            print(a,x,x^b,b)
        else:
            ans = [n,3]
            print(*ans)
            print(a,a^b^n,b)
    else:
        ans = [n,2]
        print(*ans)
        print(a,b)

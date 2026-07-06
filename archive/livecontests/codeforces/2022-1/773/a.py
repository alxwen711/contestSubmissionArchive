import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    c,d = map(int,sys.stdin.readline().split())
    e,f = map(int,sys.stdin.readline().split())
    if b == d and b > f:print(abs(c-a))
    elif d == f and d > b: print(abs(c-e))
    elif b == f and b > d: print(abs(e-a))
    else: print(0)
    

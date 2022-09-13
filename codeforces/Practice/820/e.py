import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(x):
    if x == 3: return 3
    c,d = 8,2
    h = 0
    for a in range(1,x):
        for b in range(a+1,x+1):
            print("?",str(a),str(b))
            flush()
            c = readint()
            print("?",str(b),str(a))
            flush()
            d = readint()
            if c != d: return c + d
            else: h = max(h,c)
    return h*2 #probably wrong
    
    
ar = list()
x = 7
while True:
    print("? 1",str(x))
    flush()
    if readint() == -1: x -= 1
    else: break

print("!",solve(x))
    

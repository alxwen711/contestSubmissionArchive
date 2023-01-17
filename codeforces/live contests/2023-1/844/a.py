import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    w,d,h = readints()
    a,b,f,g = readints()
    print(min(abs(a-f)+h+min(b+g,2*d-b-g),abs(b-g)+h+min(a+f,2*w-a-f)))
    

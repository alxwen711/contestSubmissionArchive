import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n = readint()
    s = input()
    t = s[::-1]
    if t < s: print(t+s)
    else: print(s)
    #print(s,t)
    

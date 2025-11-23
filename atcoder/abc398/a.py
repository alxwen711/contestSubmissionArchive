import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
if n % 2 == 0:
    h = (n-2)//2
    print("-"*h+"=="+"-"*h)
else:
    h = (n-1)//2
    print("-"*h+"="+"-"*h)

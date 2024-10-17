import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
x,y = 0,0
ans = 0
for _ in range(n):
    a,b = readints()
    ans += (abs(x-a)**2+abs(y-b)**2)**0.5
    x,y = a,b
ans += (x*x+y*y)**0.5
print(ans)

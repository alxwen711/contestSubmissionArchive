import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

a = input()
b = input()
ans = list()
x = len(a)
front = 0
back = 0
for i in range(x-1):
    if a[i] != b[i]: break
    front += 1
for j in range(x-1):
    if a[-j-1] != b[-j-1]: break
    back += 1
y = x-1
for k in range(x):
    if min(front,k)+min(back,x-k-1) >= y: ans.append(k+1)
print(len(ans))
print(*ans)

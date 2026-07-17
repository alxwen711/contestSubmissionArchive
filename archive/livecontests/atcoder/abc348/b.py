import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

pts = list()

for _ in range(readint()):
    x,y = readints()
    pts.append((x,y))
n = len(pts)
ans = list()
for a in range(n):
    index = -1
    dis = -1
    for b in range(n):
        if a != b:
            d = (pts[a][0]-pts[b][0])**2+(pts[a][1]-pts[b][1])**2
            if d > dis:
                index = b
                dis = d
    ans.append(index+1)
for i in ans:
    print(i)

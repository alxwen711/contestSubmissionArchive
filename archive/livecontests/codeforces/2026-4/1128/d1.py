import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
for n spots, only cover n-1 uniquely

given that at n = 3, 2 covers are needed


"""

for _ in range(readint()):
    n,m = readints() # m is 0 in this case
    if n == 1:
        print(0)
        continue
    segments = list()
    dist = n//2
    for i in range(1,n-dist+1):
        segments.append((i,i+dist-1))
    print(len(segments))
    for j in segments:
        print(j[0],j[1])

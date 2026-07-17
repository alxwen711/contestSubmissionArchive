import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
every 4 columns repeat
a -> c for horizontal
b -> d for vertical

determine area for each column from b to d
"""

a,b,c,d = readints()
areas = []
vd = d-b
count = vd//2
if vd % 2 == 0: areas = [count*3,count*3,count,count]
elif b % 2 == 0: areas = [count*3+2,count*3+1,count,count+1]
else: areas = [count*3+1,count*3+2,count+1,count]

hd = c-a
count = hd//4
ans = sum(areas)*count
for i in range(hd % 4):
    ans += areas[(c-i-1) % 4]
print(ans)

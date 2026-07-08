import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
pass
1 1
0 3
3 4
4 7

fail
2 1
0 2
1 0

there must be x+y-1 edges (x+y nodes), this then
implies that any 0 even and odd 0 is definitely impossible
"""

def generate(a,b):
    for i in range(a):
        print(1,i*2+2)
        print(i*2+2,i*2+3)
    increment = 2*a
    for j in range(b):
        print(1,2+increment+j)

for _ in range(readint()):
    x,y = readints()
    n = x+y
    if (n % 2 == 1 and y == 0) or (n % 2 == 0 and x == 0):
        print("NO")
        continue
    if n % 2 == 1: y -= 1
    else: x -= 1
    if x > y:
        print("NO")
        continue
    else:
        print("YES")
        generate(x,y-x)





        

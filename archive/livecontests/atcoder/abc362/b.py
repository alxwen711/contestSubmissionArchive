import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def right(a0,a1,b0,b1,c0,c1):
    x0,x1 = b0-a0,b1-a1
    y0,y1 = c0-b0,c1-b1
    if x0 == 0 and y1 == 0: return True
    if x1 == 0 and y0 == 0: return True
    return x0*y0 == x1*y1*-1

a0,a1 = readints()
b0,b1 = readints()
c0,c1 = readints()
if right(a0,a1,b0,b1,c0,c1) or right(b0,b1,c0,c1,a0,a1) or right(c0,c1,a0,a1,b0,b1): print("Yes")
else: print("No")

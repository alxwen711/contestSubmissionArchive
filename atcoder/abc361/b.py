import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

a,b,c,d,e,f = readints()
g,h,i,j,k,l = readints()

if d > g and j > a and e > h and k > b and l > c and f > i: print("Yes")
else: print("No")

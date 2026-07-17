import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 to k exclusive, 1 will never fail, k will always fail
"""
n,k = readints()
aa,bb = 1,k
for i in range(n):
    a,b = input().split()
    a = int(a)
    if b == "SAFE":
        aa = max(aa,a) 
    else:
        bb = min(bb,a)
#highest safe, lowest broken
print(aa+1,bb-1)

import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = readar()

h = list()
a,b,c = -1,-1,-1
for i in ar:
    if i >= a:
        a,b,c = i,a,b
    elif i >= b:
        b,c = i,b
    elif i >= c:
        c = i
    if c != -1: print(c)

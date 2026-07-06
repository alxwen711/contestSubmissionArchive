import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
triangles will never touch, else larger
one is more effective
start with largest size limit?

f: find the node splits for each edge
first black node is highest degree
maybe after this its highest degree not counting?
"""

n,k,a = readints()
x = list()
y = list()
c = list()
for j in range(n):
    b,bb,bbb = readints()
    x.append(b)
    y.append(bb)
    c.append(bbb)
    

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
n boxes total
each box has at least 1 ball
each ball off of max reduces fill by 1
"""
for i in range(readint()):
    n,m = readints()
    ar = readar()
    print(max(0,n-(n*m-sum(ar))))
    

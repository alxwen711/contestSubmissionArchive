import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 always leads to <
n always leads to >
<?>?> example: 4,1,3,5,2,6
>?><< example: 3,5,4,6,2,1

the one hint:

"""



n,m = readints()

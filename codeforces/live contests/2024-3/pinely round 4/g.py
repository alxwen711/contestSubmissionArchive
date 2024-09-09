import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
is there any scenario where it's impossible? does not look like it
The problem constraints make it so that literally
performing each action is possible

still very unsure how to even choose the spots, does not feel like greedy
should work
"""

for _ in range(readint()):
    n,m,k,q = readints()
    s = readin()

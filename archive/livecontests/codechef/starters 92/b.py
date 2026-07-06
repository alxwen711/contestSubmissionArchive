import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
div 4 if w and h are both even or both odd
only both even can fix?
"""

def f(w,l):
    if w % 2 != l % 2: return "YES"
    if w % 2 == 0 and l % 2 == 0: return "YES"
    return "NO"

for i in range(readint()):
    w,l = readints()
    print(f(w,l))

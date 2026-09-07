import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
ARCRC -> 2
ARARCRC -> CRARARC (4)

place X to break
determine largest square

start with AR 25 times (50 characters)
"""

ans = ["AR"]*25
x = readint()
while x != 0:
    if x >= 25:
        x -= 25
        ans.append("CR")
    else:
        ans.insert(x,"CR")
        break
print(*ans,sep="")

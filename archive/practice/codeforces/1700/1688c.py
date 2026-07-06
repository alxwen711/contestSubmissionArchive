import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
the starting string is ALWAYS length 1
ALL operations are used
it is NOT absolutely necessary to reconstruct the entire order
at most only 26 possible starts

note: would not have gotten this without first 4 hints, this is a troll problem
"""

for i in range(readint()):
    n = readint()
    h = [0]*128
    for j in range(2*n):
        fuckyou = sys.stdin.readline()
        for WHY in range(len(fuckyou)-1):
            h[ord(fuckyou[WHY])] ^= 1
    fu = sys.stdin.readline()
    for ffs in range(len(fu)-1):
        h[ord(fu[ffs])] ^= 1
    for snth in range(97,97+26):
        if h[snth] == 1: print(chr(snth))
            

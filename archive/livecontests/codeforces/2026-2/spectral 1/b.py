import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the operation is swapping any two values of even distance apart
priority is to choose highest remaining positive possible
on parity there would have to be at least one mark
"""

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar() # operations in order
    odd,even = list(),list()
    for i in range(n):
        if i % 2 == 0:
            odd.append(ar[i])
        else:
            even.append(ar[i])
    o,e = 0,0
    for b in br:
        if b % 2 == 1: o += 1
        else: e += 1
    odd.sort()
    even.sort()
    if o > 0:
        odd.pop()
        for _ in range(o-1):
            if len(odd) == 0: break
            if odd[-1] < 0: break
            odd.pop()

    if e > 0:
        even.pop()
        for _ in range(e-1):
            if len(even) == 0: break
            if even[-1] < 0: break
            even.pop()

    print(sum(odd)+sum(even))
    #print(odd,even)



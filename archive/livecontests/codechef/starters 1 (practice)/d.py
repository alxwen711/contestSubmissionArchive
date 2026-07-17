import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#01110001 -> 01011100
"""
3
4 1
1100
4 0
0101
6 1
101001

0000101010101000000
"""

for i in range(readint()):
    n,c = readints()
    s = input()
    gaps = list()
    chain = 0
    inc = 0
    while inc != n:
        if s[inc] == "0": inc += 1
        else: break
    if inc == n:
        print("YES")
        continue
    for j in range(n):
        if s[(j+inc) % n] == "1":
            gaps.append(chain)
            chain = 0
        else: chain += 1
    gaps.append(chain)
    gaps.sort()
    gaps.pop() #disregard largest gap
    #print(gaps)
    if len(gaps) == 0: print("YES")
    elif gaps[-1] <= c: print("YES")
    else: print("NO")

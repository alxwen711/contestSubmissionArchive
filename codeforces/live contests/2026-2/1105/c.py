import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Assume Alice MUST win in one move
Then some sort of setup must exist to have n-1 0's

TC3
001
100
101
010
110
all valid solutions must leave a single 4 in the array

1 4 5 2 2
1 0 5 2 6
1 4 1 2 6

whatever bits are left makes up the answer (all odd bits will have 1 left)
if xor total is 0?

3 4 has a solve (3 3)

determine how many ways there are to brute xor everything else and leave a singular

can a non-winning position be setup? no?
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    if n == 1:
        print(0)
        continue
    v = 0
    for i in ar:
        v ^= i
    ans = 0
    if v == 0: ans += 1
    for j in ar:
        v ^= j
        if j > v: ans += 1
        v ^= j
    print(ans)


    

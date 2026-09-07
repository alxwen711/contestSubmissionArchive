import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
wincon is to leave less than k stones on the field
second case is classical nim (xor)

when does bob win when k = 2

2 2 2 -> 0 0 0
2 2 3 -> 0 0 1
4 4 4 -> 2 2 2 -> 0 0 0


5 5 5 -> 3 3 3 -> 1 1 1 (Alice CAN win)

2 5 7 -> 0 3 5

residue above k is less than k -> Bob wins
residue can be reduced in one turn to above condition -> Alice wins

the win con can seemingly invert

wtf do you mean that works
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    if min(ar) < n: print("Alice")
    else:
        v = min(ar)//n*n
        c = 0
        for i in ar:
            c += (i-v)
        print("Alice" if c >= n else "Bob")

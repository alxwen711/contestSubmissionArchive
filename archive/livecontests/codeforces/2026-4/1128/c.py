import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
evens can be removed arbritarily

you can always remove exactly 1 element

e o
1 1 loses
x e wins
2+ o wins
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    even,odd = 0,0
    for i in ar:
        if i % 2 == 0: even += 1
        else: odd += 1
    if odd % 2 == 0: print("Moggity")
    elif even >= 2: print("Moggity")
    elif even == 0:
        print("Moggity" if odd != 3 else "Larpity")
    elif odd == 1: print("Larpity")
    else: print("Moggity")

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
Skipping a bit later to once the non scorable problems are available
in practice for walkthrough
"""
"""
#5pt sack


for i in range(readint()):
    l,r = readints()
    e = {}
    for a in range(l,r+1):
        for b in range(a,r+1):
            c = a+b
            d = a^b
            if c == d: e[d] = 1
    print(len(e.keys()))
"""


"""
25pts
if l = 0, how many unique vals
are creatable?
if a+b = a^b, a&b = 0
"""

for i in range(readint()):
    l,r = readints()
    if r <= 101:
        e = {}
        for a in range(l,r+1):
            for b in range(a,r+1):
                c = a+b
                d = a^b
                if c == d: e[d] = 1
        print(len(e.keys()))
    else:
        x = 1
        while x <= r:
            x <<= 1
        print(x)

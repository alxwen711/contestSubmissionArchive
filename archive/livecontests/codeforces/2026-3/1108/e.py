import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
v is unknown AND can be rigged to x, b is unknown
either x & v or x | v is returned

then send b0 and b1

then values can be one of v ^ b0, v ^ b1

determine if b0 or b1 was used

try 12 as the golden value

if the resulting value 16+ -> OR must have been used, use the mod 4 solve
if the 8 or 4 bit is missing -> AND must have been used, use 8/4 bit solve
if 8 and 4 bit exist AND 1 or 2 bit exist -> OR must have been used, mod 4
if EXACTLY 12 -> consult the scenarios for mod 16

except there is no pairs existing for this
maybe just try bigger values???

0 case is also missed here, probably edge case
"""


def solve():
    queryval = 2**28-2**14
    print(queryval)
    flush()
    o = readint()
    if o == queryval: # tricky shit here
        print(0,2**14+1)
        flush()
        v = readint()
        # then figure out here
        if v | queryval == queryval or v & queryval == queryval:
            print(0)
            flush()
            return
        else:
            print(1)
            flush()
            return
    elif o == 0: # set 1 bits must be 0 in v
        assume = 2**20
        m1,m2 = 0,assume
        print(m1,m2)
        flush()
        v = readint()
        if v & 2**20 == 0:
            print(0)
            flush()
            return
        else:
            print(1)
            flush()
            return
    else:
        if o >= (2**28): # OR used, run over clear
            assume = o - (o % (2**28))
            m1,m2 = 0,assume
            print(m1,m2)
            flush()
            v = readint()
            if v == 0:
                print(1)
                flush()
                return
            else:
                print(0)
                flush()
                return
        elif o % (2**14) != 0: # OR used, run modulo
            assume = o % (2**14)
            m1,m2 = 0,assume
            print(m1,m2)
            flush()
            v = readint()
            if v % (2**14) == 0:
                print(1)
                flush()
                return
            else:
                print(0)
                flush()
                return
        else: # AND used, assume is exactly as is
            assume = o
            m1,m2 = 0,assume
            print(m1,m2)
            flush()
            v = readint()
            if v == 0:
                print(1)
                flush()
                return
            else:
                print(0)
                flush()
                return
for _ in range(readint()):
    solve()

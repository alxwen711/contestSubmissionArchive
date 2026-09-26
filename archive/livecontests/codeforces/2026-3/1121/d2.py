import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1
11
101
0101
10101
010100
1001010
10010100
100101000 or 010010100
0100101000 or 1000100010
332 10001000100


333 100010001000
433 1000010001000
434 10000100010000
435 100001000100000
553 1000001000001000
554 10000010000010000

555 100000100000100000
655 1000000100000100000
656 10000001000001000000
657 100000010000010000000
775 1000000010000000100000
776 10000000100000001000000

777 100000001000000010000000
877 1000000001000000010000000
878
879
997 1000000000100000000010000000
998

999 100000000010000000001000000000


brute force possible solutions for n = 7 and onwards
pattern is found
"""

def compute(n,ar):
    x = 0
    for i in range(n):
        for j in range(i,n):
            v = int("".join(ar[i:j+1]),2)
            if v % 3 == 0: x += 1
    return x

best = 868678568756876786434
ansl = list()
n = 11
v = ["0"]*n

for a in range(n):
    v[a] = "1"
    x = compute(n,v)
    if x < best:
        best = x
        ansl = list()
    if x == best:
        ansl.append("".join(v))
    v[a] = "0"

    
for a in range(n-1):
    v[a] = "1"
    for b in range(a+1,n):
        v[b] = "1"
        x = compute(n,v)
        if x < best:
            best = x
            ansl = list()
        if x == best:
            ansl.append("".join(v))
        v[b] = "0"
    v[a] = "0"


for a in range(n-2):
    v[a] = "1"
    for b in range(a+1,n-1):
        v[b] = "1"
        for c in range(b+1,n):
            v[c] = "1"
            x = compute(n,v)
            if x < best:
                best = x
                ansl = list()
            if x == best:
                ansl.append("".join(v))
            v[c] = "0"
        v[b] = "0"
    v[a] = "0"
for snth in ansl:
    print(snth)


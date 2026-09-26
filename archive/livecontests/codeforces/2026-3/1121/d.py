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

at most 3 lit pixels
0
11
110
1001
1100
1111
10010
10101
100001
any 0 is irritating

d2 scuff brute force
"""

lowans = [
    "",
    "1",
    "11",
    "101",
    "0101",
    "10101",
    "010100",
    "1001010",
    "10010100",
    "100101000",
    "0100101000",
    "10001000100"    
]

adjustval = [(0,0,0),(1,0,0),(1,0,1),(1,0,2),(2,2,0),(2,2,1)]

for _ in range(readint()):
    n = readint()
    if n < 12: print(lowans[n])
    else:
        roundval = n//6
        x = roundval*2-1
        r = n % 6
        d = adjustval[r]
        a,b,c = x+d[0],x+d[1],x+d[2]
        ans = ["0"]*n
        ans[0] = "1"
        ans[a+1] = "1"
        ans[a+b+2] = "1"
        print(*ans,sep="")

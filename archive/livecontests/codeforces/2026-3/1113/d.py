import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the not good pairs:
0,1
00,11
000,111
0000,1110; furthest reduction is to 00,11

01010,10101

00111,11000

they don't have to be substrings, then only the count of 0/1 matters

00110000
00111111

this is split into 0011,1111 and 0000,0011 (1,2,7,8)

we can't just rearrange everything around
"""

for _ in range(readint()):
    n,q = readints()
    s = readin()
    t = readin()
    pa = [0] #00
    pb = [0] #01
    pc = [0] #10
    pd = [0] #11
    for i in range(n):
        if s[i] == "0" and t[i] == "0":
            pa.append(pa[-1]+1)
            pb.append(pb[-1])
            pc.append(pc[-1])
            pd.append(pd[-1])
        if s[i] == "0" and t[i] == "1":
            pa.append(pa[-1])
            pb.append(pb[-1]+1)
            pc.append(pc[-1])
            pd.append(pd[-1])
        if s[i] == "1" and t[i] == "0":
            pa.append(pa[-1])
            pb.append(pb[-1])
            pc.append(pc[-1]+1)
            pd.append(pd[-1])
        if s[i] == "1" and t[i] == "1":
            pa.append(pa[-1])
            pb.append(pb[-1])
            pc.append(pc[-1])
            pd.append(pd[-1]+1)
    for _ in range(q):
        l,r = readints()
        a,b,c,d = pa[r]-pa[l-1],pb[r]-pb[l-1],pc[r]-pc[l-1],pd[r]-pd[l-1]
        v = min(b,c)
        b -= v
        c -= v
        if b == 0 and c == 0: print("YES")
        elif b != 0:
            if b > (a+d): print("NO")
            else: print("YES")
        else: # c != 0
            if c > (a+d): print("NO")
            else: print("YES")
            

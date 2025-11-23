import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
any consecutive 0's are fine
any edge 0's are fine
101 cases are problems
1010 <- both look at 2nd flower
10100101 <- 1L1RL1R1
10110 <- impossible
1010101 <- also impossible

sort of a what subchains are possible type question
010 can be jumped
1 can be jumped
00 can be jumped
reaching end or end-1 = win
jumping 0 at the very start also works
0 by itself also works if completely surrounded??????
"""
c = ["1","00","010","000"]
for _ in range(readint()):
    n = readint()
    s = readin()
    if n <= 2: print("YES")
    else:
        h = [0]*(n+1)
        h[0] = 1
        q = [0]
        if s[0] == "0":
            h[1] = 1
            q.append(1)
        i = 0
        ql = len(q)
        while i != ql:
            x = q[i]
            if 1 <= x <= n-2:
                if s[x-1] == "0" or s[x+1] == "0":
                    if h[x+1] == 0:
                        h[x+1] = 1
                        q.append(x+1)
                        ql += 1
            for sc in c:
                if len(sc)+x <= n:
                    flag = True
                    for j in range(len(sc)):
                        if s[x+j] != sc[j]:
                            flag = False
                            break
                    if flag and h[x+len(sc)] == 0:
                        h[x+len(sc)] = 1
                        q.append(x+len(sc))
                        ql += 1
            i += 1
        print("YES" if h[-1] or h[-2] else "NO")
        #print(h)

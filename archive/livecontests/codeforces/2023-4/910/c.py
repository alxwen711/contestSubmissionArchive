import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
odd/even case has to be satisfied based on grid dimensions
always at least 3*3 edges
"""

for _ in range(readint()):
    n,m,k = readints()
    req = n+m-2
    if (req % 2 != k % 2) or k < req: print("NO")
    else:
        print("YES")
        ar = list() #hor
        br = list() #ver
        for _ in range(n):
            tmp = list()
            for _ in range(m-1):
                tmp.append("B")
            ar.append(tmp)
        for _ in range(n-1):
            tmp = list()
            for _ in range(m):
                tmp.append("B")
            br.append(tmp)
        br[0][0] = "R"
        br[0][1] = "R"
        br[0][2] = "R"
        br[1][1] = "R"
        ar[1][1] = "R"
        ar[2][0] = "R"

        #br 2,2 3,2 4,2
        for s in range(2,n-1,2):
            br[s][2] = "R"

        st = 2
        if br[n-2][2] == "R": st += 1

        for t in range(st,m-1,2):
            ar[-1][t] = "R"

        for a in ar:
            print(*a)
        for b in br:
            print(*b)


        
        
        

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
complete segment as early as possible?

how is 31 possible on 3rd test case??

2 3 6 7 0 1 4 5
full groups: 0 1 5 6 7
0 4 -> 8 +8
1 4 -> 7*(2-1) +7
5 4 -> 3*(6-2) +12
6 4 -> 2*(7-6) +2 
7 X -> 1*(8-7) +1 
0 1 4 5 2 3 6 7
1 2 2 2 2 6 7 8
7 0 1 4 5 2 3 6
0 1 2 2 2 2 6 8

2 1 0 4 3 5 7 6 8
full groups: 0 1 2 4 5 7 8
"""
def f(ar):
    d = [0]*n
    ans = 0
    sc = 0
    br = list()
    for i in range(len(ar)):
        d[ar[i]] = 1
        while sc != len(ar):
            if d[sc] == 1: sc += 1
            else: break
        br.append(sc)
        ans += sc
    return ans,br

    
for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 0
    for c in range(n):
        g,br = f(ar)
        print(c,g,ar,br)
        ans = max(ans,g)
        ar.insert(0,ar.pop())
    print(ans)

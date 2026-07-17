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


0 18 [2, 3, 6, 7, 0, 1, 4, 5] [0, 0, 0, 0, 1, 4, 5, 8] 0145
1 13 [5, 2, 3, 6, 7, 0, 1, 4] [0, 0, 0, 0, 0, 1, 4, 8] 014
2 9 [4, 5, 2, 3, 6, 7, 0, 1] [0, 0, 0, 0, 0, 0, 1, 8] 01
3 8 [1, 4, 5, 2, 3, 6, 7, 0] [0, 0, 0, 0, 0, 0, 0, 8] 0
4 31 [0, 1, 4, 5, 2, 3, 6, 7] [1, 2, 2, 2, 3, 6, 7, 8] 01__2367
5 24 [7, 0, 1, 4, 5, 2, 3, 6] [0, 1, 2, 2, 2, 3, 6, 8] 01__236
6 18 [6, 7, 0, 1, 4, 5, 2, 3] [0, 0, 1, 2, 2, 2, 3, 8] 01__23
7 15 [3, 6, 7, 0, 1, 4, 5, 2] [0, 0, 0, 1, 2, 2, 2, 8] 01__2

"""

def com(ar,n):
    ar.append(n-1)
    prev = 0
    ans = 0
    for i in range(len(ar)):
        ans += ((n-ar[i])*(ar[i]+1-prev))
        prev = ar[i]+1
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    st = ar.index(0)
    ans = n
    v = ans
    br.append((ar[st],0))
    st += 1
    if st == n: st = 0
    for i in range(1,n):
        while len(br) != 0:
            if br[-1][0] > ar[st]: #at least len 2
                v -= br[-1][0]*(br[-1][1]-br[-2][1])
                br.pop()
            else: break
        br.append((ar[st],i))
        v += br[-1][0]*(br[-1][1]-br[-2][1])
        ans = max(ans,v)
        #print(br,v)
        st += 1
        if st == n: st = 0
    print(ans)

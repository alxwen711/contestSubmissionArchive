import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
10001101 -> 10000111 x -> 11000110 -> 01001101
11011101 fails under greedy construction
10000000010000100001
check for even # of 0s
find first and second odd group ignoring head
shift from start of first to end of second
doesn't have to be an adjacent subsequence?
probably not related to odd even groups?
if 0 odd, then auto pass, but something like
4 odd can work, and something like 10101010101010...
is possible
"""
def solve(ar,n):
    sss = sum(ar)
    if sss % 2 == 1:
        print(-1)
        return
    if sss == 0 or sss == n*2:
        br = list()
        for j in range(n):
            br.append(j+1)
        print(0)
        print(*br)
        return
    #???
    print(-1)

for i in range(readint()):
    n = readint()
    s = input()
    ar = list()
    for j in range(n):
        ar.append(int(s[j]))

    solve(ar,n)

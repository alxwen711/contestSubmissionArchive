import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
0 and 1 count is either equal or 1 apart
k pairs of adjacent characters exist

best case is n-2 -> 00001111
smallest case is 01010101
00101011 -> 2
01100110 -> 3
number of adjacent groups

1 adj group -> 7 containers
01101010
7 adj groups -> 1 container; impossible

odd case?
n = 7, 5 adj groups -> 0000111

"""

for _ in range(readint()):
    n,k = readints()
    if k+1 == n:
        print(-1)
        continue
    adj = n-k
    zero = (n+1)//2
    one = n//2
    ans = list()
    for i in range(adj):
        if i % 2 == 0:
            zero -= 1
            ans.append("0")
        else:
            one -= 1
            ans.append("1")
    ans[0] = "0"*(zero+1)
    ans[1] = "1"*(one+1)
    print(*ans,sep="")

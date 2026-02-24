import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
cards are 1,1,2,2,...,n,n

6 10 setup can be done via
1 2 3 4 5 4 2 1 6 5 6 3

slowest method:
1 2 3 1 4 2 5 3 6 4 7 5 6 7
1 2 3 1 2 3 takes 5 moves
1 2 3 1 4 2 3 4 takes 7 moves
"""

def maximal(x):
    ar = [1,2]
    for i in range(2,x):
        ar.append(i+1)
        ar.append(i-1)
    ar.append(x-1)
    ar.append(x)
    return ar

for _ in range(readint()):
    n,k = readints()
    if n == 1:
        if k == 1:
            print("YES")
            print("1 1")
        else: print("NO")
    elif k < n:
        print("NO")
    elif k <= n+(n//2):
        extrasteps = k-n
        ans = list()
        for i in range(2*extrasteps):
            ans.append(i+1)
        for i in range(2*extrasteps):
            ans.append(i+1)
        for i in range(2*extrasteps,n):
            ans.append(i+1)
            ans.append(i+1)
        print("YES")
        print(*ans)
    elif k < n*2:
        maxset = n*2-1-k # how many numbers to spare out
        ans = maximal(n-maxset)
        for i in range(n-maxset,n):
            ans.append(i+1)
            ans.append(i+1)
        print("YES")
        print(*ans)
    else:
        print("NO")
        

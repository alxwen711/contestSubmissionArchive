import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
# top 3 sights do not have to be consecutive

def solve(n,ar):
    # find best for top 2 (top 1 is trivial)
    two = [0]*n
    two[1] = ar[0]+ar[1]-1
    inc = ar[0]-1
    for j in range(2,n):
        inc = max(inc-1,ar[j-1]-1)
        two[j] = ar[j]+inc
    three = [0]*n
    three[2] = ar[0]+ar[1]+ar[2]-2
    inc = two[1]-1
    for k in range(3,n):
        inc = max(inc-1,two[k-1]-1)
        three[k] = ar[k]+inc
    return max(three)

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
find an optimal order for battery testing

n = 4
12
34 (4 work)
13
24 (3 work)
14
23 (2 work)


n = 5 has 10 cases to try
12
34 (5 work)
13
24 (4 work)
14
23 (3 work)
15
25
35
45 (2 work)

n = 6 has 15 cases to try

if n is even, then drouping the pairs will work
if n is odd, ?

try setting up on n being odd
"""
def gensetup(n):
    ar = list()
    for i in range(n-1):
        ar.append((i,n-1))
        br = list()
        for j in range(n):
            kk = (i+j+1) % n
            if kk != i and kk != n-1:
                br.append(kk)
        for k in range(n//2-1):
            ar.append((br[k],br[-k-1]))
    return ar

def solve(n):
    ar = gensetup(n//2*2)
    if n % 2 == 1:
        for i in range(n-1):
            ar.append((i,n-1))
    for i in ar:
        print(i[0]+1,i[1]+1)
        flush()
        x = readint()
        if x != 0: return x

for _ in range(readint()):
    x = solve(readint())
    if x == -1: break
    


import sys

def solve(n,ar):
    for j in range(n-1):
        if ar[j+1] % ar[j] == 0:
            ar[j+1] = ar[j]
        else: return "NO"
    return "YES"


for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    print(solve(n,ar))
    

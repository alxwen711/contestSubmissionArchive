import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
possible constraints:
ar sum is even
neighbour sum is at least equal
taking each 2nd element should result in half the arr sum
in the odd case, n//2 elements added and last one has to make parity
"""
def trial(n,ar,x,v):
    ar[x] -= v
    ar[x+1] -= v
    index = x+1
    for i in range(n-2):
        if ar[index] < 0: return False
        ar[(index+1) % n] -= ar[index]
        ar[index] = 0
        index = (index+1) % n
    return ar[index] == ar[(index+1) % n]

def solve(n,ar):
    if n == 2: return "YES" if ar[0] == ar[1] else "NO" #base case
    #adj check
    for i in range(n):
        if ar[(i-1) % n] + ar[(i+1) % n] < ar[i]: return "NO"
    s = sum(ar) #must be even
    if s % 2 == 1: return "NO"
    if n % 2 == 0: #? idk if this segment is true??? 
        return "YES" if sum(ar[::2])*2 == s else "NO"
    else:
        br = list()
        index = 0
        for i in range(n):
            br.append(ar[index])
            index = (index+2) % n
        half = n//2
        u = sum(br[:half])
        cr = [0]*n
        index = n-1
        ss = s//2
        for j in range(n):
            cr[index] = ss-u
            if ss-u < 0: return "NO"
            u -= br[j]
            u += br[(half+j) % n]
            index = (index+2) % n
        for k in range(n):
            if cr[k]+cr[(k+1) % n] != ar[k]: return "NO"
    return "YES"
    
for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

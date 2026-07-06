import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
first case has reason to increase the first value
there is never a reason to decrease the last value
"""

def solve(n,ar):
    c = 0
    a = 0
    cr = 0
    for i in range(n-2,-1,-1):
        cr += 1
        if ar[i] > ar[i+1]:
            d = ar[i]-ar[i+1]
            ar[i] = ar[i+1]
            c += d
        else:
            inc = min(c,ar[i+1]-ar[i])
            ar[i] += inc
            c -= inc
            if c == 0 and ar[i] < ar[i+1]:
                a += cr*(ar[i+1]-ar[i])
                inc = a//(cr+1)
                ar[i] += inc
                a -= inc*(cr+1)
        #print(ar,c,a)
    if c != 0: return "No"
    return "Yes"
    

for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

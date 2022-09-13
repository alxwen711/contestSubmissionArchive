import sys
"""
def findMex(mex):
    x = 0
    while mex[x] != 0:
        x += 1
        if x == 100: return 100
    return x

def m(mex):
    while mex[0] != 0:
        c = findMex(mex)
        if mex """

for i in range(int(sys.stdin.readline())):
    t = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    ans = 0
    
    for j in range(t):
        for k in range(t-j):
            a,b = k, k+j
            for l in range(b-a+1):
                if ar[l+a] == 0: ans += 1
            ans += (b-a+1)
    print(ans)

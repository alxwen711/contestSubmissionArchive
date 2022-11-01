import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def freq_dict(ar, pos = False) -> dict:
    d = {}
    if ar == None: return d
    for i in range(len(ar)):
        x = ar[i]
        if d.get(x) == None:
            if pos: d[x] = list()
            else: d[x] = 0
        if pos: d[x].append(i)
        else: d[x] += 1
    return d

def solve(h,x):
    if sum(h) == 0: return "Yes"
    r = x
    overflow = x
    flag = True
    #if at any point over 500000, autofail
    for i in range(x-1,0,-1):
        r -= h[i]
        if r < 0:
            r = r % overflow
        r *= i
        if flag:
            overflow *= i
            if overflow > 645616548965165165481665165831564651896316165895665:
                overflow = 645616548965165165481665165831564651896316165895665
                flag = False
        if r > 500000: return "No"
    if r == 0: return "Yes"
    return "No"

n,x = readints()
ar = readar()
aar = freq_dict(ar)
br = list(aar.keys())

h = [0]*x
for k in range(len(br)):
    if br[k] < x:
        h[br[k]] = aar[br[k]]
print(solve(h,x))

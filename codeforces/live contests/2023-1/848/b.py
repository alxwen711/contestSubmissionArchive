import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,m,d,ar,br):
    cr = list()
    index = 0
    for i in range(n):
        if ar[i] == br[index]:
            cr.append(i)
            if len(cr) >= 2:
                if cr[-1] > cr[-2] + d: return 0 
            index += 1
            if index == m: break
    if index != m: return 0
    #good array, find shortest break pt
    best = 7895798475
    a,b = 7598275892347,92579835798325983
    fixa = True
    if d >= (n-1): fixa = False
    for j in range(m-1):
        diff = cr[j+1]-cr[j]
        if best == 1 or diff == 1: return 1
        if fixa: a = d-diff+1
        b = diff
        best = min(best,a,b)
    return best

for i in range(readint()):
    n,m,d = readints()
    ar = readar()
    br = readar()
    print(solve(n,m,d,ar,br))

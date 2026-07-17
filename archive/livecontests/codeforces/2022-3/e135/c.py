import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 to 9 digits
anything -> single dig -> 1
O(n log n) min
"""

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

def solve(ar,br):
    ans = 0
    for i in range(len(ar)):
        if ar[i] > 9:
            ar[i] = len(str(ar[i]))
            ans += 1
        if br[i] > 9:
            br[i] = len(str(br[i]))
            ans += 1
    aar = freq_dict(ar)
    at = list()
    bt = list()
    for j in range(len(br)):
        x = br[j]
        if aar.get(x) == None: bt.append(x)
        elif aar[x] == 0: bt.append(x)
        else: aar[x] -= 1
    ak = list(aar.keys())
    for k in range(len(aar)):
        for l in range(aar[ak[k]]):
            at.append(ak[k])
    for f in range(len(at)):
        if at[f] != 1:
            ans += 1
        if bt[f] != 1:
            ans += 1
    return ans
        

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    #find how many values are not shared
    aar = freq_dict(ar)
    at = list()
    bt = list()
    for j in range(len(br)):
        x = br[j]
        if aar.get(x) == None: bt.append(x)
        elif aar[x] == 0: bt.append(x)
        else: aar[x] -= 1
    ak = list(aar.keys())
    for k in range(len(aar)):
        for l in range(aar[ak[k]]):
            at.append(ak[k])
    print(solve(at,bt))
            
    

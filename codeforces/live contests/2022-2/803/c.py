import sys

def solve(n,ar):
    if n == 3:
        x = ar[0]+ar[1]+ar[2]
        if x == ar[0] or x == ar[1] or x == ar[2]: return "YES"
        else: return "NO"
    elif n == 4:
        a = list()
        a.append(ar[0]+ar[1]+ar[2])
        a.append(ar[3]+ar[1]+ar[2])
        a.append(ar[0]+ar[3]+ar[2])
        a.append(ar[0]+ar[1]+ar[3])
        for f in range(4):
            if a[f] != ar[0] and a[f] != ar[1] and a[f] != ar[2] and a[f] != ar[3]: return "NO"
        return "YES"
    #n at least 5
    pos = 0
    neg = 0
    for k in range(n):
        if ar[k] > 0:
            if pos != 0: return "NO"
            else: pos = ar[k]
        if ar[k] < 0:
            if neg != 0: return "NO"
            else: neg = ar[k]
    if pos == 0 or neg == 0 or pos+neg == 0: return "YES"
    return "NO"
        

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    """
    fail conditions:
    3+ pos
    3+ neg
    2 pos + 0
    2 neg + 0

    pass conditions:
    1 pos
    1 neg
    1 pos and 1 neg, abs equal
    all 0
    """
    print(solve(n,ar))

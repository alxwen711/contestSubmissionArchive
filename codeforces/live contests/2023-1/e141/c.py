import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
wc: 0,1,2,3,4...
"""


#det how many people can be beaten
def solve(n,m,ar):
    v = list()
    for j in range(n):
        v.append([ar[j],j])
    v.sort()
    #find number of wins first
    wins = 0
    x = m
    h = [0]*n
    prev = -1
    for k in range(n):
        if v[k][0] > x:
            break
        else:
            wins += 1
            x -= v[k][0]
            h[v[k][1]] = 1
            prev = v[k][0]
    #print("wins:",wins)
    if wins == 0: return n+1
    if wins == n: return 1
    rank = n+1-wins
    #see if 1 higher can be clinched
    if h[wins] == 1: return rank-1
    cost = ar[wins]
    x += (prev-cost)
    if x >= 0: return rank-1
    return rank


for i in range(readint()):
    n,m = readints()
    ar = readar()
    print(solve(n,m,ar))

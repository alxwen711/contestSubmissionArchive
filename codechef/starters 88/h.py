import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    #trivial cases
    if n == 1: return 1
    if n == 2: return 0

    #sum matrix
    sr = list()
    for j in range(n):
        tmp = deepcopy(ar)
        sr.append(tmp)
        for k in range(n):
            sr[j][k] += ar[j]
    """
    possible ideas:
    try solving with pairing first two
    using sum table should speed up the process
    repeat until all initial pairs tested/impossible to do better
    choose pairs greedily (earilest in array)
    n^2 pairs with O(n^2) per pair would be O(n^4)
    main problem is [1,2,3,4,5,6], ie. max deletions

    also if you are still watching this asmr vid then feel free
    to subscribe because I will probably be posting another one
    of these for next week's starters contest again lol

    maybe there's a greedy idea of using the most common sums first?
    fails due to [1,6,2,5,3,4,7,8], 9 is the most common sum but
    using 7 is optimal

    track frequency of each sum, stop once mathematically impossible
    """

    d = {}
    br = list()
    for a in range(n):
        for b in range(a+1,n):
            x = sr[a][b]
            if d.get(x) == None: d[x] = 0
            d[x] += 1
    for v in d.keys():
        br.append([d[v],v])

    br.sort()
    best = 2
    for snth in br:
        freq,val = snth[0],snth[1]
        # if freq not high enough, break, else brute force
        
    return n-best

for i in range(readint()):
    n = readint() # O(n^2) solution possible, n <= 2000
    ar = readar()
    print(solve(n,ar))

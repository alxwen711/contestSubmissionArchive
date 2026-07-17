import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
heavily suspecting this is binary exponention via matrix scuff

O(n^2) subarrays possible, matrix mult is O(n^3), binary expo is O(log n)

O(n^6 log n) (yeah I don't think that works)

maybe some modded operation can make this O(n^4 log n)?

use a pseudo dp state

this only considers the final layer, how to take sum across all??

basic adding would be O(m^4 * n), log n step is needed

even then last testcase has 219883 which is a blatent overcount
"""

def increment(ar,br,p):
    n = len(ar)
    cr = list()
    for _ in range(n):
        tmp = [0]*n
        cr.append(tmp)
    for a in range(n):
        for b in range(a,n):
            # what intersects (a,b)?
            for c in range(b+1):
                for d in range(max(c,a),n):
                    cr[c][d] = (cr[c][d] + ar[a][b]*br[c][d]) % p
    return cr

n,m,p = readints()

# construct_base(m,p)

if n == 1: print(m % p)
else: # construct the 2 case first
    matrix = None
    mult = list() # how many setups leading from first here [start][end]
    for ii in range(m):
        tmp = [0]*m
        for jj in range(ii,m):
            tmp[jj] = (n-ii) % p
        mult.append(tmp)
    n -= 1
    print(mult)
    while n != 0:
        if n % 2 == 1:
            if matrix == None:
                matrix = mult
            else:
                matrix = increment(matrix,mult,p)
        n //= 2
        mult = increment(mult,mult,p)
        print(mult)
    ans = m % p # depth 1
    for u in matrix: # depth n
        ans += sum(u)
    print(ans % p)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
can use bit representation to make this faster
12 -> [0,0,1,1,0,0,0...]
get sums for each row and col
use above to get total sum
for each element, bits of other elements is:
total - row - col + self (double count)
then can compare bit by bit

lol pypy.

There are about 5 minutes left in the contest,
getting another problem I haven't started is practically
impossible, thus will pause recording here until
the unrated problems are available in practice
"""


def solve(n,m,ar):
    if n == 1 or m == 1: return 0
    row = list()
    col = list()
    total = [0]*30
    for nntht in range(m):
        ttmp = [0]*30
        col.append(ttmp)
        
    for i in range(n):
        tmp = [0]*30
        for j in range(m):
            x = ar[i][j]
            index = 0
            while x != 0:
                if x % 2 == 1:
                    tmp[index] += 1
                    col[j][index] += 1
                x >>= 1
                index += 1
        row.append(tmp)

    if n < m:
        for aa in range(n):
            for bb in range(30):
                total[bb] += row[aa][bb]

    else:
        for aa in range(m):
            for bb in range(30):
                total[bb] += col[aa][bb]

    
    xy = n*m-n-m+1 #number of xor calcs for each element
    ans = 0
    for xx in range(n):
        rc = row[xx]
        for yy in range(m):
            s = ar[xx][yy]
            #fr = getar(total,row,col,xx,yy)
            tp = 0
            val = 1
            cc = col[yy]
            for index in range(30):
                av = total[index]-rc[index]-cc[index]
                if s % 2 == 1: av = xy-av-1
                tp += (av*val)
                s >>= 1
                val <<= 1    
            if tp > ans: ans = tp
    return ans
    
for i in range(readint()):
    n,m = readints()
    ar = list()
    for j in range(n):
        tmp = readar()
        ar.append(tmp)
    print(solve(n,m,ar))

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
check if cur vals are sorted, use min and see if sum can be attained
last-first = 6
1,2,3
4*1
maximum: 10 >= 5 -> Yes

last-first = 4
1,1,1,1
1*1
max: 5 = 5 -> Yes

last-first = 1
1
1*2
max: 3 < 4 -> No
"""

def solve(n,m,ar):
    if m == 1: return "Yes"
    br = list()
    for j in range(m-1):
        br.append(ar[j+1]-ar[j])
    low = br[0]
    br.reverse()
    for k in range(n-m):
        br.append(low)
    br.reverse()
    br.insert(0,ar[0]-sum(br[:n-m]))
    #print(br)
    for f in range(len(br)-1):
        if br[f] > br[f+1]: return "No"
    return "Yes"


for i in range(readint()):
    n,m = readints()
    ar = readar()
    print(solve(n,m,ar))
    

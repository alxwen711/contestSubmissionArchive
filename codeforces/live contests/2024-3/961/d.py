import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n is at most 2**18 (250k) and there are at most 18 characters

get some combination of the existing chars so that no more than
a gap of k exists between any of them

pretty sure the last character is forced to be a case (still checking)

could be a pseudo dp? may result in very high number of cases

k+2 length string going backwards, 2nd and 1st chr?
"""


def solve(n,c,k,s):
    
    

for _ in range(readint()):
    n,c,k = readints()
    s = readin()
    print(solve(n,c,k,s))

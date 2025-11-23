import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
some sort of dp equation

any length 1 array can be solved in cost 0
any length 2 array is the difference

either match it to the previous value or the next value

for each pair, must determine if there will be a skip or not
a skip marker cannot be used consecutively

try doing this method twice; once assuming no marker at start
second time assumes there is a marker at the start
alternatively, run with marker at start then shift?

repeat the array then find min across any n consecutive

this is still O(n^2)?

three choices are to extend the segment, full mutate, or skip

two and three segments are optimal

then this only has to be repeated a few times
"""

def segment(a,b,c):
    return max(a,b,c)-min(a,b,c)

def compute(n,ar):
    ans = [99999999999999999999]*(n+1)
    ans[0] = 0
    ans[2] = abs(ar[0]-ar[1])
    for i in range(3,n+1):
        ans[i] = min(ans[i-2]+abs(ar[i-1]-ar[i-2]),ans[i-3]+segment(ar[i-1],ar[i-2],ar[i-3]))
    return ans[-1]

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 99999999999999999999999999999
    for _ in range(4):
        ans = min(ans,compute(n,ar))
        ar.append(ar.pop(0))
    print(ans)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
subarray length * maximum
? l x -> starting subarray from l, smallest r that results in x, n+1 if fail
find m such that array can be split into subarrays where all scores are m
you must split into k subarrays

every value is at most n

you can ask n questions to get the maximum in the entire array

then there has to be some sort of limit on what m can be
if k > n//2, then at least 1 subarray has 1 value, so maximum can only be m
if n//2 >= k > n//3, either m or 2m

sample answer is 6
"""

def f(n,k,x):
    index = 1
    for i in range(k):
        if index == n+1: return False
        s = "? "+str(index)+" "+str(x)
        print(s,flush=True)
        j = readint()
        index = j+1
        if index == n+2: return False
    return index == n+1

def solve(n,k):
    # first obtain maximum of the array
    ma = n
    while True:
        v = ma*n
        s = "? 1 "+str(v)
        print(s,flush=True)
        x = readint()
        if x == n+1: ma -= 1
        else: break
    # depending on k, try several cases
    ans = -1
    for i in range(n//k):
        if f(n,k,(i+1)*ma): ans = (i+1)*ma
    s = "! "+str(ans)
    print(s,flush=True)
    r = readint()
    return r
    

for _ in range(readint()):
    n,k = readints()
    result = solve(n,k)
    if result == -1: break # failed testcase

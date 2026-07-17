import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
bitsets?
rekkles optimal strategy is to choose whatever is closest to pushing
a new bit in
poby strategy is to erase 1 bits when possible, prioritising
values closest to a new bit, then lowest values

11000000 always gets a bit push
11000000

only the last critical move actually matters
anything with multiple 1's will be pushed unless they can be removed

- check every bit except last one
- if 2+ 1's, +1 setup
- elif 1 at the end, +0.5
- else no bonus (only length)
- double values and then prefix
"""

def f(x):
    ans = x % 2
    oc = -ans
    while x != 1:
        oc += x % 2
        x //= 2
        ans += 2
    if oc != 0:
        if ans % 2 == 0: ans += 2
        else: ans += 1
    return ans

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    prefix = [0]
    for i in ar:
        prefix.append(f(i)+prefix[-1])
    #print(prefix)
    for _ in range(q):
        l,r = readints()        
        print((prefix[r]-prefix[l-1])//2)

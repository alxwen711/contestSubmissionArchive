import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
for each string, count much of the front and back
can be used
then can count pairs across both arrays for answer
"""

def front(n,s,t):
    ans = 0
    target = t[ans]
    for i in range(len(s)):
        if target == s[i]:
            ans += 1
            if ans == n: return n
            target = t[ans]
    return ans
def back(n,s,t):
    ans = 0
    target = t[-ans-1]
    for i in range(len(s)):
        if target == s[-i-1]:
            ans += 1
            if ans == n: return n
            target = t[-ans-1]
    return ans
n,t = map(str,sys.stdin.readline().split())
n = int(n)
nn = len(t)
ar = list()
br = list()
for i in range(n):
    s = sys.stdin.readline()[:-1]
    ar.append(front(nn,s,t))
    br.append(back(nn,s,t))

ar.sort()
br.sort()
br.append(999999999999999999999999)
br.reverse()
inc = n
ans = 0
for i in range(n):
    target = nn-ar[-i-1]
    while br[inc] < target:
        inc -= 1
    ans += inc
print(ans)

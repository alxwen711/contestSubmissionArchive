import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
binsearch to find the iteration of the string (not needed, str cap is 1 mil)
nkhpsjoas
n
k (n)
h (n,k)
hp (n,k) 
hps (n,k)
hj (n,k,s,p)
hjo (n,k,s,p)
a (n,k,s,p,o,j,h)
as
(n,k,s,p,o,j,h,s,a)
if same val then just keep
"""

ans = list()

for i in range(readint()):
    s = sys.stdin.readline()[:-1]
    n = readint()
    stack = list()
    ar = list()
    for j in range(len(s)):
        while len(stack) != 0:
            if s[j] < s[stack[-1]]: #pop
                ar.append(stack.pop())
            else: break
        stack.append(j)
    while len(stack) != 0:
        ar.append(stack.pop())
    ar.reverse()
    for l in range(len(s),0,-1):
        if n > l:
            n -= l
            ar.pop()
        else: break
    ar.sort()
    ans.append(s[ar[n-1]])

print(*ans,sep="")

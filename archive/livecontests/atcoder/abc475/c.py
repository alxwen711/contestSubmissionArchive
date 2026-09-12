import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
initially at town S
either keep going left, keep going right, or some sort of alternate
"""

n,s,l = readints()
ar = readar()

ans = 1
ptr = 0
left = [0]
right = [0]
for a in range(s-2,-1,-1):
    left.append(left[-1]+ar[a])
for b in range(s-1,n-1):
    right.append(right[-1]+ar[b])

# main left
ptr = len(left)-1
for rr in range(len(right)):
    rd = l-(2*right[rr])
    if rd < 0: break
    while left[ptr] > rd:
        ptr -= 1
    ans = max(ans,ptr+rr+1)


# only right
ptr = len(right)-1
for ll in range(len(left)):
    ld = l-(2*left[ll])
    if ld < 0: break
    while right[ptr] > ld:
        ptr -= 1
    ans = max(ans,ptr+ll+1)

print(ans)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
IF the longest subsequence does NOT span start to finish,
it is ALWAYS possible to +1 to the length
otherwise, compare each pair, if they are not adjacent
in pos or value, then +1 is still possible

if this is wrong, there's probably a situation in which
lis length increases by more than one
"""

n = readint()
ar = readar()
lis = list()
lis.append((ar[0],0))
prev = [-1]*n
le = [0]*n
le[0] = 1
last = 0
flag = False
for i in range(1,n):
    low = 0
    high = len(lis)-1
    while high-low > 1:
        mid = (low+high)//2
        if lis[mid][0] < ar[i]: low = mid
        else: high = mid
    if lis[low][0] >= ar[i]:
        le[i] = low+1
        lis[low] = (ar[i],i)
        if low != 0: prev[i] = lis[low-1][1]
    elif lis[high][0] >= ar[i]:
        le[i] = high+1
        lis[high] = (ar[i],i)
        if high != 0: prev[i] = lis[high-1][1]
    else: # new value
        prev[i] = lis[-1][1]
        last = i
        lis.append((ar[i],i))
        le[i] = len(lis)
ans = len(lis)
if last != n-1: ans += 1
else: # reconstruct from last, somehow
    index = n-1
    flag = False
    br = [index]
    for _ in range(ans-1):
        p = prev[index]
        if p+1 != index and ar[p]+1 != ar[index]:
            flag = True
            break
        index = p
        br.append(index)
    br.reverse()
    # last deperetae attempt to try and determine of alternate paths are possible
    for ii in range(n-1):
        if le[ii] != len(lis):
            if ii < br[lis[ii][1]] and ar[ii] < ar[br[lis[ii][1]]]:
                flag = True
                break
    if flag or index != 0: ans += 1
print(ans)
#print(prev)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
heap setup?
store min/max range restrictions
possible that even on fixed point can still be
repositioned
reposition at the end; if any continuous inc/dec,
then shift to lowest possible value
if wrong, likely due to screwed up ending
few cases tle, adveresial downshift setup
even still clearly wa on several cases
"""

n = readint()
ar = list()
for _ in range(n):
    a,b = readints()
    ar.append((a,b))
index = 0
ans = [-1]*n
low,high = ar[0][0],ar[0][1]
for i in range(n):
    #print(low,high)
    a,b = ar[i][0],ar[i][1]
    if a > high: #up shift
        for j in range(index,i):
            ans[j] = high
        ans[i] = a
        index = i+1
        low,high = a,b
    elif b < low: #down shift, may need readjust
        for j in range(index,i):
            ans[j] = low
        ans[i] = b
        # readjust
        for k in range(i-1,index,-1):
            ans[k] = max(ar[k][0],b,ans[k+1])
        for o in range(index,i):
            if ans[index] == low: index += 1
            else: break
            if index == i: index += 1
        #index = i+1
        low,high = a,b
    else: #restrict range
        low = max(low,a)
        high = min(high,b)
if index != n:
    for m in range(index,n):
        ans[m] = low
print(*ans)

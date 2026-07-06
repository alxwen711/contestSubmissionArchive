import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
TODO: figure out wtf is wrong here (or other variations)
"""

ar = list()
n = readint()
for i in range(n):
    a,b = readints()
    ar.append((a,b,i+1))

ar.sort()
flag = True
for j in range(n-1):
    if ar[j][1] > ar[j+1][1]:
        flag = False
        break

if flag: # solution exists
    print("Yes")
    ans = list()
    br = list()
    for _ in range(n+1):
        br.append(list())
    for ii in range(n):
        val = ar[ii][1]
        low,high = 0,n-1
        while high-low > 1:
            mid = (low+high)//2
            if val < ar[mid][0]: high = mid
            else: low = mid
        s = low
        if val < ar[low][0]: s = low
        elif val < ar[high][0]: s = high
        else: s = high+1
        br[s].append(ii)
    for k in range(n+1):
        cr = list()
        for l in range(len(br[k])):
            index = br[k][l]
            if ar[index][0] <= ar[index][1]: cr.append(ar[index][2])
            else: ans.append(ar[index][2])
        while len(cr) != 0:
            ans.append(cr.pop())
    print(*ans)
else: print("No")

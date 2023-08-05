import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
pos + pos always passes
neg + neg always fails
0 -> set to -n, must fail with all others
n -> set to n, must pass with all others
depending on number of 0's/n's, will limit possibilities
both cannot exist in the same array
everything else might be possible?
1 2 3 4
-3 -1 2 4
EXTRA RULES:
number of n's is min val for ALL values
n - number of 0's is max val for ALL values
number of pos vals must match with ar sum's parity
1 2 2 4 5
-4 -2 -1 3 5
how to deal with center heavy distribution??????
"""


for i in range(readint()):
    n = readint()
    ar = readar()
    br = deepcopy(ar)
    br.sort()
    minv = br.count(n)
    maxv = n-br.count(0)
    if br[0] < minv or br[-1] > maxv:
        print("NO")
        continue
    p = sum(br)
    flag = -1
    for j in range(n+1):
        #consider j negatives
        if j == 0:
            if br[0] >= n: 
                flag = 0
                break
        elif j == n:
            if br[-1] == 0:
                flag = n
                break
        else:
            if (n-j) % 2 == p % 2 and br[j-1] <= (n-j) and br[j] >= (n-j):
                flag = j
                break
    if flag == -1: print("NO")
    else:
        print("YES")
        print(flag)
        if flag == 0: #all positive
            ans = list()
            for nth in range(1,n+1):
                ans.append(nth)
            print(*ans)
        elif flag == n: #all negative
            ans = list()
            for nthu in range(1,n+1):
                ans.append(-nthu)
            print(*ans)
        else:
            posline = br[flag] # min val to receive positive
            cr = list()
            for k in range(n):
                x = ar[k]
                if x >= posline:
                    cr.append((x-(n-flag),-1,k)) #how many to beat, pos/neg val, index
                else:
                    cr.append((n-flag-x,1,k))
            cr.sort()
            print(cr)
            ans = [0]*n
            for snth in range(n):
                ans[cr[snth][2]] = -cr[snth][1]*(snth+1)
            print(*ans)




            

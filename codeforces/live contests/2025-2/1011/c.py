import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# x+k+y+k = (x+k)^(y+k), solve for k
"""
as long as both do not share 1 in the same bit area, then possible
100100100100100100100
 10010010010010010100

go from low to high


0 and 0 is fine
1 and 1 = must add here, only way to fix is to get a 01 case then 00/11 case
3 and 5 impossible? (no)
1100
1010

001
011

011
0001

9 and 11? 
1001
1101

0101
0011
"""
def increment(ar,index):
    for i in range(index,len(ar)):
        if ar[i] == 0:
            ar[i] = 1
            return
        else:
            ar[i] = 0
    ar.append(1) # carry over

def solve(x,y):
    if x == y: return -1
    ar = list()
    br = list()
    while x != 0:
        ar.append(x % 2)
        x //= 2
    while y != 0:
        br.append(y % 2)
        y //= 2
    """
    diff = len(br)-len(ar)
    if diff > 0:
        for _ in range(diff):
            ar.append(0)
    else:
        for _ in range(-diff):
            br.append(0)
    """
    ans = 0
    index = 0
    #print(ar)
    #print(br)
    while index != min(len(ar),len(br)):
        if ans > 10**18: return -1
        if ar[index] == 1 and br[index] == 1:
            flag = True
            tmp = list()
            for i in range(index-1,-1,-1):
                if ar[i] == 0 and br[i] == 0:
                    tmp.append(i)
                elif ar[i]+br[i] == 1: # fix here
                    ans += 2**i
                    flag = False
                    increment(ar,i)
                    increment(br,i)
                    for j in tmp:
                        ans += 2**j
                        increment(ar,j)
                        increment(br,j)
                    break
            if flag:
                ans += 2**index
                increment(ar,index)
                increment(br,index)
        index += 1
    return ans

for _ in range(readint()):
    x,y = readints()
    print(solve(x,y))

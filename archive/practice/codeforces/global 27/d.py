import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
presum/postsum diff
ar[sindex]*pow(2,sused) has to be more than tas lower than ar[i]*pow(2,stacks)

it IS possible to have multiple stacks

198 2 3 optimal is 198 1 6

at most 20 stacks, compute this as a literal stack setup
"""

def solve(n,ar):
    m = 1000000007
    # note: if stack difference exceeds 100 automatically push to end
    # only move the stacks to the next round if it's better
    stacklist = list()
    ans = [ar[0]]
    stacks = 0
    prefix = [0]
    while ar[0] % 2 == 0:
        stacks += 1
        ar[0] //= 2
    stacklist.append((0,0,stacks)) # start, end, how many stacks on end
    prefix.append(ar[0])
    for i in range(1,n):
        stacks = 0
        while ar[i] % 2 == 0:
            stacks += 1
            ar[i] //= 2
        prefix.append(ar[i]+prefix[-1])
        st = stacklist[-1][1]+1
        stacklist.append((st,i,stacks))
        while len(stacklist) != 1:
            mergestack = (stacklist[-2][0],stacklist[-1][1],stacklist[-2][2]+stacklist[-1][2])
            mm = min(stacklist[-1][2],stacklist[-2][2])+1
            if mergestack[2] > 100+max(stacklist[-1][2],stacklist[-2][2]):
                stacklist.pop()
                stacklist.pop()
                stacklist.append(mergestack)
            elif mergestack[1]*(2**(mergestack[2]-mm))+ar[stacklist[-1][1]] > (ar[stacklist[-2][1]]*(2**(stacklist[-2][2]-mm))+ar[stacklist[-1][1]]*2**(stacklist[-1][2]-mm)):
                stacklist.pop()
                stacklist.pop()
                stacklist.append(mergestack)
            else: break
        cc = 0
        for snth in stacklist:
            cc += prefix[snth[1]]-prefix[snth[0]]+ar[snth[1]]*pow(2,snth[2],m)
        ans.append(cc % m)
    print(*ans)
    #print(prefix)
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)

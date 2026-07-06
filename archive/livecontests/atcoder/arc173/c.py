import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
always at least 3
could attempt solving from 1 to n//2, then n back to n//2
after each subproblem, 0 -> 1 bin array
check segment contains index with differing 0/1 count
needs to be O(n log n)
14
7 14  6  8 10  2  9  5  4 12 11  3 13  1
5  3  3  7  3  3  3  5  3  3  5  3  3  3
hlhlhlhlhlxhlhlhlhlhl can also be lhlhlhlhlhlhxlhlhlhlhlhlh

1 9 2 8 3 7 4 6 5?
2 1 9 8 4 3 7 6 5

using above pattern, track how far it goes in each direction
can be done with tracking each adj pair (2*2 arrays needed with
1 having an offset of 1 for parity)

track distance extending in each direction (seg tree + bin search)
also check +1 on each side to see if extended 1 more

attempt as far left/right as possible, disable ends that full extend
(reaching an endpoint can count as inf)

(upsolving this later, very sure this is the intended sol but I have 8 mins left)
"""

def ar_seg(ar): #create "seg tree"
    s = list()
    tmp = deepcopy(ar)
    s.append(tmp)
    while len(s[-1]) != 1:
        tmp = list()
        for i in range(len(s[-1])//2):
            tmp.append(s[-1][2*i]+s[-1][2*i+1])
        s.append(tmp)
    return s


def query(ar,l,h): # seg tree query
    ans = 0
    for i in range(len(ar)):
        if l > h: break
        if l % 2 == 1:
            ans += ar[i][l]
            l += 1
        if r % 2 == 0:
            ans += ar[i][r]
            r -= 1
        l //= 2
        r //= 2
    return ans


def update(ar,index,d): #inc/dec index by d
    for i in range(len(ar)):
        if len(ar[i]) == index: break
        ar[i][index] += d
        index //= 2


n = readint()
ar = readar()
br = list()
for i in range(n):
    br.append((ar[i],i))
br.sort()
evenl = [0]*(n//2) # track pairs
oddl = [0]*(n//2) # even with +1 offset
evenh = [0]*(n//2) # track pairs
oddh = [0]*(n//2) # even with +1 offset
ref = [0]*n # ref table, 0 is higher, 1 is lower
sevenl = ar_seg(evenl)
soddl = ar_seg(oddl)
sevenh = ar_seg(evenh)
soddh = ar_seg(oddh)

ans = [0]*n
for j in range(n):
    index = br[j][1]
    # check both ends for distance lengths (consider hl/lh setups)

    # ans[index] = ?

    # update
    ref[index] = 1
    if index//2 != n//2: #check even arrays
        ia,ib = index//2*2,index//2*2+1
        if evenl[index//2] == 0 and ref[ia] == 1 and ref[ib] == 0:
            update(evenl,index//2,1)
        elif evenl[index//2] == 1 and (ref[ia] == 0 or ref[ib] == 1):
            update(evenl,index//2,-1)
        if evenr[index//2] == 0 and ref[ia] == 0 and ref[ib] == 1:
            update(evenr,index//2,1)
        elif evenr[index//2] == 1 and (ref[ia] == 1 or ref[ib] == 0):
            update(evenr,index//2,-1)
    if index != 0 and (index != n-1 or n % 2 == 1): #check odd arrays
        ia,ib = (index-1)//2*2,(index-1)//2*2+1
        if oddl[(index-1)//2] == 0 and ref[ia] == 1 and ref[ib] == 0:
            update(oddl,(index-1)//2,1)
        elif oddl[(index-1)//2] == 1 and (ref[ia] == 0 or ref[ib] == 1):
            update(oddl,(index-1)//2,-1)
        if oddr[(index-1)//2] == 0 and ref[ia] == 0 and ref[ib] == 1:
            update(oddr,(index-1)//2,1)
        elif oddr[(index-1)//2] == 1 and (ref[ia] == 1 or ref[ib] == 0):
            update(oddr,(index-1)//2,-1)

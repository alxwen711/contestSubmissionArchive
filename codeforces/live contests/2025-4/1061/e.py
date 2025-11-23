import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
beauty = largest increase in two vals l -> r
only the first 4 moves of the game will matter?

idk what happens if the first optimal has a tie

in either case this whole method is flawed in 3 1 2 1

brute force ALL first moves, then there's some realy scuffed
conditional logic?? even still this feels like its O(n^2)
"""

class Node:
    def __init__(self,i):
        self.highest = [i]
        self.lowest = [i]

def mergeNode(a,b):
    hr,lr = list(),list()
    for i in a.highest:
        hr.append(i)
    for i in a.lowest:
        lr.append(i)
    for i in b.highest:
        hr.append(i)
    for i in b.lowest:
        lr.append(i)
    hr.sort()
    lr.sort()
    hr.reverse()
    nn = Node(0)
    nn.highest = hr[:3]
    nn.lowest = lr[:3]
    return nn

def create_seg(n,ar):
    tmp = list()
    seg = list()
    for i in ar:
        tmp.append(Node(i))
    seg.append(tmp)
    while len(seg[-1]) > 1:
        tmp = list()
        for i in range(len(seg[-1])//2):
            tmp.append(mergeNode(seg[-1][2*i],seg[-1][2*i+1]))
        seg.append(tmp)
    return seg

def lowerquery(seg,l,r):
    li,ri = l,r
    ans = []
    for i in range(len(seg)):
        if li > ri: return ans
        if li % 2 == 1:
            for j in seg[i][li].lowest:
                ans.append(j)
            li += 1
            ans.sort()
            ans = ans[:3]
        if ri % 2 == 0:
            for j in seg[i][ri].lowest:
                ans.append(j)
            ri -= 1
            ans.sort()
            ans = ans[:3]
        li //= 2
        ri //= 2
    return ans


def upperquery(seg,l,r):
    li,ri = l,r
    ans = []
    for i in range(len(seg)):
        if li > ri: return ans
        if li % 2 == 1:
            for j in seg[i][li].highest:
                ans.append(j)
            li += 1
            ans.sort()
            ans.reverse()
            ans = ans[:3]
        if ri % 2 == 0:
            for j in seg[i][ri].highest:
                ans.append(j)
            ri -= 1
            ans.sort()
            ans.reverse()
            ans = ans[:3]
        li //= 2
        ri //= 2
    return ans


def query(n,seg,i,ar):
    lr,rr = None,None
    if i <= 3: lr = ar[:i]
    else: lr = lowerquery(seg,0,i-1)
    if i >= n-4: rr = ar[i+1:]
    else: rr = upperquery(seg,i+1,n-1)
    return lr,rr
from copy import deepcopy
for _ in range(readint()):
    n = readint()
    ar = readar()
    seg = create_seg(n,ar)
    # determine highest score for 3 moves if Alex goes first
    index = list()
    best = -99999999999999999999999999999999
    for i in range(n): # alex chooses i as the first lock
        lp,rp = query(n,seg,i,ar)
        ansvals = list()
        for l in lp:
            ansvals.append(ar[i]-l)
        for r in rp:
            ansvals.append(r-ar[i])
        ansvals.sort()
        if ansvals[-2] > best:
            best = ansvals[-2]
            index = list()
            index.append(i)
        elif ansvals[-2] == best:
            index.append(i)
    br = deepcopy(ar)
    ivals = deepcopy(index)
    print(ivals)
    n -= 1
    ans = 5789347589479857349853475345795739987935
    for ii in ivals:
        ar = br[:ii]+br[ii+1:]
        seg = create_seg(n,ar)
        # determine highest score for 3 moves if Alex goes first
        index = -1
        best = -99999999999999999999999999999999
        for i in range(n): # alex chooses i as the first lock
            lp,rp = query(n,seg,i,ar)
            ansvals = list()
            for l in lp:
                ansvals.append(ar[i]-l)
            for r in rp:
                ansvals.append(r-ar[i])
            ansvals.sort()
            if ansvals[-2] > best:
                best = ansvals[-2]
                index = i
        ans = min(ans,best)
    print(ans)

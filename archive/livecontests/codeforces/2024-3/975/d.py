import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
max+max+1 is the baseline

1 under max needs 3 elements red in total to exceed baseline

it is always suboptimal to ignore highest value

dp states?

onion join on highest to lowest allowed values to track total
number of choosable

iterating backwards

also parity check to make sure the largest can be chosen
if this is impossible then subtract 1
even subsegments just need the maximum contained
odd subsegments need even/odd parity
"""

class Node:
    def __init__(self,ii):
        self.size = 1
        self.parent = -1
        self.start = ii
        self.hasmax = 0
        
def getParent(nodes,x):
    index = x
    while nodes[index].parent != -1:
        index = nodes[index].parent
    return index

def binTable(ar):
    br = [0]
    for i in range(len(ar)):
        br.append(br[-1]+ar[i])
    return br

def hm(even,odd,l,r):
    n = r-l+1
    if n % 2 == 0: # both arrays
        return even[r//2+1]-even[l//2]+odd[r//2+1]-odd[l//2] != 0 
    elif l % 2 == 0: # only even
        return even[r//2+1]-even[l//2] != 0
    else: # only odd
        return odd[r//2+1]-odd[l//2] != 0 
    
def solve(n,ar):
    br = list()
    for i in range(n):
        br.append((ar[i],i))
    br.sort()
    br.reverse()
    ma = br[0][0]
    nodes = list()
    evenbase = [0]*n
    oddbase = [0]*n
    for ii in range(n):
        nodes.append(Node(ii))
        if ar[ii] == ma:
            nodes[ii].hasmax = 1
            # do something else with ii
            if ii % 2 == 0: evenbase[ii//2] = 1
            else: oddbase[ii//2] = 1
    even = binTable(evenbase)
    odd = binTable(oddbase)
    #print(even,odd)
    h = [0]*n
    s = 0 # how many can be chosen
    ans = 0
    maxc = 0
    for j in range(n):
        mi = br[j][0]
        index = br[j][1]
        h[index] = 1
        maxc += nodes[index].hasmax
        s += 1
        if index != 0:
            if h[index-1] == 1:
                pa = getParent(nodes,index)
                pb = getParent(nodes,index-1)
                s -= (nodes[pa].size+1)//2
                s -= (nodes[pb].size+1)//2
                maxc -= nodes[pa].hasmax
                maxc -= nodes[pb].hasmax
                if nodes[pa].size > nodes[pb].size or nodes[pa].size == nodes[pb].size and pa < pb:
                    nodes[pb].parent = pa
                    nodes[pa].size += nodes[pb].size
                    nodes[pa].start = nodes[pa].start-nodes[pb].size
                    s += (nodes[pa].size+1)//2
                    # recompute nodes[pa].hasmax
                    nodes[pa].hasmax = hm(even,odd,nodes[pa].start,nodes[pa].start+nodes[pa].size-1)
                    maxc += nodes[pa].hasmax
                else:
                    nodes[pa].parent = pb
                    nodes[pb].size += nodes[pa].size
                    s += (nodes[pb].size+1)//2
                    # recompute nodes[pb].hasmax
                    nodes[pb].hasmax = hm(even,odd,nodes[pb].start,nodes[pb].start+nodes[pb].size-1)
                    maxc += nodes[pb].hasmax
        if index != n-1:
            if h[index+1] == 1:
                pa = getParent(nodes,index)
                pb = getParent(nodes,index+1)
                s -= (nodes[pa].size+1)//2
                s -= (nodes[pb].size+1)//2
                maxc -= nodes[pa].hasmax
                maxc -= nodes[pb].hasmax
                if nodes[pa].size > nodes[pb].size or nodes[pa].size == nodes[pb].size and pa < pb:
                    nodes[pb].parent = pa
                    nodes[pa].size += nodes[pb].size
                    s += (nodes[pa].size+1)//2
                    # recompute nodes[pa].hasmax
                    nodes[pa].hasmax = hm(even,odd,nodes[pa].start,nodes[pa].start+nodes[pa].size-1)
                    maxc += nodes[pa].hasmax
                else:
                    nodes[pa].parent = pb
                    nodes[pb].size += nodes[pa].size
                    nodes[pb].start = nodes[pb].start-nodes[pa].size
                    s += (nodes[pb].size+1)//2
                    # recompute nodes[pb].hasmax
                    nodes[pb].hasmax = hm(even,odd,nodes[pb].start,nodes[pb].start+nodes[pb].size-1)
                    maxc += nodes[pb].hasmax
        #print(h,mi,s,maxc)
        ans = max(ans,ma+mi+s-1+min(maxc,1))
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))

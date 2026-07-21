import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
each game is independent, can use a segtree type case to figure out


11001100 4 -> 8, needs 2 ops
111000111 3 -> 9, needs 3 ops
1111 1 -> 4, needs 2 ops

1111 -> 1010

111000111
101010101
010010010

11011 needs 1 op (10101)
11011 + 01010 -> 10001, only one change to make this monotonic
error count + 1 // 2

1111111 -> 0101010
assume number of disjoint minority segments is the answer
then the number of unique segments can be used; (flaws+1)//2
"""

def create_segs(n,s):
    # create easy refs for first and last characters
    first = list()
    last = list()
    tmp = list()
    flip = 0
    for i in s:
        v = int(i) ^ flip
        tmp.append(v)
        flip ^= 1
    first.append(tmp)
    last.append(tmp)
    while len(first[-1]) != 1:
        tmp = list()
        tmp2 = list()
        for i in range(len(first[-1])//2):
            tmp.append(first[-1][2*i])
            tmp2.append(last[-1][2*i+1])
        first.append(tmp)
        last.append(tmp2)
    flaws = list()
    tmp = [0]*n
    flaws.append(tmp)
    for u in range(1,len(first)):
        nextlevel = list()
        for g in range(len(first[u])):
            base = flaws[u-1][2*g]+flaws[u-1][2*g+1]
            if last[u-1][2*g] != first[u-1][2*g+1]: base += 1
            nextlevel.append(base)
        flaws.append(nextlevel)
    return first,last,flaws


def query(li,ri,first,last,flaws):
    # determine all of the segments to be used in order
    l,r = li,ri
    leftsegs = list()
    rightsegs = list()
    for i in range(len(flaws)):
        if l > r: break
        if l % 2 == 1:
            leftsegs.append((i,l))
            l += 1
        if r % 2 == 0:
            rightsegs.append((i,r))
            r -= 1
        l //= 2
        r //= 2
    rightsegs.reverse()
    seglist = leftsegs+rightsegs

    # combine the segments for the answer
    ans = 0
    prev = -1
    for s in seglist:
        a,b = s[0],s[1]
        ans += flaws[a][b]
        if prev != -1:
            if first[a][b] != prev: ans += 1
        prev = last[a][b]
    return ans

for _ in range(readint()):
    n,q = readints()
    s = readin()
    first,last,flaws = create_segs(n,s)
    for _ in range(q):
        l,r,k = readints()
        flawcount = query(l-1,r-1,first,last,flaws)
        print("YES" if (flawcount+1)//2 <= k else "NO")


              

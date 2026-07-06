import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
binary ideas can work, lt binary fails due to string size
might be possible to iterate through each char of b as lt binary
track occurance of each letter in a in the string, with regards
to location; then for call of some freq, can determine how many
cycles of s are needed to complete and where it lands as new index

note that a lookup table of size sl can be made for each character
so that a binary search is NOT needed to track how many are left
for each cycle, this feels like a case where O(n log n) and
O(n log n log n) can screw python over
"""

n = readint()
s = sys.stdin.readline()[:-1]
t = sys.stdin.readline()[:-1]
sl,tl = len(s),len(t)

# track letters
ar = list()
for _ in range(26):
    tmp = list()
    ar.append(tmp)
for i in range(sl):
    ar[ord(s[i])-97].append(i)

# construct lookup tables
br = list()
for j in range(26):
    if len(ar[j]) == 0:
        tmp = [0]*(sl+1)
        br.append(tmp)
    else:
        tmp = list()
        index = 0
        ss = len(ar[j])
        tmp.append(ss)
        for k in range(sl):
            if ar[j][index] == k:
                index += 1
                ss -= 1
            tmp.append(ss)
            if ss == 0: break
        while len(tmp) != (sl+1):
            tmp.append(0)
        br.append(tmp)
        #print(j,tmp,ar[j])

def trial(n,x,t,ar,br,tl):
    if x == 0: return True
    pos = 0
    run = 0
    for i in range(tl):
        if run == n: return False # reached end
        index = ord(t[i])-97
        fullcount = len(ar[index])
        if fullcount == 0: return False # chr not existing in s
        # does base cycle work
        remain = br[index][pos]
        if remain >= x: # no new cycle needed
            pos = ar[index][fullcount-(remain-x)-1]+1
        else:
            target = x-remain
            run += 1 # pos = 0
            rr = target//fullcount
            if rr > (n-run): return False # not enough full runs to complete
            run += rr
            if target % fullcount == 0: # possible to backtrack a bit
                run -= 1
                pos = ar[index][-1]+1
            else:
                if run == n: return False # exhausted all cycles
                pos = ar[index][(target % fullcount)-1]+1
    return True
low = 0
high = 10**18 #~60 trials required
while high-low > 1:
    mid = (low+high)//2
    if trial(n,mid,t,ar,br,tl): low = mid
    else: high = mid

ans = high
if not trial(n,high,t,ar,br,tl): ans = low
print(ans)

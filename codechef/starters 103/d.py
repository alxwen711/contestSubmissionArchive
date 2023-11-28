import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
longest subsequence cannot contain any squares
NOT subsegment

[a,b,c,d]
if ab is a square and cd is a square, abcd is a square
also abc/bcd are not squares if a,b,c,d are not squares
but by this rule ad/bc/bd/ac are also squares?
3,12,3,12
3,12,75,27
every value in the subsequence is base val*square

this method is 1.5 billion worst case
(last testcase is definitely hitting close to this somehow)

the 10 million list method might have been the solution, rip

can remove 1 case
removing 1 and 4 cases is enough to pass, but
it can be made faster by continuing to remove
up to a certain point
"""

x = 1
sq = list()
ssq = {}

while x*x <= 10000000:
    ssq[x*x] = 1
    sq.append(x*x)
    x += 1

ref = {}


for iiii in range(7,len(sq)):
    squ = sq[iiii]
    xv = squ
    for base in range(2,(10000000//(squ))+1):
        xv += squ
        if ssq.get(base) == None:
            if ref.get(xv) == None: ref[xv] = list()
            ref[xv].append(base)
#print(len(ref))

def solve(ar):
    n = len(ar)
    if n <= 1: return n
    d = {}
    for i in ar:
        #if lv.get(i) == None: lv[i] = compute(i)
        if ref.get(i) != None:
            for lll in ref[i]:
                if d.get(lll) == None: d[lll] = 0
                d[lll] += 1
        #1 case
        if d.get(i) == None: d[i] = 0
        d[i] += 1

        #4 case
        if i % 4 == 0:
            i4 = i//4
            if d.get(i4) == None: d[i4] = 0
            d[i4] += 1
        """
        everything here is overkill, but just for going faster
        note this can't be done infinitely due as
        eventually the extra 500000 potential calculations
        outweighs the cost of making comparatively fewer lists
        """
        #9 case
        if i % 9 == 0:
            i9 = i//9
            if d.get(i9) == None: d[i9] = 0
            d[i9] += 1

        #16 case
        if i % 16 == 0:
            i16 = i//16
            if d.get(i16) == None: d[i16] = 0
            d[i16] += 1

        #25 case
        if i % 25 == 0:
            i25 = i//25
            if d.get(i25) == None: d[i25] = 0
            d[i25] += 1

        #36 case
        if i % 36 == 0:
            i36 = i//36
            if d.get(i36) == None: d[i36] = 0
            d[i36] += 1

        #49 case
        if i % 49 == 0:
            i49 = i//49
            if d.get(i49) == None: d[i49] = 0
            d[i49] += 1

    ans = 0
    for snth in d.keys():
        ans = max(ans,d[snth])
    return ans
    
for i in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    for j in ar:
        if ssq.get(j) == None: br.append(j)
    print(solve(br))

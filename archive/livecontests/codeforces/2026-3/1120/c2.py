import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy is to find a set
hard is to find number of sets

for easy part, use some sort of greedy??

0 3 2 2 2 1
0 -> nothing in 0
3 -> something in 0-1,2-3,4-5,nothing in 6 (not that that's possible)
2 -> something in 0-2 and 3-5
.
.
1 -> something in 0-5

start from full set, determine what has to be removed
(counting would then be what could be removed?)

first testcase has the following sets:
125
135
1235
1245
1345
12345
essentially 1 and 5 are forced, 145 not allowed, at least one of 234 exists

012345 case leads to 632221

each segment has a few possible conditions:
- everything must be removed (exact val)
- at least 1 value is present (lower case)
- whatever (upper case)

12345 is the maximal set
1 23 45
12 345
123 45
1234 5
12345

(minimal cover of the set)

you cannot remove any of these sets fully

then removing the 1 and 5:
 23

then from free 234, you cannot have 2 and 3 both removed

another way is that 1 23 5 are the restricting conditions
so a superceding set question is built here

just start from the smallest sets, then see if there is any subsetting

1 condition: div 2
2 condition: div 4, times 3
3 condition: div 8, times 7

assume there is no such weird overlap case

123456789 maximal set (n = 10, 0 5 4 3 2 2 2 2 2 1)
01 23 45 67 89
012 345 678 9
0123 4567 89
01234 56789
012345 6789
0123456 789
01234567 89
012345678 9
0123456789

1456789
x
1 x
1 45 678 9 x
1 4567 89 x
1 5689 x
...

01
012 345 678 9
0123 4567 89
01234 56789



only consider the length 1 subsets first, then consider any non overlapping
length 2 subsets

inserting segments in the middle is where this all gets completely fucked

cannot be from minimal set and build upwards,
even if inclusion/exclusion that just goes back to maximal set
"""

m = 1000000007

two = [1,2]
for _ in range(100000):
    two.append(two[-1]*2 % m)



for _ in range(readint()):
    n = readint()
    ar = readar()
    conditions = list()
    for i in range(n):
        l = ar[i]*(i+1)
        h = l+i+1
        conditions.append((l,1))
        conditions.append((h,-1))
    conditions.sort()
    ptr = 0
    p = 0
    h = [0]*n
    cc = 0
    for j in range(n):
        while ptr < len(conditions):
            if conditions[ptr][0] <= j:
                p += conditions[ptr][1]
                ptr += 1
            else: break
        if p == 0:
            h[j] = 1
            cc += 1
    # h now contains the maximal set allowed
    ans = pow(2,cc,m)
    prefix = [0]
    for ii in h:
        prefix.append(prefix[-1]+ii)

    # make high/low trackers, each query case must exist
    nhigh = [99999999]*n
    actual = 99999999
    for ii in range(n-1,-1,-1):
        if h[ii]: actual = ii
        nhigh[ii] = actual

    nlow = [-99999999]*n
    actual = -99999999
    for ii in range(n):
        if h[ii]: actual = ii
        nlow[ii] = actual
    

    lr = []
    hr = []

    for i in range(n):
        for j in range(ar[i]): # number of conditions to check
            low = nhigh[j*(i+1)]
            high = nlow[low + i]
            if len(lr) == 0:
                lr.append(low)
                hr.append(high)
                continue
            if low > high[-1]: # assume no weird overlaps
                lr.append(low)
                hr.append(high)
                continue
            # determine if this is fully subsetting
            

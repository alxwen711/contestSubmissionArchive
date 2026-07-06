import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

m = 676767677

"""
x 1's, y -1's
if there is a -1, split to end


1 1 -1 -1

1 1 1 1 1 -1

5 3
1 1 1 1 1 -1 -1 -1


3 4
1 1 1 -1 -1 -1 -1 -1 -1

odd length is definitely 1 partition
if x == y, must be 1
x and y are even, must be 1

1 1 1 1 -1 -1

x and y are odd, must be 2

how drunk are we

1   ?????      1 1 1 -1 -1

x and y are even or x and y are odd MUST be 2 IF x != y


1 4 screws this thinking up
1 -1 -1 | -1 | -1

3 6?
1 1 1 -1 -1 -1 -1 -1 -1

is the current setup not actually correct??

3 1
1 1 -1 1

6 4
1 -1 -1 -1 1 -1 1 1 1 1

9 3, sums of 1/2/3/6 are all possible
1 1 1 1 1 1 1 1 1 -1 -1 -1

1 -1 1 -1 1 -1 1 1 1 1 1 1

7 4
1 -1 1 -1 1 -1 1 1 1 -1 1

the 1 case is the problem above, there has to be multiple setups somehow

1 1 1 1 -1 -1 -1 -1 -1 -1 -1
"""

for _ in range(readint()):
    x,y = readints()
    ans = list()
    for _ in range(x):
        ans.append(1)
    for _ in range(y):
        ans.append(-1)
    if x != 0 and y != 0:
        # compute number of factors
        d = abs(x-y)
        aans = 0
        c = 1
        while c*c < d:
            if d % c == 0: aans += 2
            c += 1
        if c*c == d: aans += 1
        if aans < 1: aans = 1
        print(aans)
    else: # why the hell is this here
        d = abs(x-y)
        aans = 0
        c = 1
        while c*c < d:
            if d % c == 0: aans += 2
            c += 1
        if c*c == d: aans += 1
        if aans < 1: aans = 1
        print(aans)
    print(*ans)
        

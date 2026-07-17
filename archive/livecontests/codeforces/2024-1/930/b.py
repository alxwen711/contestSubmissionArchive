import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
<><<<>
longest case: >>>><<<<

keep track of how many left and right boundaries there are
depending on direction is how many recoils there are, calc
distance from left/right bounces + exit

running sum arrays needed in all cases?
"""

for _ in range(readint()):
    n = readint()
    s = sys.stdin.readline()

    # right side
    lr = list()
    lrs = [0]
    rr = list()
    rrs = [0]
    for i in range(n):
        if s[i] == "<": lr.append(i)
        else: rr.append(i)
    lr.reverse()
    rr.reverse()
    for a in lr:
        lrs.append(lrs[-1]+a)
    for b in rr:
        rrs.append(rrs[-1]+b)
        
    # left side
    ll = list()
    lls = [0]
    rl = list()
    rls = [0]
    ans = list()
    
    for j in range(n):
        # remove right side indicator
        if s[j] == "<":
            lr.pop()
            lrs.pop()
        else:
            rr.pop()
            rrs.pop()

        # depending on direction, bounce check
        x = 0
        if s[j] == "<": # use rl and lr
            if len(rl) > len(lr):
                v = len(lr)
                # v+1 bounces on rl
                length = len(rls)
                inter = rls[length-1]-rls[length-v-1-1]
                x += (j*v+j-inter)*2

                # all bounces on lr
                x += (lrs[-1]-(v*j))*2
                
                # exit right
                x += (n-j)
                
            else:
                v = len(rl)
                # all bounces on rl
                x += (j*v-rls[-1])*2

                # v bounces on lr, sum of last v values
                length = len(lrs)
                inter = lrs[length-1]-lrs[length-v-1]
                inter -= (j*v)
                x += inter*2
                
                # exit left
                x += (j+1)
                
        else: # use lr and rl
            if len(rl) < len(lr):
                v = len(rl)
                # v+1 bounces on lr
                length = len(lrs)
                inter = lrs[length-1]-lrs[length-v-1-1]
                inter -= (j*v+j)
                x += inter*2

                # all bounces on rl
                x += (j*v-rls[-1])*2
                
                # exit left
                x += (j+1)
            else:
                v = len(lr)
                # all bounces on lr
                x += (lrs[-1]-(v*j))*2
                
                # v bounces on rl
                length = len(rls)
                inter = rls[length-1]-rls[length-v-1]
                x += (j*v-inter)*2
                
                # exit right
                x += (n-j)
        ans.append(x)
        
        # add to left side indicator
        if s[j] == "<":
            ll.append(j)
            lls.append(lls[-1]+j)
        else:
            rl.append(j)
            rls.append(rls[-1]+j)
    print(*ans)

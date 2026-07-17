import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
bit sets?
if even, alice divides longest even prefix by 2 
else, -1

main removal is having 1 in front and subtracting

definitely something involving the bitsets

1 10 11 is 6

10 10 10 10 is 5

110 1000 10 100 1 is 12
if alice makes no moves, Bob forces 1 as 2nd element to minimize movement

then changing to 1 -> forced full division
11 100 1 10 1 is reached in 2 moves, can only take 10 moves at most


1 11 101 111 1001 1010 1101 1111 is 35

when raising everything up to a certain base, then determine
if it can be raised further for optimal movement

penalty for a +1 post division is the base
"""

def minimalcase(x,penalty):
    ans = 764872348732923983729437934797434343443
    base = 1
    while True:
        v = (x+base-1)//base*base
        score = penalty*(v-x)
        while v != 1:
            score += ((v%2)+1)
            v //= 2
        score += 1
        ans = min(ans,score)
        if base > x: break
        base *= 2
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    mv = max(ar)
    base = 1
    ans = 9497239479238479237492379237929234923
    startscore = 0
    while True:
        br = list()
        score = startscore
        for a in ar:
            nv = (a+base-1)//base*base
            score += nv-a
            # compute score increment
            nv //= base # actual target being dealt with
            score += minimalcase(nv,base) # determine minimal value case            
        ans = min(ans,score)    
        if base > mv: break
        base *= 2
        startscore += 1
    print(ans)





    

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
alice's optimal is to choose the lowest of the remaining
bob's optimal is to remove entire values by frequency, then
by value
lt binary might be easier

using this process lt binary still exists

alice's strategy is always to choose lowest uneaten

bob plays an lt binary strategy
first check if clearing out a value from low to high can be done in time
then check if taking this move is necessary
(ie. are there fewer than the req moves left that are "better")
if so take it, else skip
"""

def f(x,br):
    r = 0
    index = 0
    hit = [1]*len(br) # this needs to be converted to seg tree (maybe)
    #print(br,cr,hit)
    for i in range(len(br)):     
        if hit[i] == 1: # alice chooses cr[i]
            hit[i] = 0
            # emulate bob's move here
            if r == 0: # determine new most optimal move
                if x == 0: return True # completed all blocks 
                else:
                    while index != len(br):
                        viable = True
                        req = br[index]
                        rem = sum(hit[i+1:index+1])
                        #print(index,req,rem)
                        if req > rem: viable = False
                        if hit[index] == 0: viable = False
                        if viable:
                            better = 0
                            for ii in range(index+1,len(br)):
                                if br[ii] <= req: better += 1
                            if better < x:
                                r = req-1
                                hit[index] = 0
                                index += 1
                                x -= 1
                                break
                            else: index += 1 # do not use (enough better options)
                        else:
                            index += 1 # do not use (impossible)
            else:
                r -= 1 # waiting out timer
    return x == 0 # possibly done all blocks?

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = list() # bob optimality
    #cr = list() # alice moves
    d = [0]*(n+1)
    for i in ar:
        d[i] += 1
    for j in range(n+1):
        if d[j] != 0:
            br.append(d[j])
            #cr.append(j)
    #print(br,cr)
    # run binary to track how many values can be blocked
    low = 0
    high = len(br)
    while high-low > 1:
        mid = (low+high)//2
        if f(mid,br): low = mid
        else: high = mid
    ans = low
    if f(high,br): ans = high
    print(len(br)-ans)

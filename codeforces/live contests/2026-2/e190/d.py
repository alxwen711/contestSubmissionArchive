import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
sequence of watching is always
1,2,3,4,5,...

only the x x segments are of significance,
everything else is capable of disrupting

searching for next episode is not quadratic

go from back to front for optimal continuations

only have to track the earliest disruptions + synchs

define another speed up for end position
"""
dummy = 9999999999999
anslist = list()
for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    ans = 0
    chains = [dummy]*n
    disruptions = [dummy]*(n+2)
    synch = [dummy]*(n+2)
    nextpos = [dummy]*n
    for i in range(n-1,-1,-1):
        # determine if initial position is viable
        if ar[i] == 1 and br[i] == 1:
            # found a chain start
            limit = -1
            ptr = i
            nextpos[i] = min(disruptions[2],synch[2])
            steps = [i]
            for index in range(2,n+1):
                limit = min(nextpos[ptr]-1,n-1)
                if limit == n-1: break
                if ar[limit+1] != index or br[limit+1] != index: break
                limit += 1 # can continue chain here
                ptr = limit
                if chains[ptr] != dummy:
                    limit = chains[ptr]
                    break
                steps.append(ptr)
            if limit == -1: limit = n-1
            for st in steps:
                chains[st] = limit
            ans += limit-i+1
        elif ar[i] != 1 and br[i] != 1:
            # determine if possible to link to chain
            if disruptions[1] <= synch[1]:
                vv = min(disruptions[1]-1,n-1)
                ans += vv-i+1
            else:
                vv = chains[synch[1]]
                ans += vv-i+1

        # update disruptions + synch
        if ar[i] == br[i]:
            synch[ar[i]] = i # this line can go backwards
            nextpos[i] = min(disruptions[ar[i]+1],synch[ar[i]+1])
        else:
            disruptions[ar[i]] = i
            disruptions[br[i]] = i
        
    anslist.append(str(ans))
    
sys.stdout.write("\n".join(anslist))

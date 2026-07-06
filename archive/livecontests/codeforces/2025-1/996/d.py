import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
pos just has to be at least l (could be higher)
the crow only considers scarecrows to the left of it

first move has to be moving first scarecrow to 0

not every scarecrow may be necessary

always use the closest? scarecrow,
eventually if the last one is used then the optimal play
is to just push the crow over to the finish

imagine the setup as a torch passing relay, only increment time if you need to

maximal position is pos+k
"""

for _ in range(readint()):
    n,k,l = readints()
    ar = readar()
    ans = ar[0]
    pos = k
    for i in range(1,n):
        if pos >= l: break
        p = ar[i]
        if p >= pos:
            if p-ans <= pos: # no time loss
                pos += k
            else:
                rd = p-ans-pos
                ans += (rd/2)
                pos += (rd/2)+k
        else:
            np = min(p+ans,pos)
            pos = max(pos,np+k)
        

    if pos < l: ans += l-pos
    print(round(ans*2))

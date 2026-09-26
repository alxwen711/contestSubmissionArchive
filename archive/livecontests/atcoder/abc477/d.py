import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
each square starts as colour a
tiles lock in colours
only if a square has odd tile place count, then only last one matters
arbritary locks at the end should be removed

alt method:
3 possible states for a tile:
open : uses most recent colour
closed : record last colour this square was, locked
exposed : open but no paintover has occurred yet, store in set

if type 2 query, all exposed become closed
if open, use previous, otherwise there is an answer
"""

n,q = readints()
h = [0]*n
ans = [""]*n
prev = "a"
exposed = set()
for _ in range(q):
    a,b = readins()
    a = int(a)
    if a == 1:
        b = int(b)-1
        if h[b] == 0:
            h[b] = 1
            ans[b] = prev
        elif h[b] == 1:
            h[b] = 2
            exposed.add(b)
        else:
            h[b] = 1
            exposed.remove(b)
    else:
        prev = b
        for e in exposed:
            h[e] = 0
            ans[e] = ""
        exposed = set()
for i in range(n):
    if ans[i] == "": ans[i] = prev
print(*ans,sep="")




        


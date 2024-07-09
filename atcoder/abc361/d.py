import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
s = readin()
t = readin()
s += ".."
t += ".."

"""
trivially requires W/B count to be equal
apart from that no other restrictions?

BBBWBWWWBBWWBW..
..BWBWWWBBWWBWBB

given small search size, looks like a possible graph search (BFS)
"""
d = {}
d[s] = 0
q = [s]
index = 0
while index != len(q):
    if q[index] == t: break
    v = d[q[index]]
    c = -1
    for i in range(n+2):
        if q[index][i] == ".":
            c = i
            break
    #print(q[index],c)
    # iterate through each potential combination
    for j in range(n+1):
        if q[index][j] != "." and q[index][j+1] != ".":
            ns = list()
            for ii in q[index]:
                ns.append(ii)
            #print(ns)
            ns[c] = ns[j][0]
            ns[c+1] = ns[j+1][0]
            ns[j] = "."
            ns[j+1] = "."
            
            ns = "".join(ns)
            #print(ns,j,c)
            if d.get(ns) == None:
                d[ns] = v+1
                q.append(ns)
    index += 1
#print(d)
if d.get(t) == None: print(-1)
else: print(d[t])

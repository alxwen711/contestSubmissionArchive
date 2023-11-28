import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
can only go up to at most to 200000 days and 200000 cities
can try every segment pair for 2 day scenarios

then only other option is spanning 2 to hit as many singles as possible

current blocking point:
choose two segments that cover most area
"""

for _ in range(readint()):
    n,m,k = readints() #k is always 2
    ar = list()
    st = list()
    ed = list()
    for i in range(m):
        a,b = readints() #segment boundaries
        ar.append((a,b))
        if st.get(a) == None: st[a] = list()
        st[a].append(i)
        if ed.get(b) == None: ed[b] = list()
        ed[b].append(i)
    marks = set()
    mc = 0
    ans = 0
    one = list()
    two = list()
    tl = {}
    for j in range(1,n+1):
        if st.get(j) != None:
            for x in st[j]:
                marks.add(x)
                mc += 1
        if mc == 0: ans += 1 #always dry
        if mc == 1: one.append(j)
        if mc == 2:
            two.append(j)
            aa = marks.pop()
            bb = marks.pop()
            tl[j] = (aa,bb)
            marks.add(aa)
            marks.add(bb)

        if ed.get(j) != None:
            for y in ed[j]:
                marks.remove(y)
                mc -= 1
    #try every two combinational here


    #translate each remaining segment into a singularity

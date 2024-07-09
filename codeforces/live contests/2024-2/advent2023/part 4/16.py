ar = list()
#input, default to basic integer reading file
f = open("16.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

print(len(ar),len(ar[0]),len(ar[-1]))
br = list()
for i in range(110):
    tmp = list()
    for j in range(110):
        tmp.append(ar[i][j])
    br.append(tmp)

def solve(br,q):
    d = {}
    """
    up,right,down,left
    """
    #q = [(0,0,2)]
    d[q[0]] = 1
    while len(q) != 0:
        x = q.pop()
        #determine if move is possible
        a,b,di = x[0],x[1],x[2]
        if a != 0 and di == 0:
            ns = br[a-1][b]
            if ns == "/": #right
                if d.get((a-1,b,1)) == None:
                    q.append((a-1,b,1))
                    d[(a-1,b,1)] = 1
            elif ns == "-": #left and right
                if d.get((a-1,b,1)) == None:
                    q.append((a-1,b,1))
                    d[(a-1,b,1)] = 1
                if d.get((a-1,b,3)) == None:
                    q.append((a-1,b,3))
                    d[(a-1,b,3)] = 1
            elif ord(ns) == 92: #left
                if d.get((a-1,b,3)) == None:
                    q.append((a-1,b,3))
                    d[(a-1,b,3)] = 1
            else: #up
                if d.get((a-1,b,0)) == None:
                    q.append((a-1,b,0))
                    d[(a-1,b,0)] = 1

        if b != 109 and di == 1:
            ns = br[a][b+1]
            if ns == "/": #up
                if d.get((a,b+1,0)) == None:
                    q.append((a,b+1,0))
                    d[(a,b+1,0)] = 1
            elif ns == "|": #ud
                if d.get((a,b+1,0)) == None:
                    q.append((a,b+1,0))
                    d[(a,b+1,0)] = 1
                if d.get((a,b+1,2)) == None:
                    q.append((a,b+1,2))
                    d[(a,b+1,2)] = 1
            elif ord(ns) == 92: #down
                if d.get((a,b+1,2)) == None:
                    q.append((a,b+1,2))
                    d[(a,b+1,2)] = 1
            else: #right
                if d.get((a,b+1,1)) == None:
                    q.append((a,b+1,1))
                    d[(a,b+1,1)] = 1

        if a != 109 and di == 2:
            ns = br[a+1][b]
            if ns == "/": #left
                if d.get((a+1,b,3)) == None:
                    q.append((a+1,b,3))
                    d[(a+1,b,3)] = 1
            elif ns == "-": #left and right
                if d.get((a+1,b,1)) == None:
                    q.append((a+1,b,1))
                    d[(a+1,b,1)] = 1
                if d.get((a+1,b,3)) == None:
                    q.append((a+1,b,3))
                    d[(a+1,b,3)] = 1
            elif ord(ns) == 92: #right
                if d.get((a+1,b,1)) == None:
                    q.append((a+1,b,1))
                    d[(a+1,b,1)] = 1
            else: #down
                if d.get((a+1,b,2)) == None:
                    q.append((a+1,b,2))
                    d[(a+1,b,2)] = 1
        if b != 0 and di == 3:
            ns = br[a][b-1]
            if ns == "/": #down
                if d.get((a,b-1,2)) == None:
                    q.append((a,b-1,2))
                    d[(a,b-1,2)] = 1
            elif ns == "|": #ud
                if d.get((a,b-1,0)) == None:
                    q.append((a,b-1,0))
                    d[(a,b-1,0)] = 1
                if d.get((a,b-1,2)) == None:
                    q.append((a,b-1,2))
                    d[(a,b-1,2)] = 1
            elif ord(ns) == 92: #up
                if d.get((a,b-1,0)) == None:
                    q.append((a,b-1,0))
                    d[(a,b-1,0)] = 1
            else: #left
                if d.get((a,b-1,3)) == None:
                    q.append((a,b-1,3))
                    d[(a,b-1,3)] = 1
    ans = 0
    dd = {}
    for e in d.keys():
        if dd.get((e[0],e[1])) == None:
            ans += 1
            dd[(e[0],e[1])] = 1
    #print(d)
    return ans


ans2 = 0
for aa in range(110):
    ans2 = max(ans2,solve(br,[(0,aa,2)]))
for aaa in range(110):
    ans2 = max(ans2,solve(br,[(109,aaa,0)]))
for aaaa in range(110):
    ans2 = max(ans2,solve(br,[(aaaa,0,1)]))
for aaaaa in range(110):
    ans2 = max(ans2,solve(br,[(aaaaa,109,3)]))

print(ans2)

import sys

def find(x,br,d,maxm):
    pre = [0]*(maxm+10)
    for g in range(len(br)):
         if br[g][0].count(x) != 0: pre[br[g][2]-d] += 1
    return pre


for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list()
    for aoe in range(n-1):
        tmp = list(map(int, sys.stdin.readline().split()))
        tmp.sort()
        tmp[0] -= 1
        tmp[1] -= 1
        ar.append(tmp)
    ar.sort()
    br = list()
    for snth in range(n):
        br.append([list(),list(),0])
    #[lineage, children]
    """
    create queue for nodes to complete
    dictionary to store tuples containing x
    if alt node has children/path, it is filled, don't edit
    else, edit
    """
    
    d = {}
    for ff in range(n):
        d[ff] = list()

    for hh in range(n-1):
        d[ar[hh][0]].append(ar[hh])
        d[ar[hh][1]].append(ar[hh])
    queue = list()
    queue.append(0)
    maxm = 0
    while len(queue) != 0:
        x = queue.pop(0)
        for s in range(len(d[x])):
            if d[x][s][0] != x: y = d[x][s][0]
            else: y = d[x][s][1]
            if len(br[y][0])+len(br[y][1]) == 0: #new node
                br[x][1].append(y)
                mmmmm = br[x][2]
                if mmmmm > maxm: maxm = mmmmm
                for k in range(mmmmm):
                    br[y][0].append(br[x][0][k])
                br[y][0].append(x)
                br[y][2] = br[x][2]+1
                queue.append(y)
    
    """
    for j in range(n-1):
        x,y = ar[j][0]-1, ar[j][1]-1
        br[x][1].append(y)
        for k in range(len(br[x][0])):
            br[y][0].append(br[x][0][k])
        br[y][0].append(x)
    """
    #print(br)
    target = 0
    ans = 0
    while True:
        if len(br[target][1]) == 0: break
        elif len(br[target][1]) == 1: #children count
            nod = br[target][1][0]
            for f in range(n):
                ans += br[f][0].count(nod)
            break
        else:
            anod,bnod = br[target][1][0], br[target][1][1]
            aa,bb = 0,0
            xxx = br[anod][2]+1
            aaa = find(anod,br,xxx,maxm)
            bbb = find(bnod,br,xxx,maxm)
            depth = 0
            prev = 0
            while True:
                aa += aaa[depth]
                bb += bbb[depth]
                if aa > bb:
                    ans += sum(aaa)
                    target = bnod
                    break
                elif bb > aa:
                    ans += sum(bbb)
                    target = anod
                    break
                elif prev == aa:
                    ans += prev
                    target = bnod
                    break
                else:
                    prev = aa
                    depth += 1
                    """
            #count by layers
            for g in range(n):
                aa += br[g][0].count(anod)
            for h in range(n):
                bb += br[h][0].count(bnod)
            if aa > bb:
                ans += aa
                target = bnod
            else:
                ans += bb
                target = anod"""
    print(ans)
            



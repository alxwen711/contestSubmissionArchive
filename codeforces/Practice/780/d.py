import sys
def solve(c,left,right):
    if len(c) == 0: return 0
    neg = list()
    twos = 0
    for e in range(right-left+1):
        if c[e] < 0: neg.append(e)
    if len(neg) % 2 == 0: #use entire section
        for w in range(right-left+1):
            if c[w] == 2 or c[w] == -2: twos += 1
        return left,right,twos
    
    else: #det which section is better
        tl = 0
        tr = 0
        la = left+neg[0]+1
        ra = left+neg[-1]-1

        #right adjusted
        for y in range(neg[-1]):
            if c[y] == 2 or c[y] == -2: tl += 1

        #left adjusted
        tmp = neg[0]+1
        for z in range(len(c)-neg[0]-1):
            if c[tmp+z] == 2 or c[tmp+z] == -2: tr += 1
        
        if tl > tr: return left,ra,tl
        else: return la,right,tr
            
    

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int,sys.stdin.readline().split()))
    zeros = list()
    for j in range(n):
        if ar[j] == 0: zeros.append(j)
    """
    a = st index
    b = end index
    v = num of 2s
    """
    if len(zeros) == 0: #scan full array
        a,b,v = solve(ar,0,n-1)
        if v == 0: print(str(n),"0")
        else: print(str(a),str(n-b-1))
    else:
        aa,bb,vv = 0,n,0
        if zeros[0] != 0: aa,bb,vv = solve(ar[:zeros[0]],0,zeros[0]-1)
        for k in range(len(zeros)-1):
            if zeros[k+1]-zeros[k] != 1:
                a,b,v = solve(ar[zeros[k]+1:zeros[k+1]],zeros[k]+1,zeros[k+1]-1)
                if v > vv:
                    aa = a
                    bb = b
                    vv = v
        if zeros[-1] != n-1:
            a,b,v = solve(ar[zeros[-1]+1:],zeros[-1]+1,n-1)
            if v > vv:
                aa = a
                bb = b
                vv = v
        if vv == 0: print(str(n),"0")
        else: print(str(aa),str(n-bb-1))

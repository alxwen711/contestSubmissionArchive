import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
#express the seg tree as a sparse table?
        
def seg_add(left, right, node, layer, indent, r, index): #increment function
    llr = indent
    rrr = indent + r - 1
    if left == llr and right == rrr:
        node[layer][index] += 1 #exact range covered by current node
        return
    #if node.lc == None: return seg_search(left,right,node.rc) #special last node case

    """
    current node has two children
    ll -> left child's left range
    lr -> left child's right range
    rl -> right child's left range
    rr -> right child's right range
    lv -> value from left side
    rv -> value from right side
    """
    inc = r//2
    ll,lr,rl,rr = llr,llr+inc-1,llr+inc,rrr
    #print(ll,lr,rl,rr,left,right)
    if left <= lr: #left child is involved
        if left == ll and right >= lr: #left child is fully in range
            node[layer+1][index*2] += 1
        else: seg_add(left,min(lr,right),node,layer+1,indent,inc,index*2)

    if right >= rl: #right child is involved
        if right == rr and left <= rl: #right child is fully in range
            node[layer+1][index*2+1] += 1
        else: seg_add(max(rl,left),right,node,layer+1,indent+inc,inc,index*2+1)
    


    
def solve(n,q,ar):
    #use seg tree to count num of freq of each position
    x = 1
    v = 0
    sparse = [[0]]
    while x < n:
        x <<= 1
        v += 1
        tmp = [0]*x
        sparse.append(tmp)
    #t = create_segtree(x)
    
    for i in range(q):
        l,r = readints()
        seg_add(l-1,r-1,sparse,0,0,x,0)

    #node = t
    dr = [sparse[0][0]]
    #print(dr)
    for j in range(1,v+1):
        bbr = [0]*len(sparse[j])
        for d in range(len(bbr)):
            bbr[d] = sparse[j][d]+dr[d//2]
        dr = bbr
        #print(dr)
        
    br = list()
    for jj in range(n): #find each freq of position
        br.append((dr[jj],jj))
    
    br.sort()
    ar.sort()
    ans = [0]*n
    total = 0
    for snth in range(n):
        xx = n-snth-1
        ans[br[xx][1]] = ar[xx]
        total += br[xx][0]*ar[xx]
    #print(sparse)
    #print(br)
    print(total)
    print(*ans)
    
for i in range(readint()):
    n,q = readints()
    ar = readar()
    solve(n,q,ar)

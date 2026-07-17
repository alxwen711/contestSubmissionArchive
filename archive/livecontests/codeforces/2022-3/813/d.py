import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
15
125
135
145
1425
absolute maximum is 10^9
if k = n-1, max(ar)*2, everything except max(ar) is 10^9
"""

class Tree:
    def __init__(self,val,lr,rr,lc,rc):
        self.val = val #value
        self.lr = lr #left range
        self.rr = rr #right range
        self.lc = lc #left child
        self.rc = rc #right child

def seg_func(a,b): #seg_tree function, edit this according to need
    # example for finding maximum of subarray
    return min(a,b)
    
        
def seg_search(left: int, right: int, node: Tree): #searching function

    if left == node.lr and right == node.rr: return node.val #exact range covered by current node
    if node.lc == None: return seg_search(left,right,node.rc) #special last node case

    """
    current node has two children
    ll -> left child's left range
    lr -> left child's right range
    rl -> right child's left range
    rr -> right child's right range
    lv -> value from left side
    rv -> value from right side
    """
    ll,lr,rl,rr = node.lc.lr,node.lc.rr,node.rc.lr,node.rc.rr
    lv,rv = 1000000009,1000000009 
    if left <= lr: #left child is involved
        if left == ll and right >= lr: #left child is fully in range
            lv = node.lc.val
        else: lv = seg_search(left,min(lr,right),node.lc)
    if right >= rl: #right child is involved
        if right == rr and left <= rl: #right child is fully in range
            rv = node.rc.val
        else: rv = seg_search(max(rl,left),right,node.rc)
    return seg_func(lv,rv)



def create_segtree(ar: list) -> Tree:
    ar_len = len(ar)

    #create a node for each element in the list, this is the bottom layer
    nodes = list()
    for i in range(ar_len):
        tmp = Tree(ar[i],i,i,None,None)
        nodes.append(tmp)

    #create parent nodes of previous layer
    while ar_len != 1:
        layer = list()
        for j in range(ar_len//2):
            left,right = nodes[2*j],nodes[2*j+1] #children of new node
            tmp = Tree(seg_func(left.val,right.val),left.lr,right.rr,left,right)
            layer.append(tmp)
            
        if ar_len % 2 == 1: #odd # of nodes, last node special case
            right = nodes[-1]
            tmp = Tree(right.val,right.lr,right.rr,None,right)
            layer.append(tmp)
            ar_len += 1
            
        #update top layer and ar_len
        ar_len = ar_len // 2
        nodes = layer
    return nodes[0] #only head node left in array


def sparse(ar):
    ans = list()
    ans.append(ar.copy())
    l = 1
    dist = 2
    while dist <= len(ar):
        tmp = list()
        for i in range(len(ar)-dist+1):
            #find [i:i+2**l]
            tmp.append(min(ans[l-1][i],ans[l-1][i+dist//2]))
        ans.append(tmp)
        l += 1
        dist *= 2
    return ans


def f(l,h,ar):
    length = h-l+1
    two = 1
    ex = 0
    while 2*two <= length:
        two = two*2
        ex += 1
    if length == two: return ar[ex][l]
    else: return min(ar[ex][l],ar[ex][h-two+1])

def solve(n,k,ar):
    if n == k: return 1000000000
    br = list()
    for j in range(n):
        br.append([ar[j],j])
    br.sort()
    a,b,t = -1,-1,None
    best = 1000000009    
    if k == 1: #no adjacency case
        best = -1
        ar[br[0][1]] = 1000000000
        t = sparse(ar)
        for ii in range(n-1):
            x = min(ar[ii],ar[ii+1])
            if x > best:
                best = x
                a,b = ii,ii+1
    else:
        for kk in range(k-1): #figure out optimal 1000000000 placement
            #intentionally save last placement to create adjacency if nonexistant
            x = br[kk][1]
            ar[x] = 1000000000
            if x != 0:
                if ar[x-1] == 1000000000: a,b = x-1,x
            if x != n-1:
                if ar[x+1] == 1000000000: a,b = x,x+1
        if b == -1: #must create adjacency
            index = -1
            bb = 1000000009
            for p in range(n):
                if ar[p] != 1000000000 and ar[p] < bb:
                    if p != 0:
                        if ar[p-1] == 1000000000:
                            index = p
                            bb = ar[p]
                            a,b = p-1,p
                    if p != n-1:
                        if ar[p+1] == 1000000000:
                            index = p
                            bb = ar[p]
                            a,b = p,p+1
            ar[index] = 1000000000
        else:
            ar[br[k-1][1]] = 1000000000
        t = sparse(ar)
        best = 1000000000
    two = 1000000099
    #print(ar)
    for m in range(n):
        if m < a:
            two = f(m,a,t)+f(m,b,t)
            best = min(two,best)
        if m > b:
            two = f(a,m,t)+f(b,m,t)
            best = min(two,best)
    return best

    
for i in range(readint()):
    n,k = readints()
    ar = readar()
    print(solve(n,k,ar))


import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
removing costs c, inserting costs d
always must be a singular of each value
seg tree, try lowest to highest
mark each one when done, inc seg tree as needed,
take sum for discount calculation
remaining values have to be in order
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
    return max(a,b)
    
        
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
    lv,rv = 0,0 
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

def solve(ar,ans,c,d):
    n = len(ar)
    
    


for i in range(readint()):
    n,c,d = readints()
    ar = readar()
    rm = {}
    br = list()
    ans = 0
    for j in range(n):
        x = ar[j]
        if rm.get(x) == None:
            rm[x] = 1
            br.append(x)
        else: ans += d
    print(solve(br,ans,c,d))

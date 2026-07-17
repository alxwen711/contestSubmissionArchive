import sys

class Tree:
    def __init__(self,val,lr,rr,lc,rc):
        self.val,self.lr,self.rr,self.lc,self.rc = val,lr,rr,lc,rc
        
def look(l,r,n):
    if l == n.lr and r == n.rr: return n.val
    if n.lc == None: return look(l,r,n.rc)
    #dual node setup
    a,b,c,d = n.lc.lr,n.lc.rr,n.rc.lr,n.rc.rr
    x,y = 0,0
    if l <= b: #left is involved
        if l == a and r >= b: #all left
            x = n.lc.val
        else: x = look(l,min(b,r),n.lc)
    if r >= c: #right is involved
        if r == d and l <= c: #all right
            y = n.rc.val
        else: y = look(max(c,l),r,n.rc)
    return max(x,y)


n,m = map(int,sys.stdin.readline().split())
ar = list(map(int,sys.stdin.readline().split()))
nodes = list()
for i in range(m):
    tmp = Tree(ar[i],i+1,i+1,None,None)
    nodes.append(tmp)
nl = m
while nl != 1:
    #print(nl,len(nodes))
    nn = list()
    for j in range(nl//2):
        left,right = nodes[2*j],nodes[2*j+1]
        tmp = Tree(max(left.val,right.val),left.lr,right.rr,left,right)
        nn.append(tmp)
    if nl % 2 == 1:
        right = nodes[-1]
        tmp = Tree(right.val,right.lr,right.rr,None,right)
        nn.append(tmp)
        nl += 1
    nl = nl // 2
    nodes = nn
head = nodes[0]
for k in range(int(sys.stdin.readline())):
    br = list(map(int,sys.stdin.readline().split()))
    if abs(br[0]-br[2]) % br[4] != 0 or abs(br[1]-br[3]) % br[4] != 0: sys.stdout.write("NO\n")
    else:
        best = n - ((n-br[0]) % br[4])
        req = look(min(br[1],br[3]),max(br[1],br[3]),head) + 1
        if req > best: sys.stdout.write("NO\n")
        else: sys.stdout.write("YES\n")
    

#153422624 is wrong
class queue:
    def __init__(self,limit=100000):
        self.q = list()
        self.pt = 0
        self.l = 0
        self.memRefresh = limit

    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        #check if memory needs to be refreshed
        if self.pt == self.memRefresh:
            self.pt = 0
            self.l -= self.memRefresh
            self.q = self.q[self.memRefresh:]
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self) -> int:
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l

class flipNode:
    def __init__(self,name):
        self.name = name
        self.connect = list()
        self.state = 0

class conNode:
    def __init__(self,name):
        self.name = name
        self.connect = list()
        self.req = 0
        self.val = 0
        self.parents = {} #mods that signal to this node

def response(n,s,v): #node,source,value
    if len(n.connect) == 0: return -1 #dead node
    if n.name[0] == "%": #flip
        if v == 1: return -1
        nv = n.state ^ 1
        n.state = nv
        return (n.name[1:],nv)
    else: #connect
        if n.parents[s] != v:
            n.parents[s] = v
            if v == 1: n.val += 1
            else: n.val -= 1
        if n.val == n.req: return (n.name[1:],0)
        return (n.name[1:],1)

ar = list()
#input, default to basic integer reading file
f = open("20.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

#need to track all connections that lead to each conjunction
ans = 0

br = list()
nodes = {}
pslist = list()
for i in ar:
    name,connected = i.split("->")
    name = name.rstrip()
    if name[0] == "%": #flipflop
        nodes[name[1:]] = flipNode(name)
        br.append((name,connected))
    elif name[0] == "&": #conjunc
        nodes[name[1:]] = conNode(name)
        br.append((name,connected))
    else: #broadcaster
        pslist = list(map(str,connected.split(",")))
        for k in range(len(pslist)):
            pslist[k] = pslist[k].rstrip()
            pslist[k] = pslist[k].lstrip()

print(pslist)
        
#fill in connections
for j in br:
    name = j[0][1:]
    children = list(map(str,j[1].split(",")))
    for k in range(len(children)):
        children[k] = children[k].rstrip()
        children[k] = children[k].lstrip()
    #print(children)
    for u in children:
        if nodes.get(u) == None: nodes[u] = flipNode(u)
        nodes[name].connect.append(u)
        if nodes[u].name[0] == "&": #connected node
            nodes[u].req += 1
            nodes[u].parents[name] = 0

#xl,ln,xp,gp
lp = 0
hp = 0
fr = [list(),list(),list(),list()]
for target in range(1,100000):
    q = queue()
    q.add(("broadcaster",0))
    lp += 1 #button to broadcaster
    while not q.empty():
        x = q.dequeue()
        if x[0] == "df":
            gr = list()
            index = 0
            for ii in ["xl","ln","xp","gp"]:
                gr.append(nodes["df"].parents[ii])
                if nodes["df"].parents[ii] == 1: fr[index].append(target)
                index += 1
            count = sum(gr)
            if count > 1:
                print(count,"hit",gr,"button press",target)
        if x[0] == "broadcaster":
            for nv in range(len(pslist)):
                if x[1] == 0: lp += 1
                else: hp += 1
                dr = response(nodes[pslist[nv]],x[0],x[1])
                if dr != -1: q.add(dr)
        else:
            for ev in range(len(nodes[x[0]].connect)):
                if nodes[x[0]].connect[ev] == "rx" and x[1] == 0:
                    print("ANSWER FOUND")
                    print(target)
                if x[1] == 0: lp += 1
                else: hp += 1
                dr = response(nodes[nodes[x[0]].connect[ev]],x[0],x[1])
                if dr != -1: q.add(dr)
    if target % 10000 == 0: print(target)
print(lp*hp)
print(lp,hp)


print("cycles")
print(fr[0])
print(fr[1])
print(fr[2])
print(fr[3])

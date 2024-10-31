from copy import deepcopy

#at least there's no infinite loop?
class Node:
    def __init__(self,name,rl):
        self.name = name
        self.rules = rl
ar = list()
#input, default to basic integer reading file
f = open("19.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    else: break    

br = list()
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        br.append(l)
    else: break

f.close()


def solve(ar,nodes,loc):

    #finish cases
    if loc == "R": return 0
    elif loc == "A":
        ans = 1
        for i in ar:
            ans *= (i[1]-i[0]+1)
        return ans

    #go through the rules
    ans = 0
    r = nodes[loc].rules
    for i in range(len(r)):
        rl = r[i]
        if rl.count(":") == 0: #either move, A, or R (last rule)
            ans += solve(ar,nodes,rl)
        else:
            con,nl = rl.split(":") #constraint, new location
            val = int(con[2:])
            index = 0
            if con[0] == "m": index = 1
            elif con[0] == "a": index = 2
            elif con[0] == "s": index = 3
            lr,hr = ar[index][0],ar[index][1]
            if con[1] == ">": #greater than
                if lr > val: #everything passes
                    ans += solve(deepcopy(ar),nodes,nl)
                elif hr > val: #some passes
                    br = deepcopy(ar)
                    br[index] = (val+1,hr)
                    ans += solve(br,nodes,nl)
                    ar[index] = (lr,val)
            else: #less than
                if hr < val:
                    ans += solve(deepcopy(ar),nodes,nl)
                elif lr < val:
                    br = deepcopy(ar)
                    br[index] = (lr,val-1)
                    ans += solve(br,nodes,nl)
                    ar[index] = (val,hr)
    return ans

print(ar[-1])
print(br[-1])
print(len(ar),len(br))

flag = True
nodes = {}
for i in ar:
    name,rulelist = i.split("{")
    rulelist = rulelist[:-1]
    rulelist = list(map(str,rulelist.split(",")))
    nodes[name] = Node(name,rulelist)
    if flag:
        print(name,rulelist)
        flag = False

ans = solve([(1,4000),(1,4000),(1,4000),(1,4000)],nodes,"in")
print(ans)

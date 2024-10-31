from math import gcd

ar = list()
#input, default to basic integer reading file
f = open("8.txt",'r')
moves = f.readline()[:-1]
f.readline()
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

print(moves)
#print(ar)


class Node:
    def __init__(self,name):
        self.name = name
        self.left = None
        self.right = None

d = {}

flag = True

pos = list()
for i in ar:
    head = i[0:3]
    l = i[7:10]
    r = i[12:15]
    if flag:
        print(head,l,r)
        flag = False
    if d.get(head) == None:
        d[head] = Node(head)
    n = d[head]
    if d.get(l) == None:
        d[l] = Node(l)
    if d.get(r) == None:
        d[r] = Node(r)
    n.left = l
    n.right = r
    if head[2] == "A": pos.append(head)
print(len(pos))
flag = False
ans = list()
for b in pos:
    pl = b
    for a in range(len(moves)*1000):
        mm = moves[a % len(moves)]
        #check if done
        if pl[2] == "Z": 
            ans.append(a)
            break
        if mm == "L": pl = d[pl].left
        else: pl = d[pl].right
print(len(moves))
print(ans)

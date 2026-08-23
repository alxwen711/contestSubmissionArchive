import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
represent each horizontal segment as a node
there is then some sort of DAG system from connecting vertically
goal is to remove as many - as possible with as few + as possible
process level by level, there can be at most 15 nodes at a level

on score and off score


2 0
 -1
 3
-2 0
-2 2

not a tree
"""
class Node:
    def __init__(self,s):
        self.score = s
        self.parents = set()
        self.children = set()

n,m = readints()
grid = list()
levels = list()
for lev in range(n):
    s = readin()
    tmp = [0]*m
    grid.append(tmp)
    levels.append(list())
    prev = 0
    for i in range(m):
        if s[i] == "#":
            if i != prev:
                score = 0
                for u in range(prev,i):
                    if s[u] == "+": score += 1
                    else: score -= 1
                node = Node(score)
                for v in range(prev,i):
                    grid[lev][v] = node
                levels[lev].append(node)
            prev = i+1
    if prev != m:
        score = 0
        for u in range(prev,m):
            if s[u] == "+": score += 1
            else: score -= 1
        node = Node(score)
        for v in range(prev,m):
            grid[lev][v] = node
        levels[lev].append(node)
for a in range(n-1):
    for b in range(m):
        if type(grid[a][b]) == Node and type(grid[a+1][b]) == Node:
            grid[a][b].children.add(grid[a+1][b])
            grid[a+1][b].parents.add(grid[a][b])
            
# then it's finding optimality somehow.......

"""
at each level, track the possible bit set scores
then for each level that goes upwards from this, each new best dp state
is the score from that level + the maximum score from valid configs

a valid config is that if the parent is activated, the child(ren) must be as well
do we use meet in the middle? find all valid configs on each side, get the maximum
of both, then combine these? then the splitting process gets very weird

all conditions are of the form 11*1*1*1 or similar
other idea is to use seg tree and aggresively search multi nodes until all conditions
are hit; to then deal with cases where extensive traversal may be required,
just use multiple trees??? how to configure the orders?
"""

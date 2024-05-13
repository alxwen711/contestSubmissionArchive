import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
bucket sort? track frequency of each letter in the trie
then if not 1, add (x*x-x)//2
"""

class Node:
    def __init__(self):
        self.val = 0
        self.children = {}

n = readint()
ar = list(map(str,sys.stdin.readline().split()))

root = Node()
for i in ar:
    cn = root
    for j in i:
        if cn.children.get(j) == None:
            cn.children[j] = Node()
        cn = cn.children[j]
        cn.val += 1
q = [root]
ans = 0
while len(q) != 0:
    nn = q.pop()
    x = nn.val
    ans += (x*x-x)//2
    for k in nn.children.keys():
        q.append(nn.children[k])
print(ans)

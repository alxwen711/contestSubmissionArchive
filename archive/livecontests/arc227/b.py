import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
0 1 0 3
0 1 1 3 4 4 6
0 1 1 1 4 0 6

0 can be placed at any point
the string must start with a 0
only way 1's can go in is with a single 0 before it

0's are special, all other integers are inputted greedily

0 1 2 3 3 3 2 2 2 1 1 0
"""

n = readint()
ar = readar()
d = {}
for i in ar:
    if d.get(i) == None:
        d[i] = 0
    d[i] += 1

br = list()
for j in d.keys():
    br.append((j,d[j]))
br.sort()
s = list() # stack
ans = list()
if br[0][0] == 0:
    for _ in range(br[0][1]):
        s.append(0)

ptr = 1
v = 0
while len(s) != 0:
    if ptr == len(br):
        ans.append(s.pop())
        continue
    ans.append(s.pop())
    v += 1
    if br[ptr][0] == v:
        for _ in range(br[ptr][1]):
            s.append(br[ptr][0])
        ptr += 1
if len(ans) == n:
    print("Yes")
    print(*ans)
else:
    print("No")


    

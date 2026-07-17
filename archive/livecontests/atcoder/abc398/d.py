import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
In second testcase, find substrings that equate to SEE
keep running sum and find if the inverse exists
"""

n,r,c = readints()
s = readin()
x,y = 0,0
d = {}
d[(0,0)] = 0
ans = list()
for i in s:
    if i == "N": x -= 1
    elif i == "S": x += 1
    elif i == "W": y -= 1
    else: y += 1
    tx,ty = x-r,y-c
    if d.get((tx,ty)) != None: ans.append(1)
    else: ans.append(0)
    d[(x,y)] = 1
print(*ans,sep="")

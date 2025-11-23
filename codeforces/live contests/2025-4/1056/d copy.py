import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
PIGEONHOLE YOUEUTEOUHOEUHEUORCHAEUIDORGAEOIUADUIONCGDAPUOENCGIAUONIAPODRLGAIP,ADAPD,CHIAP,DCHL

"""

def solve(n):
    d = {}
    q = [(1,n)]
    ptr = 0
    while True:
        x,y = q[ptr]
        dist = y-x+1
        if dist <= 3: break
        q.append((x,x+dist//2-1))
        q.append((x+dist//2,y))
        ptr += 1
    q.reverse()
    for i in q:
        for a in range(i[0],i[1]):
            for b in range(a+1,i[1]+1):
                if d.get((a,b)) == None:
                    d[(a,b)] = 1
                    print(a,b)
                    flush()
                    x = readint()
                    if x != 0: return x
    return -1

for _ in range(readint()):
    x = solve(readint())
    if x == -1: break
    


import sys
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
1,2,5,19,102,682,5321,47071,464570,5057058
1,3,8,25,114,714,5456,47889,470710,5177810
0,1,3,6 ,12 , 32, 135,  818,  6140,120752
"""

m = 998244353
ar = [0,0,1,2,5]
br = [0,0,2]
for i in range(1000000):
    br.append((br[-1]*(len(br)+2) + len(br)) % m)
    x,y = ar[-2],ar[-1]
    z = br[-1]-br[-2]
    ar.append((z+2*y-x) % m)

#print(br[:10])
#print(ar[:10])
for _ in range(readint()):
    print(ar[readint()])
"""
ar = [0,1]
br = list()
br.append(ar)
for i in range(9):
    cr = list()
    for a in br:
        invc = 0
        for x in range(i+1):
            for y in range(x+1,i+2):
                if a[x] > a[y]: invc += 1
        for l in range(len(a)+1):
            snth = deepcopy(a)
            snth.insert(l,invc)
            cr.append(snth)
    cr.sort()
    br = list()
    br.append(cr[0])
    for snthsnth in range(len(cr)-1):
        if cr[snthsnth] != cr[snthsnth+1]: br.append(cr[snthsnth+1])
#print(br)
print(len(br))
"""

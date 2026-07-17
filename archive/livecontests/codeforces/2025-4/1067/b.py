import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
odd freq cases (there must be an even number of these)
+1 each time, favour alternatively

even freq
if div by 4, must create imbalance of 2 or more
    there is an even number of these imbalances -> fine
    there is an odd number of these imbalances -> at least 1 non-4 val else -1
if not div by 4
    could create imbalance of 4 if needed above (6 or higher)

111234
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    h = [0]*(2*n+1)
    for i in ar:
        h[i] += 1
    ans = 0
    ec = 0
    bf = 0
    twomod = list()
    fourmod = list() # must create a diff two
    for j in range(2*n+1):
        if h[j] != 0:
            if h[j] % 2 == 1:
                ans += 1
                bf += h[j]
            elif h[j] % 4 == 0:
                fourmod.append(h[j])
            else:
                twomod.append(h[j])
    if len(fourmod) % 2 == 0 or bf >= 2:
        print((len(fourmod)+len(twomod))*2+ans)
    else:
        print((len(fourmod)+len(twomod)-1)*2+ans)







            

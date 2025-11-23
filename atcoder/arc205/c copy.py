import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
blatantly obvious implemnatation
"""

ar = list()
n = readint()
for i in range(n):
    a,b = readints()
    ar.append((a,b,i+1))

ar.sort()
flag = True
for j in range(n-1):
    if ar[j][1] > ar[j+1][1]:
        flag = False
        break

if flag: # solution exists
    print("Yes")
    br = list()
    cr = list()
    for k in ar:
        if k[0] > k[1]:cr.append(k[2])
        else: br.append(k[2])
    br.reverse()
    dr = br+cr
    print(*dr)

else: print("No")

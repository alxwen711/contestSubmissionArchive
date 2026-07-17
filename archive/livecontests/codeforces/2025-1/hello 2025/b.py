import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
1 2 1 2 1 2 ?
number of unique values
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    d = {}
    for i in ar:
        if d.get(i) == None: d[i] = 0
        d[i] += 1
    br = list()
    for j in d.keys():
        br.append(d[j])
    br.sort()
    br.reverse()
    while len(br) > 1:
        if k >= br[-1]:
            k -= br[-1]
            br.pop()
        else: break
    print(len(br))

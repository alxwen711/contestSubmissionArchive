import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1,2,3,4,5,6,7,8,9,10,12...,21,23...,32,34

1 digit -> 9 numbers
2 digits -> 90-9 = 81 numbers
3 digits -> 9**3 numbers

148 - 90 = 58th 3-digit
58 in base 9 = 064 -> 173
"""
p = list()
p.append(1)
for _ in range(17):
    p.append(p[-1]*9)
    
for _ in range(readint()):
    n = readint()
    n -= 1
    dc = 1
    while n > p[dc]:
        n -= p[dc]
        dc += 1
    flag = False
    if n == p[dc]: flag = True
    ar = list()
    while n != 0:
        ar.append(n % 9)
        n //= 9
    while len(ar) < dc:
        ar.append(0)
    if flag: ar[-1] = 0
    #print(ar)
    ar.reverse()
    ar[0] += 1
    for i in range(1,len(ar)):
        if ar[i] >= ar[i-1]: ar[i] += 1
    #print(ar)
    for snth in range(len(ar)):
        ar[snth] = str(ar[snth])
    ans = "".join(ar)
    print(ans)

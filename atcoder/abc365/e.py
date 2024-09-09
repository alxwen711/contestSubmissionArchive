import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
every subsequence not including length 1
for each bit, label as 0/1 if val has it or not
[1,1,0,1,0,1,1,0,1,0,0,0,1]...
how many of these subarrays have an odd count of ones?
this looks possible in linear time, so O(n log n)
"""

n = readint()
ar = readar()
ans = 0
for i in range(30):
    v = 2**i
    br = list()
    for a in range(n):
        if ar[a] & v != 0: br.append(1)
        else: br.append(0)
    esum = 0
    osum = 0
    eprev = 0
    oprev = -1
    flag = True
    x = 0
    for j in range(n):
        if br[j] == 1:
            x -= 1 # remove 1 cases
            if flag:
                flag = False
                eprev = j
                esum += eprev-oprev
            else:
                flag = True
                oprev = j
                osum += oprev-eprev
        if flag: x += osum
        else: x += esum
    ans += x*v
print(ans)

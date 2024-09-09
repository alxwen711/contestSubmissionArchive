import sys
from itertools import permutations
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

# n <= 10, brute force?

def pal(s,i,x):
    for j in range(x//2):
        if s[i+j] != s[i-j+x-1]: return False
    return True

def ha(x):
    i = 0
    for j in x:
        i *= 26
        i += (ord(j)-97)
    return i

n,k = readints()
s = readin()
#ar = list()
#for i in s:
#    ar.append(i)
br = permutations(s)
#br.sort()
ans = 0
#print(len(br))
#prev = (1,2,3,4,5)
d = {}
for b in br:
    v = hash(b)
    if d.get(v) == None:
        d[v] = 1
        flag = True
        for c in range(n-k+1):
            if pal(b,c,k):
                flag = False
                break
        if flag: ans += 1
print(ans)

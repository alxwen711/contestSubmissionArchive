import sys

def rm(s):
    if len(s) == 1: return s, False
    h = [0]*26
    for i in range(len(s)):
        h[ord(s[i])-97] += 1
    f = [0]*26
    
    for j in range(26):
        f[j] = h[j] // 2
    #print(f)
    for k in range(len(s)):
        x = ord(s[k])-97
        if f[x] == 0:
            if k == 0: return s[k:],False
            else: return s[k:],True
        f[x] -= 1
        

for i in range(int(sys.stdin.readline())):
    s = str(sys.stdin.readline())
    s = s[:-1]
    cont = True
    while cont:
        s,cont = rm(s)
    print(s)
        

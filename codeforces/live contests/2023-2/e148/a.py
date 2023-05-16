import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    s = input()
    h = [0]*26
    for j in range(len(s)):
        h[ord(s[j])-97] += 1
    d = len(s)
    if d % 2 == 1: d -= 1
    flag = "YES"
    for k in range(26):
        if h[k] >= d:
            flag = "NO"
            break
    print(flag)
            

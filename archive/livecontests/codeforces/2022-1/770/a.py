import sys

for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split(' '))
    s = str(sys.stdin.readline().strip())
    if k == 0: print(1)
    else:
        pal = True
        for i in range(len(s)//2):
            if s[i] != s[n-1-i]:
                pal = False
                break
        if pal: print(1)
        else: print(2)
        

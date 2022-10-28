import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

a = input()
ar = list()
minLen = 0
for i in range(len(a)):
    if a[i] == "a": minLen = len(ar)
    else:
        ar.append(a[i])
#print(minLen)
if (len(ar)//2 < minLen) or (len(ar) % 2 == 1): print(":(")
else:
    flag = True
    xxxxx = len(ar)//2
    for j in range(xxxxx):
        if ar[j] != ar[j+xxxxx]:
            flag = False
            break
    if not flag: print(":(")
    else:
        ans = list()
        count = xxxxx + 1
        for k in range(len(a)):
            s = a[k]
            if s != "a": count -= 1
            if count == 0: break
            ans.append(s)
        print(*ans,sep="")
    

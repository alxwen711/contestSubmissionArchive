import sys
for i in range(int(sys.stdin.readline())):
    r,c = map(int,sys.stdin.readline().split())
    if r % 2 == 1: rL = r//2
    else: rL = int(r/2 - 1)
    if c % 2 == 1: cL = c//2
    else: cL = int(c/2 - 1)
    ar = [0]*(rL+cL+1) #0 to long
    maxDis = rL+cL
    for j in range(r):
        for k in range(c):
            ar[min((abs(j-0)+abs(k-0)),(abs(j-r+1)+abs(k-0)), (abs(j-0)+abs(k-c+1)), (abs(j-r+1)+abs(k-c+1)))] += 1
    for h in range(maxDis+1):
        print((str(r+c-2-maxDis+h)+" ")*ar[maxDis-h],end="")
    print()

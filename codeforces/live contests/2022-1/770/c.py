import sys

for i in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split(' '))
    if b == 1:
        print("YES")
        for j in range(a):
            print(j+1)
    elif a % 2 == 0:
        print("YES")
        box = b*2
        for k in range(a//2):
            for l in range(b):
                print(box*k+l*2+1, end=" ")
            print()
            for m in range(b):
                print(box*k+m*2+2, end=" ")
            print()
    else: print("NO")
    


import sys

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    if n == 1: print(1)
    elif n == 2: print("1 2")
    else:
        st = -1
        for j in range(n):
            if l[j] != j+1:
                st = j
                break
        if st == -1:
            for k in range(n):
                print(l[k],end=" ")
            print()
        else:
            end = 0
            for m in range(n):
                if l[m] == st+1:
                    end = m
                    break
            for a in range(st):
                print(l[a],end=" ")
            for b in range(end-st+1):
                print(l[end-b],end=" ")
            for c in range(n-end-1):
                print(l[end+c+1],end=" ")
            print()
            

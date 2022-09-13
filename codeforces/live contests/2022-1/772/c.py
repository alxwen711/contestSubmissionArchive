import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    if ar[n-2] > ar[n-1]: print(-1)
    elif n == 2: print(0)
    else:
        high = ar[n-1]
        key = -1
        solve = True
        for j in range(n-1):
            test = ar[n-j-2]
            if test-high <= test:
                key = n-j-1 #y val, z val is always n
                break
            elif ar[n-j-2] > ar[n-j-1]:
                solve = False
                break
        if solve == False: print(-1)
        elif key == -1: print(0)
        else:
            z = n
            y = key
            a = y-1
            print(a)
            for k in range(a):
                print(k+1,y,z)
        

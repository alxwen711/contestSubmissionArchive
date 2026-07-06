for i in range(int(input())):
    n,k = map(int,input().split())
    if k > (n+1)//2: print("-1")
    else:
        rP = 0
        for j in range(n):
            if j % 2 == 0 and rP != k:
                print("."*j+"R"+"."*(n-j-1))
                rP += 1
            else: print("."*n)

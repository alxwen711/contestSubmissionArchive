import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    n = str(n)
    if len(n) == 2: print(n[1])
    else:
        ans = 10
        for j in range(len(n)):
            if int(n[j]) < ans: ans = int(n[j])
        print(ans)
    

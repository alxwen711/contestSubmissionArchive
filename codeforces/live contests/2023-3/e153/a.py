import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    s = input()
    if len(s) == 2:
        if s == "()":
            print("NO")
        elif s == ")(":
            print("YES")
            print("(())")
        elif s == "((":
            print("YES")
            print("()()")
        else:
            print("YES")
            print("()()")
    else:
        print("YES")
        l = True
        flag = True
        n = len(s)
        for j in range(n-1):
            if s[j] == ")" and s[j+1] == "(":
                flag = False
                break
        if flag: print("()"*n)
        else: print("("*n+")"*n)

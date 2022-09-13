import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(input().split("W"))
    ans = "YES"
    for j in range(len(ar)):
        if len(ar[j]) == 1:
            ans = "NO"
            break
        elif len(ar[j]) != 0 and (ar[j].count("R")==0 or ar[j].count("B")==0):
            ans = "NO"
            break
    print(ans)

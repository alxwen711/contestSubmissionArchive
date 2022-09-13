import sys
for i in range(int(sys.stdin.readline())):
    s = str(sys.stdin.readline())
    x = len(s)-1
    #print(x)
    if x%2==1: print("NO")
    else:
        r = "YES"
        for i in range(x//2):
            if s[i] != s[i+x//2]:
                r = "NO"
                break
        print(r)

#10:55, finish in 35 minutes

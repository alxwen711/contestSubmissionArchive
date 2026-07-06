import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = str(sys.stdin.readline())
    if n >= 3: print ("NO")
    elif n == 1: print("YES")
    elif s.count("0") == 1 and s.count("1") == 1: print("YES")
    else: print("NO")

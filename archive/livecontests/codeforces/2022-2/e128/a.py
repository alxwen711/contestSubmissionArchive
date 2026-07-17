import sys
for i in range(int(sys.stdin.readline())):
    a,b,c,d = map(int,sys.stdin.readline().split())
    ans = a+c
    if a <= c <= b and c < ans: ans = c
    if c <= a <= d and a < ans: ans = a
    print(ans)

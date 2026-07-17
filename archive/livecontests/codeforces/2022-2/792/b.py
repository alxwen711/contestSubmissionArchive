import sys
for i in range(int(sys.stdin.readline())):
    a,b,c = map(int,sys.stdin.readline().split())
    print(a+b+c,b+c,c)

import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    if a == 0: print(1)
    else: print(a+(b*2)+1)

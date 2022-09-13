import sys
for i in range(int(sys.stdin.readline())):
    ar = list(map(int,sys.stdin.readline().split()))
    br = list(map(int,sys.stdin.readline().split()))
    c = sum(ar)+sum(br)
    if c == 0: print(0)
    elif c == 4: print(2)
    else: print(1)

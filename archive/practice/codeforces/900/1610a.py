import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())
    if a == 1 and b == 1: print("0")
    elif a == 1 or b == 1: print("1")
    else: print("2")

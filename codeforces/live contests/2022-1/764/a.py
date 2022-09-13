import sys

for i in range(int(sys.stdin.readline())):
    b = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    print(max(a)-min(a))

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

a = input()
ans = "Yes"
for i in range(1,16,2):
    if a[i] == "1": ans = "No"
print(ans)

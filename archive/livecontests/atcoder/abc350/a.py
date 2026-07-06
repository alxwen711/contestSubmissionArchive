import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
if s[:3] != "ABC": print("No")
elif int(s[3:]) > 349 or int(s[3:]) == 316 or int(s[3:]) == 0: print("No")
else: print("Yes")

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

s = input()
n = len(s)
if s[0] == "<" and s[-1] == ">" and s.count("=") == n-2: print("Yes")
else: print("No")

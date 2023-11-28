import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def f(n):
    a = n//100
    b = n//10 % 10
    c = n % 10
    return a*b == c

n = readint()
while not f(n):
    n += 1
print(n)

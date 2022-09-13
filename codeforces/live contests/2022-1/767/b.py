import sys

def solve(a,b,c):
    if a == b:
        if a != 1: return True
        else: return False
    r = b - a + 1
    even = r // 2
    if a % 2 == 1 and b % 2 == 1: even += 1
    if c >= even: return True
    else: return False

for i in range(int(sys.stdin.readline())):
    a,b,c = map(int, sys.stdin.readline().split())
    if solve(a,b,c): print("YES")
    else: print("NO")

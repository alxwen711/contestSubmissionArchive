import sys

def solve(a,b,c):
    if (2*b-c) / a % 1 == 0 and (2*b-c) >= a: return True
    if ((a+c)/2) / b % 1 == 0 and ((a+c)/2) >= b: return True
    if (2*b-a) / c % 1 == 0 and (2*b-a) >= c: return True
    return False

for i in range(int(sys.stdin.readline())):
    a,b,c = map(int, sys.stdin.readline().split())
    if solve(a,b,c): print("YES")
    else: print("NO")
    
    

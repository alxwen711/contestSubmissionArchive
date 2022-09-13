import sys

def solve(a,b,c):
    if (a==b and c%2==0) or (b==c and a%2==0) or( c==a and b%2==0): return "YES"
    if a+b==c or b+c==a or c+a==b: return "YES"
    return "NO"


for i in range(int(sys.stdin.readline())):
    a,b,c = map(int, sys.stdin.readline().split())
    print(solve(a,b,c))

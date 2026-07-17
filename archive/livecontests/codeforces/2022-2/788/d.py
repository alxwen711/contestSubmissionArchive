import sys
from math import sqrt
from math import ceil

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    x = (n+1)//2
    ans = ceil(sqrt(3*x))
    print(ans)
    

import sys
import math
for i in range(int(sys.stdin.readline())):
    x = float(sys.stdin.readline())+0.001
    print(math.floor(x**(1/2))+math.floor(x**(1/3))-math.floor(x**(1/6)))

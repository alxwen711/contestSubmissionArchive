import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
cost of 0->1: 1 step
1->2: x*1+(1-x)*3+(1-x)^2*5... (x is chance of success, n-1/n)
moving 1 step: x*1+(1-x)*(x+y)+(1-x)^2*(x+2y)+(1-x)^3*(x+3y)...
y is the expected steps for the previous value (store in modulo)
how to calculate the infinite sums??

sum((x^i)([n-x]^i-1)(expected steps)/n^i)

each value can be converted to modulo, then added for the format
"""

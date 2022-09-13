#10:20

import sys

for i in range(int(sys.stdin.readline())):
    a,b,c,d,e,f = map(int, sys.stdin.readline().split())
    if c <= e: g = e-c
    else: g = 2*a-c-e
    if d <= f: h = f-d
    else: h = 2*b-d-f
    print(min(g,h))

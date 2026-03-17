import sys
from math import lcm

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    a,b,c,m = readints()
    ao = m//a
    bo = m//b
    co = m//c
    ab = m//lcm(a,b)
    ac = m//lcm(a,c)
    bc = m//lcm(b,c)
    abc = m//lcm(a,b,c)
    ansa,ansb,ansc = abc*2,abc*2,abc*2
    ansa += 3*(ab+ac-(2*abc))
    ansb += 3*(ab+bc-(2*abc))
    ansc += 3*(bc+ac-(2*abc))
    ansa += 6*(ao-ab-ac+abc)
    ansb += 6*(bo-ab-bc+abc)
    ansc += 6*(co-bc-ac+abc)
    print(ansa,ansb,ansc)
    

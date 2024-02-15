import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
1 -> 0/1
2 -> 1/(1+r2)
3 -> (2+r2)/(4+r2)
4 -> (6+2r2)/(6+4r2) 2**3
5 -> (12+6r2)/(16+6r2) 2**4
6 -> (28+12r2)/(28+16r2) 2**5
7 -> (56+28r2)/(64+28r2) 2**6
8 -> (120+56r2)/(120+64r2) 2**7
"""

def solve(n):
    if n == 1: return 0
    elif n == 2: return 1
    elif n == 3: return 714285638
    m = 999999893
    #use above method to calculate (somehow)
    if n % 2 == 0:
        d2 = pow(2,n-2,m)
        n2 = (d2 - pow(2,(n//2)-1,m)) % m
        n1 = (n2+d2) % m
        d1 = n1
    else:
        d1 = pow(2,n-1,m)
        n1 = (d1 - pow(2,(n-1)//2,m)) % m
        n2 = (n1*pow(2,m-2,m)) % m
        d2 = n2
    #convert (n1+n2r2)/(d1+d2r2), *(d1-d2r2)
    #print(n1,n2,d1,d2)
    fd = (d1*d1)-(d2*d2*2)
    fn = (n2*d1)-(n1*d2)
    return (fn*pow(fd,m-2,m)) % m

for _ in range(readint()):
    print(solve(readint()))    

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
single val input, look for oeis like patterns
requires knowing cost of moving to next step and
the expected distribution of costs in next step

also determine chances of who is starting first second
spots filled, n -> first player, second player
0 _ -> 0 0
1 2 -> 2/3 1/3 (total is 1)
1 3 -> 3/8 1/8 3/4 1/4 (expected payment is 1/2)
2 3 -> 6/5 4/5 3/5 2/5 (expected payment is 2)

p1: 1*0+0*0 + 0*3/8+1*1/8 + 3/4*6/5+1/4*4/5
n = 3 -> 49/40 51/40
"""
def fast_exp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r
def py_egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = py_egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def py_modinv(a, m):
    g, x, y = py_egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
m = 998244353
n = readint()
ansa,ansb = 0,0
pa,pb = 1,0

#invn = pow(n,m-2,m)
#invn2 = pow(n*n,m-2,m)
invn = fast_exp(n,m-2,m)
invn2 = fast_exp(n*n,m-2,m)

for i in range(n):
    # i/n initial chances, i**2/n**2 ratio
    num = i*invn
    dom = (n*n-i*i)*invn2
    first = (num*fast_exp(dom,m-2,m)) % m
    second = (first*num) % m
    ansa += first*pa+second*pb
    ansb += first*pb+second*pa
    ansa = ansa % m
    ansb = ansb % m
    #print("sumvals",first,second)
    # determine new pa/pb
    if i == 0: pa,pb = 0,1 # avoid div 0
    else:
        s = (first+second) % m
        invs = py_modinv(s,m)
        first = (first*invs) % m
        second = (second*invs) % m
        #print("ratios",first,second)
        npa = (pb*first+pa*second) % m
        npb = (pa*first+pb*second) % m
        pa = npa
        pb = npb
    #print("pvals",pa,pb)
print(ansa,ansb)
    

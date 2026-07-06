import sys
from copy import deepcopy
 
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
 
"""
is O(n**1.5) used here?
"""
 
#root = 10648 #22**3
#invroot = 104531307729 #inverse root
 
# print(pow(root,2**36,m)) #should be 1, 2**36th root of m
# print(pow(root,2**36-1,m)) #inv root calculation
 
def fft(ar, n, w, p):
    if n == 1: return ar
    elif n == 2: return [(ar[0]+ar[1]) % p, (ar[0]-ar[1]) % p]
 
    br = list()
    cr = list()
    for i in range(n//2):
        br.append(ar[2*i])
        cr.append(ar[2*i+1])
 
    ww = (w*w) % p
    br = fft(br,n//2,ww,p)
    cr = fft(cr,n//2,ww,p)
    ww = 1
    dr = [0]*n
    for j in range(n//2):
        t = (ww*cr[j]) % p
        dr[j] = (br[j]+t) % p
        dr[j+(n//2)] = (br[j]-t) % p
        ww = (ww*w) % p
    return dr
 
def multiply(ar,br):
    m = 998244353 # divisible by 2**22 at minimum
 
    #fa = deepcopy(ar)
    #fb = deepcopy(br)
    n = 1
    while n < (len(ar) + len(br) - 1):
        n *= 2
    
    primroot = 3
    root = pow(primroot,(m-1)//n,m)
    invroot = pow(root,m-2,m)
    #print(root,invroot,(root*invroot) % m)
    while len(ar) != n:
        ar.append(0)
    while len(br) != n:
        br.append(0)
    #print(fa)
    #print(fb)
    # if this screws up then try swapping root/invroot
    ar = fft(ar, n, root, m)
    br = fft(br, n, root, m)
    #print(fa)
    #print(fb)
    for i in range(n):
        ar[i] = (ar[i]*br[i]) % m
    #print(fa)
    ar = fft(ar, n, invroot, m)
    ninv = pow(n,m-2,m)
    for jj in range(n):
        ar[jj] = (ar[jj]*ninv) % m
    return ar # would return result here but it's in ntt so no rounding??
 


""" #confirmation code
a = [1,3,0,-1]
b = [1,0,-2,-3,2]
print(multiply(a,b))
 
 
print(fft([1,2,3,4,3,2,1,0],8,64,97))
print(fft([16, 48, 0, 16, 0, 36, 0, 86],8,47,97))
"""
n = readint()
ar = readar()
br = [1,2,0]
cr = multiply(ar,br)

print(cr)

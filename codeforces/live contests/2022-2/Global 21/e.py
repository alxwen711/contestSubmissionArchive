#save this code for n choose r mod p toolbox
import sys
"""
def h(n,c,r):
     
    #store row of pascal triangle
    b = [0]*min(n+1,c+1)
    b[0] = 1
 
    for i in range(1,(n+1)):
        #overwrite new row of up to j values
        j = min(i,c)
        while j > 0:
            b[j] = (b[j] + b[j-1]) % r
            j -= 1
        #print(b)
    return b[c]
 
"""
n = int(sys.stdin.readline())+1
ar = list(map(int,sys.stdin.readline().split()))


#find sum of fib values in each box
#1's, counting numbers, then triangular
"""
n -> C(n,1)
n(n+1)/2 C(n+1,2)
C(n+2,3)
C(n+3,4)
"""

ans = 0
factorials = [0]*400003
factorials[0] = 1
infact = [0]*400003
infact[0] = 1
for a in range(1,400003):
    factorials[a] = factorials[a-1]*a % 1000000007
    infact[a] = pow(factorials[a],1000000005,1000000007)

for i in range(n):
    #if ar[i] != 0: ans = (ans + h(ar[i]+i,i+1,1000000007)) % 1000000007
    a,b = ar[i]+i,i+1
    if ar[i] != 0: ans = (ans + (factorials[a]*infact[b]*infact[a-b])) % 1000000007
print(ans)

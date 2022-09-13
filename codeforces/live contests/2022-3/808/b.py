import sys

def solve(n,l,r):
    h = [0]*n
    d = {}
    for j in range(n):
        x = n-j
        #find x factor
        m = (l//x)*x
        while True:
            if m > r:
                print("NO")
                return
            elif m >= l:
                #if d.get(m) == None:
                h[-j-1] = m
                    #d[m] = n-j
                break
            m += x
    print("YES")
    print(*h)
    return
                


for i in range(int(sys.stdin.readline())):
    n,l,r = map(int,sys.stdin.readline().split())
    """
    gcd = 1,2,3,4,5...
    """
    solve(n,l,r)

import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
you CAN find all segment costs in time limit (O(n^2) allowed)
then for each case from length 1 to k//2 (excess will double count)
find the min with sparse table
full runtime is O(n^2 log n), i think this is fast enough? hopefully?

you can use more than two segments

new problem: current build is now using only contiguous segments, how to use any case

maybe a way to find best setup for 1,2,3...k, basic dp feels like O(n^3)?

solution is a dp optimization to get to O(n^2)
"""

def create_sparse(ar: list) -> list:
    s = list()
    s.append(ar)
    prevrow = 0
    dist = 2 #length of subarray representation
    while dist <= len(ar):
        x = len(ar)-dist+1
        tmp = [0]*x
        for i in range(x):
            #find [i:i+dist]
            tmp[i] = (max(s[prevrow][i],s[prevrow][i+dist//2]))
        s.append(tmp)
        prevrow += 1
        dist = dist << 1
    return s

def query(l: int, h: int, ar: list):
    if l > h: return -999999999999999
    length = h-l+1
    #find largest x where 2**x <= length
    two = 1
    ex = 0
    while True:
        ex += 1
        two = two << 1
        if two > length:
            two = two >> 1
            ex -= 1
            break
    if length == two: return ar[ex][l]
    else: return max(ar[ex][l],ar[ex][h-two+1])


def solve(n,k,ar,br):
    cr = list()
    cr.append([])
    sr = list()
    sr.append([])
    for i in range(n):
        tmp = list()
        for j in range(n-i):
            tmp.append(abs(ar[j]-br[i+j])+abs(br[j]-ar[i+j]))
        cr.append(tmp)
    sr.append(create_sparse(cr[1]))
    dr = list()
    dr.append([])
    dr.append(cr[1])
    for ii in range(2,n+1):
        tmp = list()
        for jj in range(n-ii+1):
            tmp.append(max(dr[ii-1][jj]+cr[1][jj+ii-1],dr[ii-1][jj+1],cr[1][jj],cr[ii][jj]))
        dr.append(tmp)
        #sr.append(create_sparse(tmp))
    ans = -9999999999999999
    #for a in range(1,(k//2)+1):
    #    comp = k-a
    #    for b in range(len(dr[a])):
            # get complement around dr[a][b]
    #        x = dr[a][b]+max(query(0,b-comp,sr[comp]),query(a+b,n-comp,sr[comp]))
    #        ans = max(x,ans)
    return max(ans,max(dr[k]))
    
for i in range(readint()):
    n,k = readints()
    ar = readar()
    br = readar()
    print(solve(n,k,ar,br))

import sys
def solve(ar,l,a): #ret num of 0 to 1 changes
    h = 0
    for f in range(a):
        if ar[f+l][f] == "0": h += 1
    return h

for i in range(int(sys.stdin.readline())):
    literallyablankline = input()
    a = int(sys.stdin.readline())
    ar = list()
    one = 0
    for j in range(a):
        x = str(input())
        one += x.count("1")
        ar.append(x)
    for k in range(a):
        ar.append(ar[k])
    ans = 99999999999999999999999999999
    for l in range(a):
        tmp = solve(ar,l,a)
        ones = one+tmp
        tmp += ones-a
        if tmp < ans: ans = tmp
    print(ans)
        

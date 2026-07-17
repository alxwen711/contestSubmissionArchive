import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
odd by even will always be 1 off

at this point the better idea would be to add in all edges
then construct the path in coordinates, then implement this
path by removing specific walls
"""

def construct_base(n,m): # maze with no walls implemented
    ans = list()
    tmp = ["+"]*(2*m+1)
    tmp[-2] = "S"
    ans.append(tmp)
    for i in range(2*n-1):
        tmp = ["+"]*(2*m+1)
        if i % 2 == 0:
            for j in range(1,2*m):
                if j % 2 == 0: tmp[j] = "."
                else: tmp[j] = "o"
        else:
            for k in range(1,2*m,2):
                tmp[k] = "."
        ans.append(tmp)
    tmp = ["+"]*(2*m+1)
    tmp[-2] = "G"
    ans.append(tmp)
    return ans

def print_ans(ar):
    print("Yes")
    for i in ar:
        print(*i,sep="")

n,m,k = readints()
if k < n or k % 2 != n % 2: print("No")
else: # placement exists
    if n % 2 == 0: # even case
        req = (k-n)//2
        ar = list()
        for i in range(n//2):
            ar.append(min(m-1,req))
            req -= min(n-1,req)
        ans = construct_base(n,m)
        #print_ans(ans)
        # place all horizontal walls
        for a in range(2,2*n,2):
            for b in range(1,2*m,2):
                ans[a][b] = "-"
        #print_ans(ans)
        # reconstruct according to ar
        for c in range(n//2):
            if 4*c+4 != 2*n: ans[4*c+4][2*m-1] = "."
            if ar[c] != m-1:
                ans[4*c+3][2*m-2-(ar[c]*2)] = "|"
                ans[4*c+1][2*m-2-(ar[c]*2)] = "|"
            ans[4*c+2][2*m-1-(ar[c]*2)] = "."
            
        print_ans(ans)
        
    else: # odd m case
        ans = construct_base(n,m)
        
        # place all vertical walls
        for a in range(1,2*n,2):
            for b in range(2,2*m,2):
                ans[a][b] = "|"

        req = (k-n)//2
        sideinc = min(req,m-1)
        for c in range(sideinc):
            ans[2][2*m-1-(2*c)] = "-"
            ans[-3][2*m-1-(2*c)] = "-"
            ans[1][2*m-2-(2*c)] = "."
            ans[-2][2*m-2-(2*c)] = "."
        req -= sideinc
        if req != 0: # vertical looping
            # note: there is still yet another scenario where
            # secondary horizontal looping is used, not implemented here
            ar = list()
            for i in range((m-1)//2):
                ar.append(min(n-2,req))
                req -= min(n-2,req)
            for d in range((m-1)//2):
                if ar[d] != 0:
                    ans[-2][4*d] = "|"
                    ans[-3][4*d-1] = "."
                    ans[-3][4*d+1] = "."
                    ans[-3-(2*ar[d])][4*d-1] = "-"
                    ans[-3-(2*ar[d])][4*d+1] = "-"
                    ans[-2-(2*ar[d])][4*d] = "."
        print_ans(ans)
            

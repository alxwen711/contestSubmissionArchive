import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def f(n,s): #find min, likely correct
    index = 0
    hit = n//4
    ans = 0
    u = [0]*n
    while hit != 0 and index < n-1:
        if s[index] == "1" and s[index+1] == "1":
            hit -= 1
            u[index] = 1
            u[index+1] = 1
            index += 2
            ans += 1
        else: index += 1
    index = 0
    #find 01/10
    r = hit
    while r != 0 and index < n-1:
        if u[index] == 0 and u[index+1] == 0 and ((s[index] == "1" and s[index+1] == "0") or (s[index] == "0" and s[index+1] == "1")):
            u[index] = 1
            u[index+1] = 1
            ans += 1
            r -= 1
            index += 2
        else: index += 1
    index = 0
    #find 00
    while r != 0 and index < n-1:
        if u[index] == 0 and u[index+1] == 0 and s[index] == "0" and s[index+1] == "0":
            u[index] = 1
            u[index+1] = 1
            r -= 1
            index += 2
        else: index += 1
    
    for i in range(n):
        if u[i] == 0 and s[i] == "1": ans += 1
    return ans
    
    return ans
    
def g(n,s): #find max, somewhere there is some reasoning error here
    u = [0]*n
    r = n//4
    index = 0
    ans = 0
    # place anywhere except 11?
    while r != 0 and index < n-1:
        if s[index] == "0" or s[index+1] == "0":
            u[index] = 1
            u[index+1] = 1
            if s[index] == "1" or s[index+1] == "1": ans += 1
            r -= 1
            index += 2
        else: index += 1
    index = 0
    #find 11
    while r != 0 and index < n-1:
        if u[index] == 0 and u[index+1] == 0 and s[index] == "1" and s[index+1] == "1":
            u[index] = 1
            u[index+1] = 1
            ans += 1
            r -= 1
            index += 2
        else: index += 1
    
    """
    while r != 0 and index < n-1:
        if (s[index] == "1" and s[index+1] == "0") or (s[index] == "0" and s[index+1] == "1"):
            u[index] = 1
            u[index+1] = 1
            ans += 1
            r -= 1
            index += 2
        else: index += 1
    index = 0
    #find 00
    while r != 0 and index < n-1:
        if u[index] == 0 and u[index+1] == 0 and s[index] == "0" and s[index+1] == "0":
            u[index] = 1
            u[index+1] = 1
            r -= 1
            index += 2
        else: index += 1
    """
    ans -= r
    for i in range(n):
        if u[i] == 0 and s[i] == "1": ans += 1
    return ans
    

n,m = readints()
ansa,ansb = 0,0
for i in range(n):
    s = input()
    ansa += f(m,s)
    ansb += g(m,s)
print(ansa,ansb)
    

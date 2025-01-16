import sys

#input functions
readint = lambda: int(f.readline().strip("\n"))
readints = lambda: map(int,f.readline().split())
readar = lambda: list(map(int,f.readline().split()))
readin = lambda: f.readline[:-1] # may need to check on this
readins = lambda: map(str,f.readline().split())
flush = lambda: sys.stdout.flush()

"""
the logic for longest string likely means
replacing each digit with either 1 or 2
so that they can start a new character

definitely can NEVER be a 0
the optimal number of strings can be obtained from all 1's

in some cases 2's are possible

the last digit is extremely icky (could be 1-9 in specific case)

a split of all 1's can be computed via dp

?? can have dependencies that make it so that individual ranges cannot be used
(if first ? is a 2, then a 1-9 range on second digit fail on 27)

fill in the string backwards, k is always at most the number of strings

? mark cases:

0?,1?,x? -> 1-9
2? -> 1-6
?? -> handle seperately

?0,?1,?2,?3,?4,?5,?6 -> 1-2
?7,?8,?9 -> 1

use edge cases for 1 digit
"""


def solve(s,k): # actual solution goes here
    n = len(s)
    if n == 1:
        if s != "?": return s,1
        else: return k,1
    ar = list()
    for i in range(n):
        if s[i] == "?": ar.append("?")
        else: ar.append(int(s[i]))

    # string construction
    
    k -= 1
    if ar[-1] == "?":
        if ar[-2] == "?": #15 cases total
            bruh = [26,25,24,23,22,21,19,18,17,16,15,14,13,12,11] # 15 cases
            r = k % 15
            ar[-2] = bruh[r]//10
            ar[-1] = bruh[r]%10
            k //= 15
        elif ar[-2] != 2:
            r = k % 9
            ar[-1] = 9-r
            k //= 9
        else:
            r = k % 6
            ar[-1] = 6-r
            k //= 6
    for j in range(n-1,-1,-1):
        if ar[j] == "?":
            if ar[j+1] <= 6:
                r = k % 2
                ar[j] = 2-r
                k //= 2
            else:
                ar[j] = 1
    
    # based on ar, count how many are possible

    m = 998244353
    dp = [0]*27
    dp[ar[0]] += 1
    #print(dp)
    for p in range(1,n):
        ndp = [0]*27
        x = ar[p]
        for q in range(1,27):
            if q >= 3 or (q == 2 and x >= 7): # must split
                ndp[x] = (ndp[x]+dp[q]) % m
            else: # both is possible
                ndp[x] = (ndp[x]+dp[q]) % m
                ndp[q*10+x] = (ndp[q*10+x]+dp[q]) % m
        ndp[0] = 0 # 0 is invalid
        dp = ndp
        #print(dp,ar[p])
    ans = sum(dp) % m
    for snth in range(n):
        ar[snth] = str(ar[snth])
    return "".join(ar),ans
    
filename = "1d3"
f = open(filename+".txt","r") # ALWAYS MAKE F THE OPEN FILE
casecount = readint()
print(casecount)
ans = list()
for i in range(casecount):
    # get input here
    s,k = readins()
    k = int(k)
    ans.append(solve(s,k))
    print(i+1,"done")
f.close()

f = open(filename+"sol.txt","w")
for k in range(len(ans)):
    f.write("Case #"+str(k+1)+": "+str(ans[k][0])+" "+str(ans[k][1]))
    f.write("\n")
f.close()


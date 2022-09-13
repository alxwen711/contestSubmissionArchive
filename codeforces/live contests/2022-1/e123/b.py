import sys

"""
1423
4123
1432
4132
"""

def checkList(ans,n):
    for x in range(n-2):
        if ans[x] + ans[x+1] == ans[x+2]:
            #print(ans[x],ans[x+1],ans[x+2])
            return False
    return True

def noDup(ans,sol,n,solves):
    #print(ans,sol)
    for y in range(solves):
        dup = True
        for z in range(n):
            if ans[z] != sol[y][z]:
                dup = False
                break
        if dup: return False
    return True

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = 0
    if n == 3:
        print("2 3 1")
        print("1 3 2")
        print("3 1 2")
    elif n == 4:
        print("1 4 2 3")
        print("1 4 3 2")
        print("4 3 2 1")
        print("4 1 3 2")
    elif n == 5:
        print("5 1 4 2 3")
        print("5 1 4 3 2")
        print("5 4 3 2 1")
        print("5 4 1 3 2")
        print("5 4 3 1 2")
    else:
        pairs = n//2
        solves = 0
        attempts = 0
        #ans = list()
        pastSol = list()
        ss = n//2*2
        while solves < n:
            ans = list()
            a = attempts
            for k in range(pairs):
                if a % 2 == 1: #reverse order
                    ans.append(n-k)
                    ans.append(k+1)
                else:
                    ans.append(k+1)
                    ans.append(n-k)
                a = a//2
            if n % 2 == 1: ans.insert(ss,n//2+1)
            if checkList(ans,n) and noDup(ans,pastSol,n,solves):
                for l in range(n):
                    if l != n-1: print(ans[l],end=" ")
                    else: print(ans[l])
                pastSol.append(ans)
                solves += 1
            attempts += 1
            if attempts == 2**(n//2):
                attempts = 0
                ss += -1
                if ss == -1:
                    print(n," does not work")
"""
48
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50


"""

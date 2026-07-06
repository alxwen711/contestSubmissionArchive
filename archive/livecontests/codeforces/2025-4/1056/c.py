import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
7
1
1

L
R

4
4 4 3 2

LRRR

3
1 3 2

impossible

2
2 1

LR

3
2 2 2

RLR
LRL

3
3 2 3

impossible

3
3 2 2

impossible

cape count is determined in position by 1 + L's on left + R's on right
sequence does NOT have to be determined
answer can only be 0, 1, or 2

swapping the character means the number remains the same
+1 is from repeated L's
-1 is from repeated R's
there is at least one sequence change unless it's full alt
if full alt AND n is odd, then ans is 2
if not all positions can be filled, check if ends are different
otherwise this is impossible
+1 and -1 back to back is impossible
looking easier to try to build the answer then assert that they are the same
"""


def update(ar,ans,count): # use some sort of graph dfs to complete
    q = []
    for i in range(len(ans)-1):
        a = ans[i]
        b = ans[i+1]
        if (a == " " and b != " ") or (a != " " and b == " "):
            q.append(i)
    while len(q) != 0:
        i = q.pop()
        #a,b = ans[x],ans[x+1]
        diff = ar[i+1]-ar[i]
        if diff == 1: # both are L
            if ans[i] == " ":
                ans[i] = "L"
                count += 1
                if i != 0: q.append(i-1)
            elif ans[i] != "L":
                return count
            if ans[i+1] == " ":
                ans[i+1] = "L"
                count += 1
                if i != n-2: q.append(i+1)
            elif ans[i+1] != "L":
                return count
        elif diff == -1: # both are R
            if ans[i] == " ":
                ans[i] = "R"
                count += 1
                if i != 0: q.append(i-1)
            elif ans[i] != "R":
                return count
            if ans[i+1] == " ":
                ans[i+1] = "R"
                count += 1
                if i != n-2: q.append(i+1)
            elif ans[i+1] != "R":
                return count
        else: # both are different
            if ans[i] == ans[i+1] and ans[i] != " ":
                return count
            if ans[i] != " " or ans[i+1] != " ":
                if ans[i] == " ":
                    count += 1
                    if ans[i+1] == "L": ans[i] = "R"
                    else: ans[i] = "L"
                    if i != 0: q.append(i-1)
                if ans[i+1] == " ":
                    count += 1
                    if ans[i] == "L": ans[i+1] = "R"
                    else: ans[i+1] = "L"
                    if i != n-2: q.append(i+1)
    return count
    

    
def accurate(ar,ans): # check if this ar actually matches the answer found
    lc,rc = 0,0
    for i in ans:
        if i == "L": lc += 1
        else: rc += 1
    la,ra = 0,0
    for i in range(len(ans)):
        if ans[i] == "L":
            lc -= 1
            if 1+rc+la != ar[i]: return False
            la += 1
        else:
            rc -= 1
            if 1+rc+la != ar[i]: return False
            ra += 1
    return True

m = 676767677

for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = [" "]*n
    flag = True
    count = 0
    for i in range(n-1):
        c = ar[i+1]-ar[i]
        if c == 1: # both must be L
            if ans[i] == " ":
                ans[i] = "L"
                count += 1
            elif ans[i] != "L":
                flag = False
                break
            if ans[i+1] == " ":
                ans[i+1] = "L"
                count += 1
            elif ans[i+1] != "L":
                flag = False
                break
        elif c == -1: # both must be R
            if ans[i] == " ":
                ans[i] = "R"
                count += 1
            elif ans[i] != "R":
                flag = False
                break
            if ans[i+1] == " ":
                ans[i+1] = "R"
                count += 1
            elif ans[i+1] != "R":
                flag = False
                break
        elif c == 0: # these must be different
            if ans[i] == ans[i+1] and ans[i] != " ":
                flag = False
                break
            if ans[i] != " " or ans[i+1] != " ":
                if ans[i] == " ":
                    count += 1
                    if ans[i+1] == "L": ans[i] = "R"
                    else: ans[i] = "L"
                if ans[i+1] == " ":
                    count += 1
                    if ans[i] == "L": ans[i+1] = "R"
                    else: ans[i+1] = "L"
        else: # impossible case
            flag = False
            break
    if flag:
        if count != n:
            count = update(ar,ans,count)
        #print(ans)
        if count == 0: # full alt edge case
            if n % 2 == 1:
                print(2 if ar[0] == (n+1)//2 else 0)
            else:
                print(1 if ar[0] == n//2 or ar[0] == n//2+1 else 0)
        elif count == n:
            print(1 if accurate(ar,ans) else 0)
        else: print(0) # impossible to determine?
    else: print(0)
    

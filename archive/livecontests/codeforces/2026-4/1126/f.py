import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
0 1 or 2

2 -> set ends to 10**9, done
0 -> check if the coverage exists (maximum in range, hashmap, repeat on the segments)
1 -> how

find all problem pillars
1 pillar -> drop to minimum, solved
multiple pillars -> if either end is a maximum of the entire continuous segment
including previously passing parts, it can work. else no?
"""

def create_seg(n,ar):
    s = list()
    tmp = list()
    for i in ar:
        tmp.append(i)
    s.append(tmp)
    while len(s[-1]) > 1:
        tmp = list()
        for i in range(len(s[-1])//2):
            tmp.append(max(s[-1][2*i],s[-1][2*i+1]))
        s.append(tmp)
    return s

def query(ar,li,ri):
    ans = -4786384576
    l,r = li,ri
    for i in range(len(ar)):
        if l > r: return ans
        if l % 2 == 1:
            ans = max(ans,ar[i][l])
            l += 1
        if r % 2 == 0:
            ans = max(ans,ar[i][r])
            r -= 1
        l //= 2
        r //= 2
    return ans
        

for _ in range(readint()):
    n = readint()
    ar = readar()
    if n == 1:
        print(0)
        continue
    elif n == 2:
        if ar[0] != ar[1]:
            print(1)
            print(1,ar[1])
        else:
            print(0)
        continue
    seg = create_seg(n,ar)
    d = {}
    for i in range(len(ar)):
        v = ar[i]
        if d.get(v) == None: d[v] = list()
        d[v].append(i)
    q = [(0,n-1)]
    wrong = list()
    while len(q) != 0:
        x = q.pop()
        a,b = x[0],x[1]
        if a == b: wrong.append(a)
        else:
            mv = query(seg,a,b)
            # find lowest and highest case of mv in range a to b
            lx = len(d[mv])

            low = 0
            high = lx-1
            while high-low > 1:
                mid = (low+high)//2
                if d[mv][mid] >= a: high = mid
                else: low = mid
            lowv = d[mv][high]
            if d[mv][low] >= a: lowv = d[mv][low]

            low = 0
            high = lx-1
            while high-low > 1:
                mid = (low+high)//2
                if d[mv][mid] <= b: low = mid
                else: high = mid
            highv = d[mv][low]
            if d[mv][high] <= b: highv = d[mv][high]
            if lowv == highv: wrong.append(lowv)
            if a != lowv: q.append((a,lowv-1))
            if b != highv: q.append((highv+1,b))
    wrong.sort()
    #print(wrong)
    if len(wrong) == 0: print(0)
    elif len(wrong) == 1:
        print(1)
        if wrong[0] != 0:
            print(wrong[0]+1,ar[wrong[0]-1])
        else:
            print(wrong[0]+1,ar[wrong[0]+1])
    else:
        lc = query(seg,wrong[0],wrong[-1])
        if ar[wrong[0]] == lc:
            print(1)
            print(wrong[-1]+1,lc)
        elif ar[wrong[-1]] == lc:
            print(1)
            print(wrong[0]+1,lc)
        elif ar[wrong[0]] == ar[wrong[-1]]:
            flag = -1
            possible = True
            for ii in range(wrong[0]+1,wrong[-1]):
                if ar[ii] > ar[wrong[0]]:
                    if flag == -1:
                        flag = ii
                    else:
                        possible = False
                        break

            if possible:
                print(1)
                print(flag+1,ar[wrong[0]])
            else:
                print(2)
                print(1,1000000000)
                print(n,1000000000)
        else:
            mv = max(ar[wrong[0]],ar[wrong[-1]])
            ll = wrong[0]
            if ar[wrong[0]] < ar[wrong[-1]]:
                ar[wrong[0]] = mv
            else:
                ll = wrong[-1]
                ar[wrong[-1]] = ll
            possible = True
            for ii in range(wrong[0]+1,wrong[-1]):
                if ar[ii] > ar[wrong[0]]:
                    possible = False
                    break
            if possible:
                print(1)
                print(ll+1,ar[wrong[0]])
            else:
                print(2)
                print(1,1000000000)
                print(n,1000000000)
            
        
        







    

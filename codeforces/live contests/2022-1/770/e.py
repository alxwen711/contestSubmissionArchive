import sys
araara = list(list())
h = list()
tmp = list()
ost = list()
def findIndex(h, a):
    length = len(h)
    if length == 0: return False, 0
    else:
        low = 0
        high = length - 1
        while high - low > 1:
            mid = (low+high)//2
            if h[mid][0] == a: return True, mid
            elif h[mid][0] > a:
                high = mid
            else:
                low = mid
        if h[low][0] == a: return True, low
        elif h[high][0] == a: return True, high
        else: return False, low+1

for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split(' ')))
    for j in range(n):
        found, index = findIndex(h, ar[j]) #binary search
        if not found:
            h.insert(index,[ar[j],1])
        else:
            h[index][1] += 1
        ft, it = findIndex(tmp, ar[j])
        if not ft:
            tmp.insert(it, [ar[j],1])
        else:
            tmp[it][1] += 1
    araara.append(ar)
    #print(tmp)
    for s in range(len(tmp)):
        if True:
            xx = tmp[s][1]
            fffff, iiiii = findIndex(ost, xx)
            if not fffff:
                ost.append([xx])
    tmp.clear()
            

possible = True
for j in range(len(h)):
    if h[j][1] % 2 == 1:
        possible = False
        break
if possible:
    print("YES")
    for ou in range(len(ost)):
        if ou % 2 == 1:
            du, kk = findIndex(h,ost[ou][0])
            h[kk][1] += 1
    for k in range(len(araara)):
        for m in range(len(araara[k])):
            val = araara[k][m]
            dummy, where = findIndex(h,val)
            if h[where][1] % 2 == 0: sys.stdout.write("L")
            else: sys.stdout.write("R")
            h[where][1] += -1
        sys.stdout.write("\n")

else: print("NO")


def getvals(x):
    num = False
    pole = -1
    numbers = list()
    numb = ""
    for i in range(len(x)):
        if 48 <= ord(x[i]) <= 57:
            if num:
                numb += x[i]
            else:
                num = True
                pole = i
                numb += x[i]
        else:
            if num:
                num = False
                numbers.append((pole,int(numb),len(numb)))
                numb = ""
    if num:
        numbers.append((pole,int(numb),len(numb)))
    return numbers

def evaluate(br,index,ar,d):
    ans = 0
    n = len(ar)
    for i in br:
        st = i[0]
        m = len(ar[index])
        flag = False
        for j in range(st-1,st+i[2]+1):
            if j == -1 or j == m: continue
            if index != 0: #check up
                if (ord(ar[index-1][j]) >= 58 or ord(ar[index-1][j]) <= 47) and ord(ar[index-1][j]) != 46:
                    flag = True
                    d[(index-1,j)].append(i[1])
                    break
            if index != n-1: #check down
                if (ord(ar[index+1][j]) >= 58 or ord(ar[index+1][j]) <= 47) and ord(ar[index+1][j]) != 46:
                    flag = True
                    d[(index+1,j)].append(i[1])
                    break
        if st != 0:
            if (ord(ar[index][st-1]) >= 58 or ord(ar[index][st-1]) <= 47) and ord(ar[index][st-1]) != 46:
                 flag = True
                 d[(index,st-1)].append(i[1])
        ed = st+i[2]
        if ed != m:
            if (ord(ar[index][ed]) >= 58 or ord(ar[index][ed]) <= 47) and ord(ar[index][ed]) != 46:
                 flag = True
                 d[(index,ed)].append(i[1])
        if flag: ans += i[1]
    return ans

#input, default to basic integer reading file
f = open("3.txt",'r')

ar = list()

while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)


f.close()
index = 0
ans = 0
print(ar[0])

d = {}
for a in range(len(ar)):
    for b in range(len(ar[a])):
        if (ord(ar[a][b]) >= 58 or ord(ar[a][b]) <= 47) and ord(ar[a][b]) != 46:
            tmp = list()
            d[(a,b)] = tmp
            
for i in ar:
    br = getvals(i)
    ans += evaluate(br,index,ar,d)
    index += 1
print(ans)


ans2 = 0
for ii in d.keys():
    if len(d[ii]) == 2: ans2 += (d[ii][0]*d[ii][1])
print(ans2)

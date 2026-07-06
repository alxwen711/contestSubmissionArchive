ar = list()
#input, default to basic integer reading file
f = open("14.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

def hset(br):
    m = 10089886811898868001
    v = 0
    for a in br:
        for b in a:
            v *= 5
            if b == ".": v += 1
            elif b == "O": v += 2
            else: v += 3
        v = v % m
    return v
ans = 0
br = list()
for i in range(len(ar)):
    tmp = list()
    for j in range(len(ar[i])):
        tmp.append(ar[i][j])

    br.append(tmp)
flag = True
d = {}
remain = 0
for cycle in range(1000000001):
    v = hset(br)
    if d.get(v) != None: #calculate cycle
        print("found cycle at",d[v],cycle)
        dist = cycle-d[v]
        complete = cycle + ((1000000000-cycle)//dist)*dist
        remain = 1000000000-complete
        print(dist,"cycle length,", remain,"more cycles needed")
        break
    if cycle == 1000000000: break
    else: d[v] = cycle
    if cycle % 100 == 0: print(cycle,"cycles done")
    #north
    flag = True
    while flag:
        flag = False
        for a in range(len(br)-1):
            for b in range(len(br[a])):
                if br[a][b] == "." and br[a+1][b] == "O":
                    br[a][b] = "O"
                    br[a+1][b] = "."
                    flag = True
    #west
    flag = True
    while flag:
        flag = False
        for a in range(len(br)):
            for b in range(len(br[a])-1):
                if br[a][b] == "." and br[a][b+1] == "O":
                    br[a][b] = "O"
                    br[a][b+1] = "."
                    flag = True
    #south
    flag = True
    while flag:
        flag = False
        for a in range(len(br)-1):
            for b in range(len(br[a])):
                if br[a][b] == "O" and br[a+1][b] == ".":
                    br[a][b] = "."
                    br[a+1][b] = "O"
                    flag = True
    #east
    flag = True
    while flag:
        flag = False
        for a in range(len(br)):
            for b in range(len(br[a])-1):
                if br[a][b] == "O" and br[a][b+1] == ".":
                    br[a][b] = "."
                    br[a][b+1] = "O"
                    flag = True


for _ in range(remain):
    #north
    flag = True
    while flag:
        flag = False
        for a in range(len(br)-1):
            for b in range(len(br[a])):
                if br[a][b] == "." and br[a+1][b] == "O":
                    br[a][b] = "O"
                    br[a+1][b] = "."
                    flag = True
    #west
    flag = True
    while flag:
        flag = False
        for a in range(len(br)):
            for b in range(len(br[a])-1):
                if br[a][b] == "." and br[a][b+1] == "O":
                    br[a][b] = "O"
                    br[a][b+1] = "."
                    flag = True
    #south
    flag = True
    while flag:
        flag = False
        for a in range(len(br)-1):
            for b in range(len(br[a])):
                if br[a][b] == "O" and br[a+1][b] == ".":
                    br[a][b] = "."
                    br[a+1][b] = "O"
                    flag = True
    #east
    flag = True
    while flag:
        flag = False
        for a in range(len(br)):
            for b in range(len(br[a])-1):
                if br[a][b] == "O" and br[a][b+1] == ".":
                    br[a][b] = "."
                    br[a][b+1] = "O"
                    flag = True


ans = 0
for k in range(len(br)):
    ans += (k+1)*(br[-k-1].count("O"))
print(ans)

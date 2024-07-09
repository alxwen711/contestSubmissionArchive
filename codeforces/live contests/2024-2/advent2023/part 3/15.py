#input, default to basic integer reading file
f = open("15.txt",'r') 
ar = list(map(str,f.readline().split(",")))    
f.close()
print(len(ar))
print(ar[0],ar[-1])
ans = 0
flag = True

def label(i):
    x = 0
    for j in range(len(i)):
        x += ord(i[j])
        x *= 17
        x = x % 256
    return x
    
br = list()
for _ in range(256):
    tmp = list()
    br.append(tmp)
for i in ar:
    if i[-1] == "-":
        target = i[:-1]
        flag = False
        for a in range(256):
            for b in range(len(br[a])):
                if br[a][b][0] == target:
                    br[a].pop(b)
                    flag = True
                    break
            if flag: break
    else:
        s,v = map(str,i.split("="))
        h = label(s)
        v = int(v)
        replace = False
        for c in range(len(br[h])):
            if s == br[h][c][0]:
                replace = True
                br[h][c][1] = v
                break
        if not replace:
            br[h].append([s,v])

for t in range(256):
    for u in range(len(br[t])):
        ans += (t+1)*(u+1)*(br[t][u][1])
print(ans)


#input, default to basic integer reading file
f = open("2.txt",'r') 
ar = list()

while True:
    l = f.readline()
    if not l: break

    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        # do stuff with l here
        ar.append(l)
    
f.close()


def solve(gl):
    gll = list(gl.split(','))
    r,g,b = 0,0,0
    for u in gll:
        u = u.lstrip()
        count,col = u.split(" ")
        if col == "red": r = max(r,int(count))
        elif col == "blue": b = max(b,int(count))
        else: g = max(g,int(count))
    return r,g,b

flag = True
ans = 0
cc = 0
for i in ar:
    cc += 1
    games = i.split(":")[1]
    
    gl = list(games.split(";"))
    if flag:
        flag = False
        print(gl)
    rr,gg,bb = 0,0,0
    for j in range(len(gl)):
        r,g,b = solve(gl[j])
        rr = max(r,rr)
        gg = max(g,gg)
        bb = max(b,bb)
    ans += rr*gg*bb
    #if rr <= 12 and gg <= 13 and bb <= 14: ans += cc
print(ans)

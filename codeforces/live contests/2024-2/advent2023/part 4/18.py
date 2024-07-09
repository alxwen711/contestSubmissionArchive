"""
track every horizontal line, scan top to bottom
part 2
1359555770 is wrong, 0 check failed, no other info
96556750704866 is wrong, 0 check failed, no other info
193156683635346 is also wrong?
also not 93156683635346

determine what is going on with possible off by 1 error
has to be higher than 96556791428149?
96556251590676
"""

ar = list()
#input, default to basic integer reading file
f = open("18.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

flag = True
pts = [(0,0)] #x,y
ans = 0
for i in range(len(ar)):
    d,v,c = ar[i].split(" ")
    code = int(c[2:7],16)
    ans += code
    d = int(c[7])
    if d == 0: pts.append((pts[-1][0]+code,pts[-1][1]))
    elif d == 1: pts.append((pts[-1][0],pts[-1][1]-code))
    elif d == 2: pts.append((pts[-1][0]-code,pts[-1][1]))
    else: pts.append((pts[-1][0],pts[-1][1]+code))
assert pts[0] == pts[-1] #enclosed shape?

#this is just shoelace innit
ans2 = 0
#print(pts)
for iii in range(len(pts)-1):
    ans2 += (pts[iii][0]*pts[iii+1][1])-(pts[iii][1]*pts[iii+1][0])

print(abs(ans2//2)+ans)
print(abs(ans2//2))
print((abs(ans2//2)+ans+abs(ans2//2))//2+1)
"""

ff = open("18badidea.txt","w")
for iii in range(len(pts)-1):
    ff.write(str(pts[iii][0]))
    ff.write("\t")
    ff.write(str(pts[iii][1]))
    ff.write("\n")
    
ff.close()

hor = list()
aaa = 8764895769876987546
bbb = -aaa
for j in range(len(pts)-1):
    if pts[j][1] == pts[j+1][1]:
        aa = min(pts[j][0],pts[j+1][0])
        bb = max(pts[j][0],pts[j+1][0])
        hor.append((pts[j][1],aa,bb))
        aaa = min(aaa,aa)
        bbb = max(bbb,bb)
hor.sort()    
print(len(hor),aaa,bbb)
#apply first line, then iterate
#would apply accurate setup here, but I'm lazy
store the x/y lines in a dictionary
if it removes a line, then increase area by 1
print(hor)
lmao = [0]*20000000
w = 0
const = 5000000 #some negative

ans = 0
st = hor[0][0]
d = {}
for q in hor:
    if d.get(q[0]) == None: d[q[0]] = list()
    d[q[0]].append((q[1],q[2]))
print(d)
while st <= hor[-1][0]:
    if d.get(st) != None:
        for segment in d[st]:
            print(segment)
            #print(segment[0],segment[1])
            for bruh in range(segment[0],segment[1]+1):
                if lmao[bruh+const] == 1:
                    ans += 1
                    lmao[bruh+const] = 0
                    w -= 1
                else:
                    w += 1
                    lmao[bruh+const] = 1
            print(w,"value after segemnt")
    ans += w
    if w == 0: break
    st += 1
print(w,"end of shape, should be 0 here")
print(st)
print(ans)
"""

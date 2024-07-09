
#input, default to basic integer reading file
f = open("4.txt",'r')
ar = list()
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

#do stuff with ar

n = len(ar)
ans = 0
cards = [1]*198
for i in range(n):
    a = ar[i].split(":")[1]
    b,c = a.split("|")
    b = b.lstrip().rstrip().replace("  "," ")
    c = c.lstrip().rstrip().replace("  "," ")
    #print(b)
    br = list(map(int,b.split(" ")))
    cr = list(map(int,c.split(" ")))
    
    if i == 0: print(br,cr)
    hit = 0
    for j in br:
        if cr.count(j) != 0:
            hit += 1
    for k in range(i+1,i+1+hit):
        if k == 198: break
        cards[k] += cards[i]

        
    if hit != 0: ans += (2**(hit-1))
print(ans)
print(sum(cards))

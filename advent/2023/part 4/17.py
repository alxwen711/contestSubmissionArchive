from heapq import * #min heap

ar = list()
"""
#input, default to basic integer reading file
#a*?
#lower than 1260
#part 1: 1238
Part 2:
move in between 4 and 10 steps, kill me now.
lower than 1411, 0 leeway
lower than 1367, leeway 20 used
50 leeway gives 1372?
20 leeway, no stop still gives 1367
50 leeway, no stop
1362 FINALLY

pretty sure 0 leeway no stop works if all specific state's best are tracked instead of spots?
"""

f = open("17.txt",'r') 
while True:
    l = f.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
f.close()

def hv(x):
    return x[0]-(x[1]*2000)-(x[2]*300000)+(x[3]*45000000)+(x[4]*225000000)


print(len(ar),len(ar[0]),len(ar[-1]))

n = len(ar)

br = list()
cr = list()
for i in range(n):
    tmp = list()
    tmp2 = list()
    for j in range(n):
        tmp.append(int(ar[i][j]))
        tmp2.append(100000)
    br.append(tmp)
    cr.append(tmp2)
h = list()
heappush(h,(0,0,0,-1,0)) #(cost,-i,-j,dir,count)
leeway = 50 #adjust as needed
cycle = 0
used = {}
ans = 9999999999
while len(h) != 0: #urdl
    x = heappop(h)
    if x[1] == -n+1 and x[2] == -n+1: #hit target
        if x[0] < ans:
            ans = x[0]
            print(ans)
        #break
    cost = x[0]
    ii,jj = -x[1],-x[2]
    d = x[3]
    count = x[4]
    if cost <= (cr[ii][jj]+1000000): #give a bit of leeway for extra rule?
        if d == 0:
            if jj >= 4: #left
                nc = cost+br[ii][jj-4]+br[ii][jj-3]+br[ii][jj-2]+br[ii][jj-1]
                if nc <= cr[ii][jj-4]+leeway: #actually could give a solution
                    cr[ii][jj-4] = min(cr[ii][jj-4],nc)
                    tup = (nc,-ii,-jj+4,3,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if jj < n-4: #right
                nc = cost+br[ii][jj+4]+br[ii][jj+3]+br[ii][jj+2]+br[ii][jj+1]
                if nc <= cr[ii][jj+4]+leeway: #actually could give a solution
                    cr[ii][jj+4] = min(cr[ii][jj+4],nc)
                    tup = (nc,-ii,-jj-4,1,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if count != 10 and ii != 0: #up
                nc = cost+br[ii-1][jj]
                if nc <= cr[ii-1][jj]+leeway: #actually could give a solution
                    cr[ii-1][jj] = min(cr[ii-1][jj],nc)
                    tup = (cost+br[ii-1][jj],-ii+1,-jj,0,x[4]+1)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
                    
        elif d == 1:
            if ii >= 4: #up
                nc = cost+br[ii-4][jj]+br[ii-3][jj]+br[ii-2][jj]+br[ii-1][jj]
                if nc <= cr[ii-4][jj]+leeway: #actually could give a solution
                    cr[ii-4][jj] = min(cr[ii-4][jj],nc)
                    tup = (nc,-ii+4,-jj,0,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if ii < n-4: #down
                nc = cost+br[ii+4][jj]+br[ii+3][jj]+br[ii+2][jj]+br[ii+1][jj]
                if nc <= cr[ii+4][jj]+leeway: #actually could give a solution
                    cr[ii+4][jj] = min(cr[ii+4][jj],nc)
                    tup = (nc,-ii-4,-jj,2,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if count != 10 and jj != n-1: #right
                nc = cost+br[ii][jj+1]
                if nc <= cr[ii][jj+1]+leeway: #actually could give a solution
                    cr[ii][jj+1] = min(cr[ii][jj+1],nc)
                    tup = (cost+br[ii][jj+1],-ii,-jj-1,1,x[4]+1)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            

        elif d == 2:
            if jj >= 4: #left
                nc = cost+br[ii][jj-4]+br[ii][jj-3]+br[ii][jj-2]+br[ii][jj-1]
                if nc <= cr[ii][jj-4]+leeway: #actually could give a solution
                    cr[ii][jj-4] = min(cr[ii][jj-4],nc)
                    tup = (nc,-ii,-jj+4,3,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if jj < n-4: #right
                nc = cost+br[ii][jj+4]+br[ii][jj+3]+br[ii][jj+2]+br[ii][jj+1]
                if nc <= cr[ii][jj+4]+leeway: #actually could give a solution
                    cr[ii][jj+4] = min(cr[ii][jj+4],nc)
                    tup = (nc,-ii,-jj-4,1,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if count != 10 and ii != n-1: #down
                nc = cost+br[ii+1][jj]
                if nc <= cr[ii+1][jj]+leeway: #actually could give a solution
                    cr[ii+1][jj] = min(cr[ii+1][jj],nc)
                    tup = (cost+br[ii+1][jj],-ii-1,-jj,2,x[4]+1)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1


        elif d == 3:
            if ii >= 4: #up
                nc = cost+br[ii-4][jj]+br[ii-3][jj]+br[ii-2][jj]+br[ii-1][jj]
                if nc <= cr[ii-4][jj]+leeway: #actually could give a solution
                    cr[ii-4][jj] = min(cr[ii-4][jj],nc)
                    tup = (nc,-ii+4,-jj,0,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if ii < n-4: #down
                nc = cost+br[ii+4][jj]+br[ii+3][jj]+br[ii+2][jj]+br[ii+1][jj]
                if nc <= cr[ii+4][jj]+leeway: #actually could give a solution
                    cr[ii+4][jj] = min(cr[ii+4][jj],nc)
                    tup = (nc,-ii-4,-jj,2,4)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1
            if count != 10 and jj != 0: #left
                nc = cost+br[ii][jj-1]
                if nc <= cr[ii][jj-1]+leeway: #actually could give a solution
                    cr[ii][jj-1] = min(cr[ii][jj-1],nc)
                    tup = (cost+br[ii][jj-1],-ii,-jj+1,3,x[4]+1)
                    tuph = hv(tup)
                    if used.get(tuph) == None:
                        heappush(h,tup)
                        used[tuph] = 1


        else: #first move, can move down and right for sure
            #down
            nc = cost+br[ii+4][jj]+br[ii+3][jj]+br[ii+2][jj]+br[ii+1][jj]
            if nc <= cr[ii+4][jj]+leeway: #actually could give a solution
                cr[ii+4][jj] = min(cr[ii+4][jj],nc)
                tup = (nc,-ii-4,-jj,2,4)
                tuph = hv(tup)
                if used.get(tuph) == None:
                    heappush(h,tup)
                    used[tuph] = 1
            #right
            nc = cost+br[ii][jj+4]+br[ii][jj+3]+br[ii][jj+2]+br[ii][jj+1]
            if nc <= cr[ii][jj+4]+leeway: #actually could give a solution
                cr[ii][jj+4] = min(cr[ii][jj+4],nc)
                tup = (nc,-ii,-jj-4,1,4)
                tuph = hv(tup)
                if used.get(tuph) == None:
                    heappush(h,tup)
                    used[tuph] = 1  
        cycle += 1
        if cycle == 100000:
            print(x)
            cycle = 0


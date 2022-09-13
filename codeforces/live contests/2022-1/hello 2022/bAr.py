
for i in range(int(input())):
    n = int(input())
    st = list(map(int, input().split())) #low,high,cost
    dual = False
    lc = st[2]
    hc = st[2]
    print(st[2]) #first set
    for j in range(n-1):
        entry = list(map(int, input().split())) #l,h,c
        if dual:
            #2 set boundary
            if (entry[0] < st[0] and entry[1] >= st[1]) or (entry[1] > st[1] and entry[0] <= st[0]):
                st[2] = entry[2]
                st[0] = entry[0]
                st[1] = entry[1]
                dual = False
                #det subset
            #not subset
            elif (entry[0] < st[0]) or (entry[0] == st[0] and entry[2] < lc):
                st[0] = entry[0]
                lc = entry[2]
                entry[2] += hc 

            elif (entry[1] > st[1]) or (entry[1] == st[1] and entry[2] < hc):
                st[1] = entry[1]
                hc = entry[2]
                entry[2] += lc
                
        else: #1 set boundary
            if (entry[0] < st[0] and entry[1] >= st[1]) or (entry[1] > st[1] and entry[0] <= st[0]) or (entry[0] == st[0] and entry[1] == st[1] and entry[2] < st[2]):
                st[2] = entry[2]
                st[0] = entry[0]
                st[1] = entry[1]
                #det subset
            #not subset
            elif entry[0] < st[0]:
                dual = True
                st[0] = entry[0]
                hc = st[2]
                lc = entry[2]
                st[2] = lc + hc

            elif entry[1] > st[1]:
                dual = True
                st[1] = entry[1]
                hc = entry[2]
                lc = st[2]
                st[2] = lc + hc 
            
        #new cost print
        print(st, lc, hc)
        #print(st[2])

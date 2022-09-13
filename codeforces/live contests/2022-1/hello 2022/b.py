

for i in range(int(input())):
    n = int(input())
    low, high, cost = map(int, input().split())
    dual = False
    lc,hc = cost, cost
    print(cost) #first set
    for j in range(n-1):
        l, h, c = map(int, input().split())
        if dual:
            #2 set boundary
            if (l < low and h >= high) or (h > high and l <= low):
                cost, low, high = c, l, h
                dual = False
                #det subset
            #not subset
            elif (l < low) or (l == low and c < lc):
                low, lc = l, c
                cost = hc+lc
            elif (h > high) or (h == high and c < hc):
                high, hc = h, c
                cost = hc+lc
                
        else: #1 set boundary
            if (l < low and h >= high) or (h > high and l <= low) or (l == low and h == high and c < cost):
                cost, low, high = c, l, h
                #det subset
            #not subset
            elif l < low or h > high:
                dual = True
                if l < low:
                    low, hc, lc = l, cost, c
                else:
                    high, hc, lc = h, c, cost
                cost = hc + lc

            
        #new cost print
        print(cost)

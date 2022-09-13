import sys
for i in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    o = k
    s = str(input())
        
    #odd st-> 0, even st->1
    index = 0
    lol = ""
    if k % 2 == 1:
        #keep 0, adjust 1
        while index < n:
            if k == 0: break
            if s[index] == "1":
                k -= 1
                lol += "1 "
            else: lol += "0 "
            index += 1
        
    else:
        #keep 1, adjust 0
        while index < n:
            if k == 0: break
            if s[index] == "0":
                k -= 1
                lol += "1 "
            else: lol += "0 "
            index += 1
            
    ans = "1"*index
    if index != n:
        if o % 2 == 0: print(ans + s[index:])
        else:
            for p in range(n-index):
                if s[index+p] == "0": ans += "1"
                else: ans += "0"
            print(ans)
        lol += "0 "*(n-index)
    else:
        lol = lol[:-2]+str(int(lol[-2])+k)
        if k % 2 == 1: print(ans[:n-1]+"0")
        else: print(ans)
    print(lol)


import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
these are the indices of the values
assign highest values for the 1 indices
assign lowest values for the 2 indices
next highest go to 3, next lowest go to 4
generally assign odd indices high to low and even indices low to high
if the last x non filled spots are removed here, reverse order


"""
def gentranslators(n,ans):
    index = 0
    encode = [-1]*n
    decode = [-1]
    for i in range(n):
        if ans[i] == 0:
            index += 1
            encode[i] = index
            decode.append(i)
    return encode,decode,index
for _ in range(readint()):
    n = readint()
    ar = readar()
    miter = max(ar)
    vals = list()
    for _ in range(miter+1):
        tmp = list()
        vals.append(tmp)
    for i in range(n):
        if ar[i] == -1: vals[0].append(i)
        else: vals[ar[i]].append(i)
    #print(vals)
    ans = [0]*n
    highpt = n
    lowpt = 1
    for j in range(1,len(vals)):
        encode,decode,unfill = gentranslators(n,ans)
        if j % 2 == 1: # high assignment
            br = list()
            for i in vals[j]:
                br.append(encode[i])
            #print(br,unfill,encode)            
            # check for order reversal
            if br[-1] == unfill:
                for c in range(1,len(br)+1): 
                    if c == len(br):
                        for e in range(c//2):
                            br[-e-1],br[-c+e] = br[-c+e],br[-e-1]
                        break
                    if br[-c-1] != unfill-c:
                        for e in range(c//2):
                            br[-e-1],br[-c+e] = br[-c+e],br[-e-1]
                        break
            #br.reverse()
            #print(br)
            for b in br:
                ans[decode[b]] = highpt
                highpt -= 1
        
        else: # low assignment
            br = list()
            for i in vals[j]:
                br.append(encode[i])
            #print(br,unfill,encode)
            # check for order reversal
            if br[-1] == unfill:
                for c in range(1,len(br)+1): 
                    if c == len(br):
                        for e in range(c//2):
                            br[-e-1],br[-c+e] = br[-c+e],br[-e-1]
                        break
                    if br[-c-1] != unfill-c:
                        for e in range(c//2):
                            br[-e-1],br[-c+e] = br[-c+e],br[-e-1]
                        break
            #print(br)
            for b in br:
                ans[decode[b]] = lowpt
                lowpt += 1
        
    ans[vals[0][0]] = highpt
    print(*ans)

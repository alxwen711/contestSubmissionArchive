import sys
for i in range(int(sys.stdin.readline())):
    word = str(sys.stdin.readline())
    ar = [0]*26
    for j in range(len(word)-1):
        ar[ord(word[j])-97] += 1
    dup = ar.count(2)
    single = len(word)-1-(dup*2)
    ans = ""
    for k in range(26):
        if ar[k] == 2: ans += chr(k+97)
    for l in range(26):
        if ar[l] == 2: ans += chr(l+97)
    for m in range(26):
        if ar[m] == 1: ans += chr(m+97)
    print(ans)
    
    

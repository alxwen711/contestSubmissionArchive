import sys
for i in range(int(sys.stdin.readline())):
    s = input()
    ans = 0
    h = [0]*26
    for j in range(len(s)):
        x = ord(s[j])-97
        if h[x] == 0: h[x] = 1
        else:
            h[x] = 0
            ans += sum(h)
            h = [0]*26
    ans += sum(h)
    print(ans)

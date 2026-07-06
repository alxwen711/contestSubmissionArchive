import sys

for i in range(int(sys.stdin.readline())):
    s = str(sys.stdin.readline())
    x = str(sys.stdin.readline())
    c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(s)-1):
        c[ord(s[i])-97] += 1

    if x == "abc\n" and c[0]*c[1]*c[2] != 0: ans = "a"*c[0]+"c"*c[2]+"b"*c[1]
    else: ans = "a"*c[0]+"b"*c[1]+"c"*c[2]
    for j in range(23):
        ans += chr(j+100)*c[j+3]
    print(ans)
    

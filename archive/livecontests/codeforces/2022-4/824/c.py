import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def cycle(d,l,x):
    if l == x: return False
    st = d[ord(l)-97]
    while True:
        if st == x: return False
        if st == " ": return True
        st = d[ord(st)-97]
    return True
    

def solve(n,s):
    letters = list()
    for t in range(97,97+26):
        letters.append(chr(t))
    d = [" "]*26
    ans = list()
    for m in range(n):
        x = s[m]
        y = d[ord(x)-97]
        if y == " ":
            """
            if len(letters) == 2:
                first = ord(x)-97
                second = 0
                for w in range(26):
                    if d[w] == " " and w != first:
                        second = w
                        break
                aa,bb = letters[0],letters[1]
                if x == aa:
                    d[first] = bb
                    d[second] = aa
                else:
                    d[first] = aa
                    d[second] = bb
                    """
            if len(letters) == 1:
                d[ord(x)-97] = letters[0]
            else:
                for ss in range(len(letters)):
                    if cycle(d,letters[ss],x):
                        d[ord(x)-97] = letters[ss]
                        letters.pop(ss)
                        break
            y = d[ord(x)-97]
        ans.append(y)
        #print(d)
    print(*ans,sep="")
    return


for i in range(readint()):
    n = readint()
    s = input()
    solve(n,s)
    

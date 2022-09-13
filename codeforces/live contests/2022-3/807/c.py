import sys
#solution is to work backwards

def solve(x,s,st,end,l,n,c):
    if x <= n: return s[x-1]
    prev = 0
    for f in range(c):
        if x <= l[f]:
            if f == 0: prev = n+1
            else: prev = l[f-1]+1
            return solve(st[f]+x-prev,s,st,end,l,n,c)
    return -1 #something broke
        
for i in range(int(sys.stdin.readline())):
    n,c,q = map(int,sys.stdin.readline().split())
    s = input()
    st = list()
    end = list()
    l = list()
    length = n
    for j in range(c):
        a,b = map(int,sys.stdin.readline().split())
        st.append(a)
        end.append(b)
        length += (b-a+1)
        l.append(length)
    """
    l contains len after x copies
    st/end contains each copy
    """
    for k in range(q):
        print(solve(int(input()),s,st,end,l,n,c))

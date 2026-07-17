import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

    
def sp(x,s):
    if 2*s <= x: return s,x-s
    elif s <= x: return x-s,s
    else: return 0,x

for i in range(readint()):
    #a -> low to high
    n,s = readints()
    ar = readar()
    br = list()
    br.append(ar[0])
    for j in range(1,n-1):
        a,b = sp(ar[j],s)
        br.append(a)
        br.append(b)
    br.append(ar[n-1])
    ansa = 0
    fronta = list()
    fronta.append(0)
    bl = len(br)
    for k in range(bl//2):
        ansa += br[2*k]*br[2*k+1]
        fronta.append(ansa)
    backa = list()
    for kk in range(len(fronta)):
        backa.append(fronta[-1]-fronta[-kk-1])
    ansb = 0
    frontb = list()
    frontb.append(0)
    ansb += br[0]*br[2]
    frontb.append(ansb)
    for m in range(n-3):
        ansb += br[2*m+1]*br[2*m+4]
        frontb.append(ansb)
    ansb += br[bl-1]*br[bl-3]
    frontb.append(ansb)
    backb = list()
    for ss in range(len(frontb)):
        backb.append(frontb[-1]-frontb[-ss-1])
    ans = min(ansa,ansb)
    pairs = len(br)//2
    for v in range(1,pairs-1):
        ans = min(ans,fronta[v]+backb[pairs-v-1]+br[2*v]*br[2*v+2])
        ans = min(ans,frontb[v]+backa[pairs-v-1]+br[2*v-1]*br[2*v+1])
    print(ans)    

    

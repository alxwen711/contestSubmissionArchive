import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
more students than colleges
at most 1.5 mill preferences
O(k)
"""

for i in range(readint()):
    n,m = readints()
    ar = readar() # college ranks
    br = readar() # student ranks
    cr = list()
    d = {}
    for tt in range(n):
        d[tt+1] = ar[tt]
    for j in range(m):
        tmp = readar()
        cr.append(tmp) #[student id][prefence rank]
        #[student id][0] is number of colleges in list
    # (exam rank, college rank, student id)
    """
    update ONLY if college is open AND student is open
    """
    college = [-1]*(n+1) #college to student
    student = [0]*(m) # student to college
    choices = list()
    for k in range(m):
        for l in range(1,len(cr[k])):
            choices.append((br[k],d[cr[k][l]],k))
    choices.sort()
    for p in choices:
        cid = p[1]
        sid = p[2]
        if college[cid] == -1 and student[sid] == 0:
            student[sid] = cid
            college[cid] = sid
    x = student[0]
    if x == 0: print(0)
    else:
        for snth in range(n):
            if ar[snth] == x:
                print(snth+1)
                break

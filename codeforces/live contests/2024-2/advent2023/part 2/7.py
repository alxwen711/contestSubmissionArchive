ar = list()
#input, default to basic integer reading file
ff = open("7.txt",'r')

def f(freq,x):
    ar = list()
    for i in range(len(freq)):
        if freq[i] == x: ar.append(i)
    return ar
"""
def evaluate(x):
    freq = [x.count("A"),x.count("K"),x.count("Q"),x.count("J"),x.count("T"),x.count("9"),x.count("8"),x.count("7"),x.count("6"),x.count("5"),x.count("4"),x.count("3"),x.count("2")]
    if freq.count(5) == 1: #5 of kind
        return [0,freq.index(5)]
    elif freq.count(4) == 1: #4 of kind
        return [1,freq.index(4),freq.index(1)]
    elif freq.count(3) == 1: #3 of kind
        if freq.count(2) == 1: #full house
            return [2,freq.index(3),freq.index(2)]
        else:
            cr = f(freq,1)
            return [3,freq.index(3),cr[0],cr[1]]
    elif freq.count(2) != 0: #pair
        cr = f(freq,2)
        if len(cr) == 2:
            return [4,cr[0],cr[1],freq.index(1)]
        else:
            dr = f(freq,1)
            return [5,cr[0],dr[0],dr[1],dr[2]]
    else:
        er = f(freq,1)
        return [6,er[0],er[1],er[2],er[3],er[4]]
"""


def evaluate(x):
    freq = [x.count("A"),x.count("K"),x.count("Q"),x.count("J"),x.count("T"),x.count("9"),x.count("8"),x.count("7"),x.count("6"),x.count("5"),x.count("4"),x.count("3"),x.count("2")]
    if freq.count(5) == 1: #5 of kind
        return 0
    elif freq.count(4) == 1: #4 of kind
        return 1
    elif freq.count(3) == 1: #3 of kind
        if freq.count(2) == 1: #full house
            return 2
        else:
            return 3
    elif freq.count(2) != 0: #pair
        cr = f(freq,2)
        if len(cr) == 2:
            return 4
        else:
            return 5
    else:
        return 6

def evaluate2(x):
    grid = ["A","K","Q","T","9","8","7","6","5","4","3","2"]
    score = 9999
    for i in grid:
        s = ""
        for j in x:
            if j == "J": s += i
            else: s += j
        score = min(score,evaluate(s))
    return score
def assign(x):
    order = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
    ar = list()
    for i in x:
        for j in range(len(order)):
            if i == order[j]:
                ar.append(j)
                break
    return ar
while True:
    l = ff.readline()
    if not l: break

    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        l = l[:-1]
        ar.append(l)
    
ff.close()
br = list()
for i in ar:
    a,b = i.split(" ")
    b = int(b)
    br.append((evaluate2(a),assign(a),b))

br.sort()
ans = 0
val = 1
for j in range(len(br)):
    ans += (val*br[-j-1][2])
    val += 1
print(ans)
print(br[:10])

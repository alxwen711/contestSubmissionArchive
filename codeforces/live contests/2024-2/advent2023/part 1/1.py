

def first(x,numbers):
    n = len(x)
    for i in range(len(x)):
        if 48 <= ord(x[i]) <= 57: return int(x[i])
        #go through each possible digit
        for j in numbers.keys():
            if len(j)+i <= n:
                if j == x[i:i+len(j)]: return numbers[j]
                


        
def last(x,numbers):
    n = len(x)
    for j in range(len(x)):
        if 48 <= ord(x[-j-1]) <= 57: return int(x[-j-1])
        #go through each possible digit
        for k in numbers.keys():
            if (j+1) >= len(k):
                if k == x[(n-j-1):n-j-1+len(k)]: return numbers[k]

def ff(x):
    numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    return first(x,numbers)*10+last(x,numbers)
#input, default to basic integer reading file
ar = list()

f = open("1.txt",'r') 
while True:
    l = f.readline()
    if not l: break
    #do stuff with l here
    if len(l) != 1: #not empty line, will read "\n" at end
        ar.append(l[:-1])
    
f.close()


ans = 0
for j in ar:
    ans += ff(j)
print(ans)

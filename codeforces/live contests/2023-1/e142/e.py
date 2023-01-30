import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
from math import gcd,sqrt,ceil
from random import randint


def prime(n: int) -> bool:
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n <= 1: return False
    d,s = n-1,0
    while d % 2 == 0:
        s += 1
        d = d // 2
    for i in range(100):
        a = randint(2,n-2)
        if trial(n,s,a,d): return False
    return True


def trial(n: int, s: int, a: int, d: int) -> bool:
    val = pow(a,d,n)
    if val == 1 or val == n-1: return False
    for i in range(s-1):
        val = pow(val,2,n)
        if val == n-1: return False
    return True

#copy only the code above if you just need a primality test




def fact_func(x: int, r: int, c: int) -> int: #may need to use other c's than 1
    return (x*x+c) % r


def find_factor(n: int) -> int: #assume a composite number is given
    for c in range(1,11):
        if c >= n: break
        x,y,a = 2,2,1
        while a == 1: #unsure how many iterations are needed here
            x = fact_func(x,n,c)
            y = fact_func(fact_func(y,n,c),n,c)
            a = gcd(n,abs(x-y))
            if x == y:
                break
        if a != n: break #factor has been found
    return a


def factorize(n: int) -> list[list[int]]:
    if n <= 3: return [[n,1]] #0-1 edge cases
    #break n into smaller factors
    d = {}
    while not prime(n) and n != 1:
        x = find_factor(n)
        if d.get(x) == None: d[x] = 0
        d[x] += 1
        n = n // x
    if n != 1:
        if d.get(n) == None: d[n] = 0
        d[n] += 1
    
    #check factors
    k = list(d.keys())
    for i in range(len(k)):
        a,b = k[i],d[k[i]]
        if not prime(a):
            c = trial_div(a)
            for j in range(len(c)):
                factor = c[j]
                if d.get(factor) == None: d[factor] = 0
                d[factor] += b
            """
            wip method using factorize recursively
            c = factorize(a)
            for j in range(len(c)):
                factor,freq = c[j][0], c[j][1]
                if d.get(factor) == None: d[factor] = 0
                d[factor] += (freq*b)
            """
            d[a] = 0
            
    #translate from dict to list[int]
    k = list(d.keys())
    ans = list()
    for j in range(len(k)):
        if d[k[j]] != 0:
            ans.append([k[j],d[k[j]]])
    return ans
     

#keep div and trial_div for completeness
def div(n: int, ar: list) -> list[int]:
    if n == 1: return ar
    if n % 2 == 0:
        ar.append(2)
        return div(n//2,ar)

    for i in range(3,ceil(sqrt(n+1)),2): #3,5,7,...,sqrt(n)
        if n % i == 0:
            ar.append(i)
            return div(n//i,ar)
    #n is prime
    ar.append(n)
    return ar


def trial_div(n: int) -> list[int]:
    if n <= 3: return [n]
    else: return div(n,list())

    
for i in range(readint()):
    n,a,b = readints()
    f = factorize(a*b)
    #print(f)
    ar = list()
    for j in range(len(f)):
        if f[j][0] <= n: ar.append(f[j])
    #only look at upper triangle in times table

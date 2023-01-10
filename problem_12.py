import time

def howmanydivisors(n):
    count = 2 
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            count += 2
        i += 1
    if i ** 2 == n:
        count += 1
    return count

def triagularnum(numofdivisors):
    for n in range(1,numofdivisors**2):
        triang = int((n*(n+1))/2)
        if howmanydivisors(triang) > numofdivisors:
            return triang

start = time.time()
print(triagularnum(500))
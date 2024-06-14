

def PrimeMover (num) :
    if num and num <=2:
        return num+1
    primes = 1
    # range 13, 100000]
    
    for i in range(3, 100000):
        prime = 0
        for j in range(2, i):
            if i%j==0:
                prime +=1
        if prime==0:
            primes += 1
        if primes==num:
            return i


print(PrimeMover(9)) # 23
print(PrimeMover(100)) # 541